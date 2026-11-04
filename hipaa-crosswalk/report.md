# HIPAA Security Rule coverage report

Specifications scored: 46  |  Covered: 3  |  Partial: 12  |  Gap: 31

## By safeguard

| Safeguard | Covered | Partial | Gap |
|---|---|---|---|
| Administrative | 2 | 7 | 14 |
| Physical | 0 | 1 | 9 |
| Technical | 1 | 4 | 4 |
| Organizational | 0 | 0 | 4 |

## Detail

| CFR | Specification | R/A | Status | Evidence on hand | Remaining NIST controls | COBIT 2019 |
|---|---|---|---|---|---|---|
| 164.308(a)(1)(ii)(A) | Risk analysis | R | Gap | - | RA-1, RA-3, RA-9 | APO12, APO13 |
| 164.308(a)(1)(ii)(B) | Risk management | R | Partial | CA-5: Remediation plan tracking and retesting through closure | RA-7, PM-9 | APO12, APO13 |
| 164.308(a)(1)(ii)(C) | Sanction policy | R | Gap | - | PS-8 | APO07 |
| 164.308(a)(1)(ii)(D) | Information system activity review | R | Partial | CA-7: Repeated testing cycles each year | AU-6, AU-7 | DSS05, MEA01 |
| 164.308(a)(2) | Assigned security responsibility | R | Gap | - | PM-2, PM-29 | APO01, APO13 |
| 164.308(a)(3)(ii)(A) | Authorization and/or supervision | A | Partial | AC-2: Periodic access review testing; add/remove user access through AccessNow | PS-6 | APO07, DSS05 |
| 164.308(a)(3)(ii)(B) | Workforce clearance procedure | A | Partial | AC-6: Entitlement review within access and SoD testing | PS-3 | APO07, DSS05 |
| 164.308(a)(3)(ii)(C) | Termination procedures | A | Covered | PS-4: Access removal on termination via AccessNow (de-provisioning); AC-2: Periodic access review testing; add/remove user access through AccessNow | - | APO07, DSS05 |
| 164.308(a)(4)(ii)(A) | Isolating health care clearinghouse functions | R | Gap | - | AC-4, SC-7 | DSS05 |
| 164.308(a)(4)(ii)(B) | Access authorization | A | Partial | AC-2: Periodic access review testing; add/remove user access through AccessNow; AC-5: Segregation of duties testing (SOC 2: 30 systems; SOX: 30 tests); AC-6: Entitlement review within access and SoD testing | AC-3 | DSS05, DSS06 |
| 164.308(a)(4)(ii)(C) | Access establishment and modification | A | Partial | AC-2: Periodic access review testing; add/remove user access through AccessNow | PS-5 | DSS05, DSS06 |
| 164.308(a)(5)(ii)(A) | Security reminders | A | Gap | - | AT-2 | APO07, DSS05 |
| 164.308(a)(5)(ii)(B) | Protection from malicious software | A | Gap | - | SI-3, SI-8 | DSS05 |
| 164.308(a)(5)(ii)(C) | Log-in monitoring | A | Gap | - | AC-7, AU-6 | DSS05 |
| 164.308(a)(5)(ii)(D) | Password management | A | Covered | IA-5: Password authentication testing (641 controls) | - | DSS05 |
| 164.308(a)(6)(ii) | Response and reporting | R | Gap | - | IR-1, IR-4, IR-5, IR-6 | DSS02 |
| 164.308(a)(7)(ii)(A) | Data backup plan | R | Gap | - | CP-9 | DSS04 |
| 164.308(a)(7)(ii)(B) | Disaster recovery plan | R | Gap | - | CP-2, CP-10 | DSS04 |
| 164.308(a)(7)(ii)(C) | Emergency mode operation plan | R | Gap | - | CP-2, CP-12 | DSS04 |
| 164.308(a)(7)(ii)(D) | Testing and revision procedures | A | Gap | - | CP-4 | DSS04 |
| 164.308(a)(7)(ii)(E) | Applications and data criticality analysis | A | Gap | - | CP-2, RA-2 | DSS04, BAI09 |
| 164.308(a)(8) | Periodic technical and nontechnical evaluation | R | Partial | CA-2: SOX ITGC and SOC 2 control testing campaigns; CA-7: Repeated testing cycles each year | CA-8 | MEA01, MEA02, MEA03 |
| 164.308(b)(1) | Written contract or other arrangement | R | Gap | - | SA-9, PS-7, SR-3 | APO10 |
| 164.310(a)(2)(i) | Contingency operations | A | Gap | - | CP-2, PE-17 | DSS04 |
| 164.310(a)(2)(ii) | Facility security plan | A | Gap | - | PE-1, PE-3 | DSS05 |
| 164.310(a)(2)(iii) | Access control and validation procedures | A | Gap | - | PE-2, PE-3 | DSS05 |
| 164.310(a)(2)(iv) | Maintenance records | A | Gap | - | MA-2 | DSS01 |
| 164.310(b) | Workstation use | R | Gap | - | PL-4, AC-8 | DSS05 |
| 164.310(c) | Workstation security | R | Gap | - | PE-3, PE-5 | DSS05 |
| 164.310(d)(2)(i) | Disposal | R | Gap | - | MP-6 | DSS05 |
| 164.310(d)(2)(ii) | Media re-use | R | Gap | - | MP-6 | DSS05 |
| 164.310(d)(2)(iii) | Accountability | A | Partial | CM-8: ServiceNow application and server inventory used as system of record | MP-5 | BAI09, DSS05 |
| 164.310(d)(2)(iv) | Data backup and storage | A | Gap | - | CP-9 | DSS04 |
| 164.312(a)(2)(i) | Unique user identification | R | Partial | IA-2: MFA and authentication troubleshooting for online banking and remote deposit clients | IA-4 | DSS05 |
| 164.312(a)(2)(ii) | Emergency access procedure | R | Partial | AC-2: Periodic access review testing; add/remove user access through AccessNow | CP-2 | DSS04, DSS05 |
| 164.312(a)(2)(iii) | Automatic logoff | A | Gap | - | AC-11, AC-12 | DSS05 |
| 164.312(a)(2)(iv) | Encryption and decryption | A | Gap | - | SC-13, SC-28 | DSS05 |
| 164.312(b) | Audit controls | R | Gap | - | AU-2, AU-3, AU-12, AU-6 | DSS05, MEA01 |
| 164.312(c)(2) | Mechanism to authenticate ePHI | A | Covered | SI-7: File integrity monitoring testing (60 controls) | - | DSS05, DSS06 |
| 164.312(d) | Person or entity authentication | R | Partial | IA-2: MFA and authentication troubleshooting for online banking and remote deposit clients; IA-5: Password authentication testing (641 controls) | IA-8 | DSS05 |
| 164.312(e)(2)(i) | Integrity controls | A | Partial | SI-7: File integrity monitoring testing (60 controls) | SC-8 | DSS05 |
| 164.312(e)(2)(ii) | Encryption | A | Gap | - | SC-8, SC-13 | DSS05 |
| 164.316(a) | Policies and procedures | R | Gap | - | PL-1, AC-1, AU-1, IA-1, IR-1 | APO01, APO13 |
| 164.316(b)(2)(i) | Time limit (6-year retention) | R | Gap | - | SI-12, AU-11 | APO01, BAI09 |
| 164.316(b)(2)(ii) | Availability | R | Gap | - | PL-2, SI-12 | APO01 |
| 164.316(b)(2)(iii) | Updates | R | Gap | - | PL-1, CM-3, PL-2 | APO01, BAI06 |
