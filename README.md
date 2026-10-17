# FFIEC → COBIT 2019 Crosswalk

A small, tested crosswalk that maps **FFIEC IT Examination Handbook** expectations to **COBIT 2019** governance and management objectives. It then uses a COBIT capability assessment to show which FFIEC examination areas a financial institution is not ready for.

It's built for US banks and credit unions that run IT governance on COBIT but are examined against the FFIEC handbook. The crosswalk answers three questions:

- **Forward:** which COBIT processes evidence a given FFIEC expectation?
- **Reverse:** which FFIEC exam areas does a COBIT objective support?
- **Gap:** given current vs. target COBIT capability levels, where is the institution exposed before an exam, and what should be fixed first?

## What's included

| Path | Contents |
| --- | --- |
| `data/ffiec_expectations.csv` | 43 paraphrased expectations from 7 handbook booklets |
| `data/mappings.csv` | 88 FFIEC → COBIT mappings, each with strength, relationship type and a written rationale |
| `data/cobit_2019.json` | The 40 COBIT 2019 objectives, plus the management practices that are mapped at practice level |
| `crosswalk.py` | CLI: validate, lookup, reports, gap analysis (Python 3.10+, standard library only) |
| `examples/assessment.csv` | Sample COBIT capability assessment for a fictional institution |
| `output/` | Generated reports: `crosswalk.md`, `crosswalk.csv`, `coverage.md`, `gap_report.md` |
| `test_crosswalk.py` | Unit tests for data integrity, lookups and gap logic |

### FFIEC booklets covered

| Booklet | Expectations | Edition used |
| --- | --- | --- |
| Management | 6 | 2015 |
| Information Security | 18 | 2016 |
| Business Continuity Management | 6 | 2019 |
| Architecture, Infrastructure, and Operations | 5 | 2021 |
| Development, Acquisition, and Maintenance | 3 | 2024 |
| Audit | 2 | 2012 |
| Outsourcing Technology Services | 3 | 2004 |

> **Why not the FFIEC Cybersecurity Assessment Tool (CAT)?** The FFIEC retired the CAT on 31 August 2025 and pointed institutions to frameworks such as NIST CSF 2.0 and the CISA Cybersecurity Performance Goals. The IT Examination Handbook is still the reference examiners use, so this crosswalk maps from it.

## Methodology

Each mapping records three judgments, so that a reviewer can challenge it:

1. **Strength.** A **primary** mapping means the COBIT element substantively addresses the expectation. A **supporting** mapping means it contributes evidence. Gap analysis scores primary mappings only.
2. **Relationship.** How the two scopes compare, using set-theory terms adapted from NIST IR 8477:

   | Relationship | Meaning | Count |
   | --- | --- | --- |
   | `equivalent` | Substantially the same scope | 16 |
   | `subset_of` | The FFIEC expectation is narrower than the COBIT element | 3 |
   | `superset_of` | The FFIEC expectation is broader, so COBIT alone leaves a residual | 2 |
   | `intersects` | Overlapping, and each has content the other lacks | 67 |

   The `superset_of` rows are the most useful in an exam. For example, **IS-15 Incident response → DSS02** is marked `superset_of` because FFIEC expects customer and regulatory notification, which DSS02 does not cover. That residual is picked up by a supporting mapping to MEA03.
3. **Rationale.** A one-line justification on every mapping.

Mappings point to a COBIT **objective** (e.g. `APO13`) or, where more precise, a **management practice** (e.g. `DSS05.04`). Practices roll up to their objective for scoring.

**Gap scoring.** Each FFIEC expectation takes the largest shortfall (target − current capability level) among its primary COBIT objectives. Remediation priorities rank COBIT objectives by *shortfall × number of FFIEC expectations held back*, so one improvement that clears several exam areas ranks first.

## Quick start

```bash
python crosswalk.py validate                     # integrity checks
python crosswalk.py lookup IS-06                 # FFIEC -> COBIT
python crosswalk.py lookup APO10.04              # COBIT -> FFIEC
python crosswalk.py report                       # crosswalk + coverage reports in output/
python crosswalk.py gap examples/assessment.csv  # gap analysis -> output/gap_report.md
python -m unittest -v test_crosswalk
```

To assess your own institution, copy `examples/assessment.csv` and fill in `current_capability` and `target_capability` (COBIT capability levels 0–5) for each objective.

## Sample results

**Coverage.** The 43 FFIEC expectations map to **35 of 40** COBIT objectives. The five with no FFIEC counterpart are APO04 Innovation, APO05 Portfolio, APO08 Relationships, APO11 Quality and BAI05 Organizational Change. That's expected: the handbook focuses on risk and control rather than value delivery.

**Gap analysis** for the fictional institution in `examples/assessment.csv`: 15 of 43 expectations meet target and 28 have gaps. The top remediation priorities are:

| COBIT objective | Current → target | FFIEC expectations affected |
| --- | --- | --- |
| APO10 Managed Vendors | 2 → 4 | BCM-06, IS-12, OTS-01, OTS-02, OTS-03 |
| DSS05 Managed Security Services | 3 → 4 | IS-06, IS-07, IS-08, IS-10, IS-14, IS-16 |
| DSS04 Managed Continuity | 3 → 4 | BCM-01 to BCM-05 |
| APO12 Managed Risk | 3 → 4 | IS-02, IS-04, IS-13, MGT-02 |

So raising vendor management by two capability levels addresses third-party findings across three separate booklets.

## Limitations

- **Expert-judgment mapping.** This is not an official FFIEC or ISACA crosswalk. Validate it with your compliance and audit teams before relying on it.
- **Paraphrased, topic-level expectations.** They summarize handbook content and are not quotations. Booklet section numbering isn't reproduced, so check the current text and editions at [ithandbook.ffiec.gov](https://ithandbook.ffiec.gov/).
- **Not exhaustive.** Booklets such as Retail Payment Systems, Wholesale Payment Systems and Supervision of Technology Service Providers are out of scope.
- **Capability is not effectiveness.** COBIT capability levels show how mature a process is, not whether its controls operate effectively. Pair the gap results with control testing.
- **Third-party risk.** For third-party risk, also consider the 2023 *Interagency Guidance on Third-Party Relationships: Risk Management* (Federal Reserve, FDIC, OCC), which goes beyond the 2004 Outsourcing booklet.

## Possible extensions

- Add NIST CSF 2.0 as a third column (the CAT's recommended successor), linking FFIEC → CSF → COBIT.
- Map COBIT practices to evidence artifacts (policies, reports, tickets) to produce an exam evidence request list.
- Export the gap results to CSV or a dashboard for tracking remediation.
