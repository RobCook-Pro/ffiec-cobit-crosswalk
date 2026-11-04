# HIPAA Security Rule Crosswalk

A small, dependency-free Python tool that maps the HIPAA Security Rule (45 CFR 164 Subpart C) implementation specifications to **NIST SP 800-53 Rev. 5** controls and **COBIT 2019** objectives, then scores an existing control inventory against them.

It follows the same approach as my [DORA crosswalk](https://github.com/robcookpro-collab/dora-crosswalk): start from the control set an organization already tests and show how far it already discharges a regulation, and where the residual obligations are.

## What is in the repo

| Path | Purpose |
|---|---|
| `data/hipaa_security_rule_map.csv` | 46 implementation specifications (164.308, .310, .312, .316), Required/Addressable flag, mapped NIST 800-53 Rev. 5 controls, mapped COBIT 2019 objectives |
| `data/control_inventory.csv` | Example inventory of controls tested (SoD, access review, password authentication, FIM, configuration review). Replace it with your own |
| `src/crosswalk.py` | Scores each specification as Covered, Partial or Gap and writes `report.md` |
| `test_crosswalk.py` | Unit test for the scoring logic |
| `report.md` | Output for the example inventory |

## Run it

```
python3 src/crosswalk.py
python3 test_crosswalk.py
```

Use `--inventory your_inventory.csv --out your_report.md` for your own data. The inventory needs a `nist_800_53_r5` column with control IDs such as `AC-2`.

## Scoring

- **Covered**: every NIST control mapped to the specification is in the inventory.
- **Partial**: some are.
- **Gap**: none are.

"Covered" means the mapped controls are tested in the inventory. It does not mean the organization is HIPAA compliant.

## Limits

- The mappings are my analytical crosswalk, informed by the structure of NIST SP 800-66 Rev. 2. They are not an official HHS or NIST mapping, and reasonable reviewers may map some specifications differently.
- It covers the Security Rule only. The Privacy Rule, the Breach Notification Rule, business associate agreement terms and PHI-specific scoping are out of scope.
- Several specifications are Addressable under HIPAA, which allows documented alternatives. The tool scores them the same way and flags the Required/Addressable type for context.
- It is a study and analysis aid, not legal or compliance advice.
