# Week 7 — Risk Assessment Completion and Module Review

## Topics Covered
- Completing the BS7799-3 risk assessment process
- Likelihood estimation scales
- Risk acceptance vs risk treatment
- Scenario-based risk assessment
- Asset-threat-vulnerability approach
- Module summary

---

## Key Concepts

### Estimating Likelihood (BS7799-3 Clause 6.4.3)
Use a minimum 5-point verbal scale that is unambiguous — avoid vague terms like "frequent":

| Level | Example Definition |
|---|---|
| 1 | Once a year |
| 2 | Once a quarter |
| 3 | Once a month |
| 4 | Weekly |
| 5 | Daily |

The scale will need refinement over time as the organisation learns more about its specific threat environment. Starting with any consistent scale is better than paralysis.

### Risk Estimation Matrix
Combine Likelihood × Impact to produce risk ratings:

| | Low Impact | Medium Impact | High Impact | Very High Impact |
|---|---|---|---|---|
| **High Likelihood** | Medium | High | Critical | Critical |
| **Medium Likelihood** | Low | Medium | High | Critical |
| **Low Likelihood** | Low | Low | Medium | High |

Risks rated HIGH or CRITICAL require documented mitigation plans.

### Risk Acceptance
Not all risks can or should be eliminated. Two categories:
- **Accept** — risk is too rare or too expensive to address; document the decision at board level
- **Treat** — implement controls to reduce likelihood, impact, or both

Important: acceptance decisions must be signed off at board level because directors may be personally liable for adverse outcomes.

### Risk Treatment Options
- **Avoid** — stop the activity that creates the risk
- **Reduce** — implement controls to lower likelihood or impact
- **Transfer** — insurance, contractual obligations to third parties
- **Accept** — document and monitor

### Two Approaches to Risk Assessment

**Asset-Threat-Vulnerability approach (BS7799-3 Clauses 7.2.1 and 7.2.3):**
- Start with assets (what needs protecting)
- Identify threats to each asset
- Identify vulnerabilities those threats could exploit
- Estimate risk for each combination

**Scenario approach (BS7799-3 Clause 7.2.2):**
- Start with a business event (e.g. power cut at headquarters)
- Trace all business elements impacted by that event
- Assess combined risk across the cascade

Both approaches are closely related and complementary.

### Perceptual Bias in Risk Assessment
Risk estimates based on data and process are often challenged by participants who feel the numbers "don't seem right." Experience shows this is usually perceptual bias — influenced by recent experiences or individual risk tolerance — rather than actual errors in the methodology. The correct response: complete the assessment with current data, then review and refine.

---

## Summative Assessment Summary
**Title:** Risk Management Plan for a Digital Health Services Provider  
**Framework:** NIST RMF (selected over ISO 27001 for stronger operational integration and traceability of controls)  
**System:** Cloud-based SaaS cognitive assessment platform processing special category health data  

**Key Findings:**
- Confidentiality risk: HIGH (cognitive health data = special category under GDPR Article 9)
- Integrity risk: HIGH (falsified assessment results could affect employment and treatment decisions)
- Availability risk: MODERATE-HIGH (downtime breaks contracts and damages client trust)

**Two Critical Threats Analysed:**
1. Unauthorized access / data breaches — phishing, credential stuffing, weak session management
2. Third-party / supply chain compromise — cloud misconfiguration, malicious libraries, CI/CD pipeline attacks

**Controls Selected (NIST SP 800-53):**
- MFA (phishing-resistant) for privileged accounts
- AES-256 at rest, TLS in transit
- SIEM for centralised logging and anomaly detection
- Formal incident response plan with GDPR notification timelines
- Vendor risk management programme

---

## Module Review — Key Themes

| Week | Theme | Core Idea |
|---|---|---|
| 1 | Risk fundamentals | Risk = Likelihood × Impact; understand org first |
| 2 | Human factors | People are often the weakest link; social engineering bypasses technical controls |
| 3 | Network attacks | Post-compromise lateral movement; packet capture; DDoS |
| 4 | Encryption | Raises cost of data theft; symmetric + asymmetric combined in TLS |
| 5 | Databases + cloud | SQL injection; inference attacks; shared responsibility model |
| 6 | GDPR + compliance | Seven principles; Articles 32 and 35; cross-border transfers |
| 7 | Risk completion | Likelihood scales; risk acceptance; scenario vs asset-based approaches |

---

## Week 7 Summary
The final week completes the risk assessment loop — from identifying and categorising risks (Weeks 1-6) to estimating, accepting, and treating them (Week 7). The BS7799-3 framework provides a structured, repeatable process. The summative assessment applied these concepts to a realistic digital health scenario, demonstrating how NIST RMF controls map to GDPR compliance requirements.
