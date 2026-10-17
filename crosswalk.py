#!/usr/bin/env python3
"""FFIEC IT Examination Handbook -> COBIT 2019 crosswalk.

    python crosswalk.py validate                    # data integrity checks
    python crosswalk.py lookup IS-06                # FFIEC expectation -> COBIT
    python crosswalk.py lookup DSS05                # COBIT objective/practice -> FFIEC
    python crosswalk.py report                      # crosswalk + coverage reports in output/
    python crosswalk.py gap examples/assessment.csv # gap analysis from a COBIT capability assessment

Standard library only (Python 3.10+).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "output"

STRENGTHS = ("primary", "supporting")
# Set-theory relationship of the FFIEC expectation to the COBIT element (after NIST IR 8477).
RELATIONSHIPS = {
    "equivalent": "FFIEC expectation and COBIT element cover substantially the same scope",
    "subset_of": "FFIEC expectation is narrower than the COBIT element",
    "superset_of": "FFIEC expectation is broader than the COBIT element",
    "intersects": "Scopes overlap; each has content the other lacks",
}


@dataclass(frozen=True)
class Expectation:
    id: str
    booklet: str
    topic: str
    text: str


@dataclass(frozen=True)
class Mapping:
    ffiec_id: str
    cobit_id: str
    strength: str
    relationship: str
    rationale: str

    @property
    def objective(self) -> str:
        return self.cobit_id.split(".")[0]


class Crosswalk:
    def __init__(self, data_dir: Path = DATA):
        self.cobit = json.loads((data_dir / "cobit_2019.json").read_text(encoding="utf-8"))
        with (data_dir / "ffiec_expectations.csv").open(encoding="utf-8", newline="") as f:
            self.expectations = [Expectation(r["ffiec_id"], r["booklet"], r["topic"], r["expectation"])
                                 for r in csv.DictReader(f)]
        with (data_dir / "mappings.csv").open(encoding="utf-8", newline="") as f:
            self.mappings = [Mapping(**r) for r in csv.DictReader(f)]
        self.by_id = {e.id: e for e in self.expectations}

    # ---- lookups ------------------------------------------------------------
    def cobit_name(self, cobit_id: str) -> str:
        return self.cobit["practices"].get(cobit_id) or self.cobit["objectives"].get(cobit_id, "")

    def maps_for(self, ffiec_id: str) -> list[Mapping]:
        order = {s: i for i, s in enumerate(STRENGTHS)}
        return sorted((m for m in self.mappings if m.ffiec_id == ffiec_id), key=lambda m: order[m.strength])

    def ffiec_for(self, cobit_id: str) -> list[Mapping]:
        """Mappings to a COBIT objective (including its practices) or to a specific practice."""
        if "." in cobit_id:
            return [m for m in self.mappings if m.cobit_id in (cobit_id, cobit_id.split(".")[0])]
        return [m for m in self.mappings if m.objective == cobit_id]

    def booklets(self) -> list[str]:
        return list(dict.fromkeys(e.booklet for e in self.expectations))

    # ---- validation -----------------------------------------------------------
    def validate(self) -> list[str]:
        errs: list[str] = []
        ids = [e.id for e in self.expectations]
        errs += [f"duplicate FFIEC id {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
        seen = set()
        for m in self.mappings:
            where = f"{m.ffiec_id} -> {m.cobit_id}:"
            if m.ffiec_id not in self.by_id:
                errs.append(f"{where} unknown FFIEC id")
            if not self.cobit_name(m.cobit_id):
                errs.append(f"{where} not a COBIT 2019 objective or practice in data/cobit_2019.json")
            if m.strength not in STRENGTHS:
                errs.append(f"{where} strength '{m.strength}' not in {STRENGTHS}")
            if m.relationship not in RELATIONSHIPS:
                errs.append(f"{where} relationship '{m.relationship}' not in {tuple(RELATIONSHIPS)}")
            if not m.rationale.strip():
                errs.append(f"{where} missing rationale")
            if (m.ffiec_id, m.cobit_id) in seen:
                errs.append(f"{where} duplicate mapping")
            seen.add((m.ffiec_id, m.cobit_id))
        for e in self.expectations:
            if not any(m.strength == "primary" for m in self.maps_for(e.id)):
                errs.append(f"{e.id}: no primary COBIT mapping")
        return errs

    # ---- coverage ---------------------------------------------------------------
    def coverage(self) -> dict:
        per_obj: dict[str, dict] = {o: {"primary": set(), "supporting": set()} for o in self.cobit["objectives"]}
        for m in self.mappings:
            per_obj[m.objective][m.strength].add(m.ffiec_id)
        rel = defaultdict(int)
        for m in self.mappings:
            rel[m.relationship] += 1
        return {
            "per_objective": per_obj,
            "unmapped_objectives": [o for o, v in per_obj.items() if not (v["primary"] or v["supporting"])],
            "relationships": dict(rel),
        }

    # ---- gap analysis -------------------------------------------------------------
    def gap(self, assessment: dict[str, tuple[int, int]]) -> list[dict]:
        """assessment: COBIT objective -> (current capability, target capability), levels 0-5.

        Each FFIEC expectation is scored on its PRIMARY mappings (practices roll up to their
        objective): gap = largest (target - current) shortfall; status gap / meets / not_assessed.
        """
        rows = []
        for e in self.expectations:
            prim = sorted({m.objective for m in self.maps_for(e.id) if m.strength == "primary"})
            shortfalls, unassessed = {}, []
            for o in prim:
                if o not in assessment:
                    unassessed.append(o)
                    continue
                cur, tgt = assessment[o]
                if cur < tgt:
                    shortfalls[o] = tgt - cur
            if shortfalls:
                status = "gap"
            elif unassessed:
                status = "not_assessed"
            else:
                status = "meets"
            rows.append({"ffiec_id": e.id, "booklet": e.booklet, "topic": e.topic, "status": status,
                         "gap_levels": max(shortfalls.values(), default=0),
                         "short_objectives": sorted(shortfalls), "unassessed": unassessed})
        order = {"gap": 0, "not_assessed": 1, "meets": 2}
        return sorted(rows, key=lambda r: (order[r["status"]], -r["gap_levels"], r["ffiec_id"]))

    @staticmethod
    def priorities(rows: list[dict], assessment: dict[str, tuple[int, int]]) -> list[dict]:
        """Rank COBIT objectives by how many FFIEC expectations their shortfall blocks."""
        blocks = defaultdict(list)
        for r in rows:
            for o in r["short_objectives"]:
                blocks[o].append(r["ffiec_id"])
        out = [{"objective": o, "current": assessment[o][0], "target": assessment[o][1],
                "shortfall": assessment[o][1] - assessment[o][0], "ffiec_blocked": ids}
               for o, ids in blocks.items()]
        return sorted(out, key=lambda p: (-len(p["ffiec_blocked"]) * p["shortfall"], p["objective"]))


def load_assessment(path: Path) -> dict[str, tuple[int, int]]:
    out = {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            obj = r["cobit_objective"].strip().upper()
            cur, tgt = int(r["current_capability"]), int(r["target_capability"])
            if not (0 <= cur <= 5 and 0 <= tgt <= 5):
                raise ValueError(f"{obj}: capability levels must be 0-5")
            out[obj] = (cur, tgt)
    return out


# ---- Markdown rendering ----------------------------------------------------------------
def md_crosswalk(xw: Crosswalk) -> str:
    L = ["# FFIEC → COBIT 2019 crosswalk", "",
         "Primary mappings in **bold**. Relationship = how the FFIEC expectation's scope compares to the COBIT element.", ""]
    for b in xw.booklets():
        L += [f"## {b}", "", "| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |",
              "| --- | --- | --- | --- | --- | --- |"]
        for e in (e for e in xw.expectations if e.booklet == b):
            for i, m in enumerate(xw.maps_for(e.id)):
                cid = f"**{m.cobit_id}**" if m.strength == "primary" else m.cobit_id
                first = (f"{e.id}", e.topic) if i == 0 else ("", "")
                L.append(f"| {first[0]} | {first[1]} | {cid} {xw.cobit_name(m.cobit_id)} | {m.strength} | "
                         f"{m.relationship} | {m.rationale} |")
        L.append("")
    return "\n".join(L)


def md_coverage(xw: Crosswalk) -> str:
    cov = xw.coverage()
    L = ["# COBIT 2019 coverage by the FFIEC crosswalk", "",
         f"{len(xw.expectations)} FFIEC expectations, {len(xw.mappings)} mappings, "
         f"{40 - len(cov['unmapped_objectives'])} of 40 COBIT objectives referenced.", "",
         "| COBIT objective | Primary for | Supporting for |", "| --- | --- | --- |"]
    for o, v in cov["per_objective"].items():
        if v["primary"] or v["supporting"]:
            L.append(f"| {o} {xw.cobit['objectives'][o]} | {', '.join(sorted(v['primary'])) or '—'} | "
                     f"{', '.join(sorted(v['supporting'])) or '—'} |")
    L += ["", "## COBIT objectives with no FFIEC mapping", "",
          "These are candidates for review, not necessarily gaps: the FFIEC handbook simply may not set expectations there.", ""]
    L += [f"- {o} {xw.cobit['objectives'][o]}" for o in cov["unmapped_objectives"]]
    L += ["", "## Relationship types", "", "| Relationship | Count | Meaning |", "| --- | --- | --- |"]
    L += [f"| {k} | {cov['relationships'].get(k, 0)} | {v} |" for k, v in RELATIONSHIPS.items()]
    return "\n".join(L) + "\n"


def md_gap(xw: Crosswalk, rows: list[dict], prios: list[dict]) -> str:
    n = {s: sum(r["status"] == s for r in rows) for s in ("meets", "gap", "not_assessed")}
    L = ["# FFIEC readiness gap analysis (from COBIT capability assessment)", "",
         f"**{n['meets']}** expectations meet target · **{n['gap']}** have gaps · **{n['not_assessed']}** not assessed "
         f"(of {len(rows)}).", "",
         "## Remediation priorities", "",
         "COBIT objectives ranked by shortfall × number of FFIEC expectations they hold back.", "",
         "| COBIT objective | Current | Target | Shortfall | FFIEC expectations affected |", "| --- | --- | --- | --- | --- |"]
    L += [f"| {p['objective']} {xw.cobit['objectives'][p['objective']]} | {p['current']} | {p['target']} | "
          f"{p['shortfall']} | {', '.join(p['ffiec_blocked'])} |" for p in prios]
    L += ["", "## By FFIEC expectation", "", "| FFIEC | Booklet | Topic | Status | Gap (levels) | Short objectives |",
          "| --- | --- | --- | --- | --- | --- |"]
    L += [f"| {r['ffiec_id']} | {r['booklet']} | {r['topic']} | {r['status']} | {r['gap_levels'] or '—'} | "
          f"{', '.join(r['short_objectives'] + [o + ' (not assessed)' for o in r['unassessed']]) or '—'} |" for r in rows]
    return "\n".join(L) + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {path.relative_to(ROOT).as_posix()}")


# ---- CLI ---------------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="FFIEC IT Examination Handbook -> COBIT 2019 crosswalk")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    lk = sub.add_parser("lookup"); lk.add_argument("id")
    sub.add_parser("report")
    gp = sub.add_parser("gap"); gp.add_argument("assessment", type=Path)
    a = p.parse_args(argv)
    xw = Crosswalk()

    errs = xw.validate()
    if a.cmd == "validate" or errs:
        if errs:
            print("INVALID:\n  " + "\n  ".join(errs))
            return 1
        cov = xw.coverage()
        print(f"OK - {len(xw.expectations)} FFIEC expectations across {len(xw.booklets())} booklets, "
              f"{len(xw.mappings)} mappings, {40 - len(cov['unmapped_objectives'])}/40 COBIT objectives referenced")
        return 0

    if a.cmd == "lookup":
        key = a.id.strip().upper()
        if key in xw.by_id:
            e = xw.by_id[key]
            print(f"{e.id}  [{e.booklet}] {e.topic}\n  {e.text}")
            for m in xw.maps_for(e.id):
                print(f"  {m.strength:<10} {m.cobit_id:<9} {xw.cobit_name(m.cobit_id)}  ({m.relationship}) - {m.rationale}")
        elif xw.cobit_name(key):
            print(f"{key}  {xw.cobit_name(key)}")
            for m in xw.ffiec_for(key):
                e = xw.by_id[m.ffiec_id]
                print(f"  {m.strength:<10} {e.id:<7} [{e.booklet}] {e.topic}  (via {m.cobit_id})")
        else:
            print(f"error: '{a.id}' is neither an FFIEC id nor a COBIT 2019 objective/practice", file=sys.stderr)
            return 1
        return 0

    if a.cmd == "report":
        write(OUT / "crosswalk.md", md_crosswalk(xw))
        write(OUT / "coverage.md", md_coverage(xw))
        rows = [{"ffiec_id": m.ffiec_id, "booklet": xw.by_id[m.ffiec_id].booklet, "topic": xw.by_id[m.ffiec_id].topic,
                 "cobit_id": m.cobit_id, "cobit_name": xw.cobit_name(m.cobit_id), "strength": m.strength,
                 "relationship": m.relationship, "rationale": m.rationale} for m in xw.mappings]
        buf = OUT / "crosswalk.csv"
        with buf.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader(); w.writerows(rows)
        print(f"wrote {buf.relative_to(ROOT).as_posix()}")
        return 0

    if a.cmd == "gap":
        try:
            assessment = load_assessment(a.assessment)
        except (OSError, KeyError, ValueError) as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
        unknown = [o for o in assessment if o not in xw.cobit["objectives"]]
        if unknown:
            print(f"error: not COBIT 2019 objectives: {', '.join(unknown)}", file=sys.stderr)
            return 1
        rows = xw.gap(assessment)
        write(OUT / "gap_report.md", md_gap(xw, rows, xw.priorities(rows, assessment)))
        n = sum(r["status"] == "gap" for r in rows)
        print(f"{n} of {len(rows)} FFIEC expectations have COBIT capability gaps")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
