#!/usr/bin/env python3
"""HIPAA Security Rule crosswalk scorer (dependency-free).

Maps 45 CFR 164 Security Rule implementation specifications to NIST SP 800-53 Rev. 5
and COBIT 2019 objectives, then scores an existing control inventory against them.

Status per specification:
  Covered  - every mapped NIST control is in the inventory
  Partial  - some mapped NIST controls are in the inventory
  Gap      - none are in the inventory

Usage: python3 src/crosswalk.py [--map data/hipaa_security_rule_map.csv]
       [--inventory data/control_inventory.csv] [--out report.md]
"""
import argparse, csv, collections

def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def score(rows, inv):
    have = {r["nist_800_53_r5"].strip() for r in inv}
    out = []
    for r in rows:
        need = [c for c in r["nist_800_53_r5"].split(";") if c]
        hit = [c for c in need if c in have]
        st = "Covered" if len(hit) == len(need) else ("Partial" if hit else "Gap")
        out.append({**r, "hit": hit, "missing": [c for c in need if c not in hit], "status": st})
    return out

def report(scored, inv):
    ev = {r["nist_800_53_r5"]: r["evidence"] for r in inv}
    L = ["# HIPAA Security Rule coverage report", ""]
    tot = collections.Counter(s["status"] for s in scored)
    L += [f"Specifications scored: {len(scored)}  |  Covered: {tot['Covered']}  |  Partial: {tot['Partial']}  |  Gap: {tot['Gap']}", ""]
    L += ["## By safeguard", "", "| Safeguard | Covered | Partial | Gap |", "|---|---|---|---|"]
    by = collections.defaultdict(collections.Counter)
    for s in scored: by[s["safeguard"]][s["status"]] += 1
    for k, c in by.items(): L.append(f"| {k} | {c['Covered']} | {c['Partial']} | {c['Gap']} |")
    L += ["", "## Detail", "", "| CFR | Specification | R/A | Status | Evidence on hand | Remaining NIST controls | COBIT 2019 |", "|---|---|---|---|---|---|---|"]
    for s in scored:
        e = "; ".join(f"{c}: {ev[c]}" for c in s["hit"]) or "-"
        L.append(f"| {s['cfr']} | {s['implementation_spec']} | {s['type']} | {s['status']} | {e} | {', '.join(s['missing']) or '-'} | {s['cobit_2019'].replace(';', ', ')} |")
    return "\n".join(L) + "\n"

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--map", default="data/hipaa_security_rule_map.csv")
    a.add_argument("--inventory", default="data/control_inventory.csv")
    a.add_argument("--out", default="report.md")
    a = a.parse_args()
    m, inv = load(a.map), load(a.inventory)
    sc = score(m, inv)
    open(a.out, "w", encoding="utf-8").write(report(sc, inv))
    print(f"wrote {a.out}:", dict(collections.Counter(s["status"] for s in sc)))
