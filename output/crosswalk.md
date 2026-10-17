# FFIEC → COBIT 2019 crosswalk

Primary mappings in **bold**. Relationship = how the FFIEC expectation's scope compares to the COBIT element.

## Management

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| MGT-01 | IT governance and strategy | **EDM01** Ensured Governance Framework Setting and Maintenance | primary | intersects | Board-level governance framework and oversight of I&T |
|  |  | **APO02** Managed Strategy | primary | intersects | IT strategic plan aligned to enterprise strategy |
|  |  | EDM02 Ensured Benefits Delivery | supporting | intersects | Board evaluates value delivered by I&T investments |
| MGT-02 | IT risk management | **APO12** Managed Risk | primary | equivalent | Full IT risk lifecycle: collect data, analyze, maintain profile, respond |
|  |  | **EDM03** Ensured Risk Optimization | primary | intersects | Board sets risk appetite and oversees risk optimization |
| MGT-03 | Policies and roles | **APO01** Managed I&T Management Framework | primary | superset_of | FFIEC expectation spans policies and roles; APO01 covers the I&T management framework including both |
|  |  | EDM01 Ensured Governance Framework Setting and Maintenance | supporting | intersects | Board direction on governance structures |
| MGT-04 | IT resources | **APO07** Managed Human Resources | primary | intersects | Staffing levels and skills |
|  |  | **APO06** Managed Budget and Costs | primary | intersects | IT budget and cost management |
|  |  | EDM04 Ensured Resource Optimization | supporting | intersects | Board oversight of resource optimization |
| MGT-05 | Reporting to the board | **MEA01** Managed Performance and Conformance Monitoring | primary | intersects | Performance and conformance monitoring and reporting |
|  |  | EDM05 Ensured Stakeholder Engagement | supporting | intersects | Stakeholder (board) reporting and transparency |
| MGT-06 | Legal and regulatory compliance | **MEA03** Managed Compliance With External Requirements | primary | equivalent | Identify and comply with external legal and regulatory requirements |
|  |  | APO13 Managed Security | supporting | intersects | GLBA safeguards are implemented through the security management system |

## Information Security

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| IS-01 | Security governance and culture | **APO13** Managed Security | primary | intersects | Information security management system and program |
|  |  | EDM01 Ensured Governance Framework Setting and Maintenance | supporting | intersects | Board approval and accountability for the program |
|  |  | APO07 Managed Human Resources | supporting | intersects | Security culture and accountability of personnel |
| IS-02 | Risk identification | **APO12.01** Collect data | primary | subset_of | Threat and vulnerability identification is the security slice of collecting risk data |
|  |  | DSS05.07 Manage vulnerabilities and monitor the infrastructure for security-related events | supporting | intersects | Vulnerability identification on infrastructure |
| IS-03 | Asset inventory and classification | **BAI09** Managed Assets | primary | intersects | Asset inventory and lifecycle |
|  |  | **APO14** Managed Data | primary | intersects | Data classification by sensitivity |
|  |  | BAI10 Managed Configuration | supporting | intersects | Configuration items and their relationships |
| IS-04 | Risk measurement | **APO12.02** Analyze risk | primary | subset_of | Security risk analysis within enterprise risk analysis |
|  |  | APO12.03 Maintain a risk profile | supporting | intersects | Prioritized risk profile |
| IS-05 | Security policies and standards | **APO13** Managed Security | primary | intersects | Security policies are part of the ISMS |
|  |  | APO01 Managed I&T Management Framework | supporting | intersects | Policy framework and policy lifecycle |
| IS-06 | User access controls | **DSS05.04** Manage user identity and logical access | primary | equivalent | User identity and logical access management |
|  |  | DSS05.05 Manage physical access to I&T assets | supporting | intersects | Physical access to I&T assets |
| IS-07 | Network controls | **DSS05.02** Manage network and connectivity security | primary | equivalent | Network and connectivity security |
| IS-08 | Malware and endpoint protection | **DSS05.01** Protect against malicious software | primary | intersects | Malicious software protection |
|  |  | **DSS05.03** Manage endpoint security | primary | intersects | Endpoint security and hardening |
| IS-09 | Change management | **BAI06** Managed IT Changes | primary | equivalent | IT change management: authorize, assess, approve, implement |
|  |  | BAI10 Managed Configuration | supporting | intersects | Configuration baselines updated on change |
| IS-10 | Control of information | **DSS05.06** Manage sensitive documents and output devices | primary | subset_of | Sensitive documents and output; COBIT practice narrower than FFIEC data-protection scope |
|  |  | APO14 Managed Data | supporting | intersects | Data management including retention and disposal |
|  |  | DSS06 Managed Business Process Controls | supporting | intersects | Business process controls over information handling |
| IS-11 | Application security | **BAI03** Managed Solutions Identification and Build | primary | intersects | Security requirements built into solution design and build |
|  |  | BAI07 Managed IT Change Acceptance and Transitioning | supporting | intersects | Security testing during acceptance |
| IS-12 | Service provider security oversight | **APO10.04** Manage vendor risk | primary | intersects | Vendor risk including security requirements |
|  |  | **APO10.05** Monitor vendor performance and compliance | primary | intersects | Monitor vendor control performance |
| IS-13 | Threat intelligence | **APO12.01** Collect data | primary | intersects | Collect threat data relevant to the enterprise |
|  |  | DSS05.07 Manage vulnerabilities and monitor the infrastructure for security-related events | supporting | intersects | Use threat information in monitoring |
| IS-14 | Security monitoring | **DSS05.07** Manage vulnerabilities and monitor the infrastructure for security-related events | primary | equivalent | Monitor infrastructure for security-related events |
|  |  | DSS01 Managed Operations | supporting | intersects | Operational monitoring |
| IS-15 | Incident response | **DSS02** Managed Service Requests and Incidents | primary | superset_of | FFIEC incident response includes customer and regulatory notification that DSS02 does not specify |
|  |  | DSS03 Managed Problems | supporting | intersects | Root-cause analysis |
|  |  | MEA03 Managed Compliance With External Requirements | supporting | intersects | Regulatory notification obligations |
| IS-16 | Assurance and testing | **DSS05.07** Manage vulnerabilities and monitor the infrastructure for security-related events | primary | intersects | Vulnerability assessment |
|  |  | **MEA04** Managed Assurance | primary | intersects | Independent assurance including penetration testing |
|  |  | MEA02 Managed System of Internal Control | supporting | intersects | Control self-assessment |
| IS-17 | Security awareness training | **APO07** Managed Human Resources | primary | intersects | Training and skills of personnel |
|  |  | BAI08 Managed Knowledge | supporting | intersects | Knowledge sharing and awareness |
| IS-18 | Program effectiveness reporting | **MEA01** Managed Performance and Conformance Monitoring | primary | intersects | Performance measurement and reporting |
|  |  | APO13 Managed Security | supporting | intersects | ISMS effectiveness reviews |

## Business Continuity Management

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| BCM-01 | BCM governance | **DSS04.01** Define the business continuity policy, objectives and scope | primary | intersects | Continuity policy, objectives and scope |
|  |  | EDM03 Ensured Risk Optimization | supporting | intersects | Board oversight of resilience risk |
| BCM-02 | Business impact analysis | **DSS04.02** Maintain business resilience | primary | intersects | Business resilience including impact analysis |
| BCM-03 | Continuity and resilience strategies | **DSS04.03** Develop and implement a business continuity response | primary | intersects | Continuity response and recovery strategy |
|  |  | **DSS04.07** Manage backup arrangements | primary | equivalent | Backup arrangements |
|  |  | BAI04 Managed Availability and Capacity | supporting | intersects | Availability and redundancy design |
| BCM-04 | Exercises and testing | **DSS04.04** Exercise, test and review the business continuity plan (BCP) and disaster response plan (DRP) | primary | equivalent | Exercise, test and review BCP and DRP |
|  |  | DSS04.06 Conduct continuity plan training | supporting | intersects | Continuity training |
| BCM-05 | Plan maintenance and improvement | **DSS04.05** Review, maintain and improve the continuity plans | primary | equivalent | Review, maintain and improve continuity plans |
|  |  | DSS04.08 Conduct post-resumption review | supporting | intersects | Post-resumption review |
| BCM-06 | Third-party resilience | **APO10.04** Manage vendor risk | primary | intersects | Vendor risk including resilience |
|  |  | DSS04.03 Develop and implement a business continuity response | supporting | intersects | Continuity strategy covers third-party dependencies |

## Architecture, Infrastructure, and Operations

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| AIO-01 | Enterprise architecture | **APO03** Managed Enterprise Architecture | primary | equivalent | Enterprise architecture |
| AIO-02 | IT operations | **DSS01** Managed Operations | primary | equivalent | Operations management and operational procedures |
| AIO-03 | Capacity and availability | **BAI04** Managed Availability and Capacity | primary | equivalent | Availability and capacity |
| AIO-04 | Configuration and asset lifecycle | **BAI10** Managed Configuration | primary | intersects | Configuration baselines and control |
|  |  | **BAI09** Managed Assets | primary | intersects | Asset lifecycle including end of life |
| AIO-05 | Problem management | **DSS03** Managed Problems | primary | equivalent | Problem management and root cause |

## Development, Acquisition, and Maintenance

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| DAM-01 | Project and SDLC management | **BAI11** Managed Projects | primary | intersects | Project management |
|  |  | BAI01 Managed Programs | supporting | intersects | Program management |
|  |  | BAI03 Managed Solutions Identification and Build | supporting | intersects | Development life cycle |
| DAM-02 | Requirements and acquisition | **BAI02** Managed Requirements Definition | primary | equivalent | Requirements definition |
|  |  | BAI03 Managed Solutions Identification and Build | supporting | intersects | Solution identification and acquisition |
| DAM-03 | Testing and acceptance | **BAI07** Managed IT Change Acceptance and Transitioning | primary | equivalent | Change acceptance and transition including testing |

## Audit

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| AUD-01 | Independent IT audit | **MEA04** Managed Assurance | primary | intersects | Independent assurance |
|  |  | MEA02 Managed System of Internal Control | supporting | intersects | System of internal control |
| AUD-02 | Issue tracking and remediation | **MEA02** Managed System of Internal Control | primary | intersects | Control deficiency remediation tracking |
|  |  | MEA04 Managed Assurance | supporting | intersects | Assurance follow-up |

## Outsourcing Technology Services

| FFIEC | Topic | COBIT 2019 | Strength | Relationship | Rationale |
| --- | --- | --- | --- | --- | --- |
| OTS-01 | Due diligence and selection | **APO10.02** Select vendors | primary | intersects | Vendor selection |
|  |  | APO10.01 Identify and evaluate vendor relationships and contracts | supporting | intersects | Identify and evaluate vendor relationships |
| OTS-02 | Contracts and service levels | **APO09** Managed Service Agreements | primary | intersects | Service level agreements |
|  |  | **APO10.03** Manage vendor relationships and contracts | primary | intersects | Vendor contract management |
| OTS-03 | Ongoing monitoring | **APO10.05** Monitor vendor performance and compliance | primary | equivalent | Monitor vendor performance and compliance |
|  |  | APO10.04 Manage vendor risk | supporting | intersects | Ongoing vendor risk |
