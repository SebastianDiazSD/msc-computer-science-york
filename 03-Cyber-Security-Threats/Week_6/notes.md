# Week 6 — Privacy, GDPR, and Regulatory Compliance

## Topics Covered
- Privacy legislation approaches (EU vs US vs others)
- GDPR — key principles and obligations
- Data Protection Impact Assessment (DPIA)
- Cross-border data transfers
- Sarbanes-Oxley and sector-specific regulations
- Legal privilege considerations

---

## Key Concepts

### Privacy vs Security
Security is technically focused — protect systems from attack. Privacy is legally and ethically focused — protect individuals' rights over their own data.

Privacy is harder to manage than security because:
- Legal frameworks vary by jurisdiction (GDPR in EU, CCPA in California, no comprehensive federal law in US)
- Some countries treat disclosed data as freely usable by businesses; others require explicit consent
- Emotional and political dimensions make consensus difficult

### GDPR — Seven Key Principles (Article 5)
1. **Lawfulness, fairness and transparency** — processing must have a legal basis and be clear to data subjects
2. **Purpose limitation** — data collected for one purpose cannot be freely used for others
3. **Data minimisation** — collect only what is necessary
4. **Accuracy** — keep data up to date
5. **Storage limitation** — do not keep data longer than needed
6. **Integrity and confidentiality** — implement appropriate security measures
7. **Accountability** — be able to demonstrate compliance

Only principle 6 is explicitly about security — but all others affect how security must be implemented.

### GDPR Legal Bases (Article 6)
Processing personal data requires one of:
- Explicit consent
- Contract necessity
- Legal obligation
- Vital interests
- Public task
- Legitimate interests

For **special category data** (health, biometrics, ethnicity, political opinions) — Article 9 requires an additional condition on top of Article 6.

### Article 32 — Security Requirements
Organisations must implement "appropriate technical and organisational measures" based on risk level. Includes:
- Encryption of personal data
- Ongoing confidentiality, integrity, availability, and resilience of systems
- Ability to restore data after incidents
- Regular testing of security measures

Failure to have appropriate measures can result in fines **even without a breach occurring**.

### DPIA (Data Protection Impact Assessment) — Article 35
Required when processing is likely to result in high risk to individuals:
- Large-scale processing of sensitive data (health, biometrics)
- Systematic monitoring of public areas
- Automated decision-making with significant effects

A DPIA must evaluate risks, identify mitigation measures, and be documented. Cybersecurity and data protection governance must be linked.

### Cross-Border Data Transfers
GDPR has extraterritorial reach — personal data of EU residents cannot be freely transferred to countries without adequate protection. Transfer mechanisms:
- **Adequacy decision** — EU recognises the destination country's laws as adequate
- **Standard Contractual Clauses (SCCs)** — contractual obligations between sender and recipient
- **Binding Corporate Rules** — for transfers within multinational organisations

Encryption reduces exposure but does not replace legal transfer mechanisms.

### Other Regulations
- **Sarbanes-Oxley (USA)** — requires communications to be preserved for 2+ years; creates challenges for IT and security teams managing data retention
- **Computer Misuse Act (UK)** — criminalises unauthorised access to computer systems
- **Legal privilege** — communications between lawyers and clients are protected; IT and security teams must ensure these are properly identified and secured

---

## Connection to Summative Assessment
GDPR was the primary regulatory framework in my coursework. I applied Articles 6, 9, 32, and 35 specifically to the digital health platform. The DPIA requirement was identified as mandatory due to large-scale processing of cognitive and behavioural health data. I also addressed cross-border cloud data transfer compliance and key management as partial (but insufficient alone) mitigations.

---

## Week 6 Summary
Legal and regulatory compliance adds a non-technical layer to security requirements. GDPR is the most comprehensive and extraterritorial framework — its seven principles and specific articles create concrete technical and organisational obligations. DPIAs are mandatory for high-risk processing. Compliance is not optional — fines apply even without a breach if measures are inadequate.
