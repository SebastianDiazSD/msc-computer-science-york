# Activity 2 – Legal, Ethical and Moral Analysis

**Chosen case studies:** Bias in Algorithms + Driverless Cars

---

## Exercise 1 – General Questions

### Q1: What is the difference between a law and a professional code of conduct?

A **law** is a formally enacted rule by a legislative authority (parliament, congress) that is **universally binding** within a jurisdiction and enforced by an external authority (police, courts). Violation carries legal consequences — criminal prosecution, fines, or civil liability. Laws set the minimum acceptable standard of behaviour in a society.

A **professional code of conduct** is a set of standards established by a professional body (e.g., BCS, ACM, IEEE) that members voluntarily agree to uphold upon joining. It goes beyond legal minimum compliance — it addresses ethical behaviour, integrity, honesty, and professional responsibility. Enforcement is internal: sanctions include removal from the professional register or public censure, not imprisonment. Codes apply only to members of the relevant body.

**Key distinction:** Laws set the floor; codes of conduct set a higher standard. A professional could act entirely within the law but still violate their professional code — for example, a developer who builds a technically legal but deliberately deceptive dark-pattern interface.

---

### Q2: How are new laws developed?

New laws typically arise when existing legislation fails to address a new situation — often triggered by a public incident, a new technology, or political pressure.

**Triggering factors:**
- A high-profile incident (e.g., the VW emissions scandal → new EU emissions enforcement; the Uber fatality → AV regulation consultations)
- A new technology that existing law does not cover (e.g., the internet → Computer Misuse Act 1990; data processing → GDPR 2018)
- International pressure or treaty obligations
- Lobbying by industry, civil society, or academic research

**UK legislative process:**
1. Government consultation (Green Paper)
2. Policy proposals (White Paper)
3. Bill introduced to Parliament
4. Three readings and committee scrutiny in the House of Commons
5. Same process in the House of Lords
6. Royal Assent → becomes an Act of Parliament

**Example:** The Computer Misuse Act 1990 was directly prompted by *R v Gold and Schifreen* [1988] AC 1063, where existing law proved inadequate to prosecute hackers who accessed BT's network. The case led directly to legislative action.

---

### Q3: Two ethical standards relevant to computing

**1. ACM Code of Ethics and Professional Conduct (2018)**
Principle 1.2: "Avoid harm." Computing professionals must weigh the risks their systems pose to health, safety, security, and wellbeing. This requires both pre-deployment testing and ongoing monitoring.

Reference: ACM (2018). *ACM Code of Ethics and Professional Conduct*. Available at: https://www.acm.org/code-of-ethics

**2. IEEE Code of Ethics (2020)**
Principle 1: Members commit to "hold paramount the safety, health, and welfare of the public." This places a direct obligation on engineers to refuse to implement systems they know are harmful, regardless of employer pressure.

Reference: IEEE (2020). *IEEE Code of Ethics*. Available at: https://www.ieee.org/about/corporate/governance/p7-8.html

---

### Q4: Conflict between an ethical standard and moral implementation

**Example: National security surveillance**

The ACM and BCS codes both require computing professionals to respect user privacy and act in the public interest. However, an engineer working for a national intelligence agency under UK law (Investigatory Powers Act 2016 / RIPA 2000) may be legally required — and may personally believe it is morally justified — to develop tools that conduct bulk surveillance of private communications without individual consent.

From the institutional moral framework of national security ("we protect the public by monitoring threats"), building the tool is the right thing to do. From the ACM ethical standard (privacy as a fundamental right), it is a violation. The law not only permits the breach but may legally compel it.

This is not a hypothetical conflict — Edward Snowden's revelations about GCHQ/NSA programmes illustrated exactly this tension. Engineers who designed and implemented those systems may have personally agreed with the mission while violating the spirit of their professional codes.

---

## Exercise 2 – Applied Case Study Analysis

---

### Case Study A: Bias in Algorithms

#### Legal Issue
**Issue:** Automated decision-making systems producing discriminatory outcomes in hiring, credit scoring, and criminal sentencing.

**Applicable legislation:** General Data Protection Regulation (EU) 2016/679, **Article 22** — *Automated individual decision-making, including profiling.*

This article gives EU citizens the right not to be subject to a decision based solely on automated processing that produces "legal or similarly significant effects." Organisations must provide meaningful information about the logic involved, and individuals may request human review.

**Whose legal system:** European Union (applicable to any organisation processing EU citizen data regardless of location).

**Citation:** Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data (GDPR), Article 22. *Official Journal of the European Union*, L 119/1.

---

#### Ethical Problem
**Problem:** The deployment of biased algorithmic systems without transparency, consent, or accountability.

**Whose standpoint:** This is an issue from the standpoint of **affected communities** — particularly racialised minorities and women who have been systematically disadvantaged by algorithmic tools — and from the perspective of the **ACM computing professional community**, which holds that computing systems should not harm individuals or groups.

The COMPAS recidivism tool (Angwin et al., 2016) assigned higher-risk scores to Black defendants at double the rate of false positives compared to white defendants, with no transparency to the individuals affected. Defendants had no ability to understand, challenge, or appeal the score.

**Citation:** Angwin, J., Larson, J., Mattu, S. and Kirchner, L. (2016). 'Machine Bias', *ProPublica*, 23 May. Available at: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

---

#### Moral Perspective and Suggested Solution
From a **consequentialist moral perspective**, the harm produced by biased systems — wrongful imprisonment, loss of employment, denial of credit — outweighs any efficiency gains to the organisations deploying them.

My suggested solution has three components:
1. **Mandatory pre-deployment bias audits** by independent third parties before any algorithm is used in high-stakes decisions (criminal justice, employment, credit, healthcare).
2. **Transparency requirements**: individuals subject to automated decisions must receive a plain-language explanation of the key factors and the right to human review, as GDPR Article 22 already requires but which is poorly enforced.
3. **Ongoing monitoring**: bias metrics (false positive rates across demographic groups) should be published regularly by deployers — similar to how pharmaceutical companies publish adverse event reports.

---

### Case Study B: Driverless Cars

#### Legal Issue
**Issue:** Liability when an autonomous vehicle causes injury or death.

**Applicable legislation:** **Automated and Electric Vehicles Act 2018 (UK)**, Section 2 — *Liability of insurers where accident caused by automated vehicle.*

This Act establishes that the insurer of an automated vehicle is directly liable for injuries or deaths caused by the vehicle driving itself, resolving the gap in the existing Road Traffic Act 1988 which assumed a human driver was always responsible.

**Whose legal system:** England and Wales (UK).

**Citation:** Automated and Electric Vehicles Act 2018 (c. 18), Section 2. Available at: https://www.legislation.gov.uk/ukpga/2018/18/contents/enacted

---

#### Ethical Problem
**Problem:** The encoding of life-prioritisation decisions into autonomous vehicle algorithms without democratic consent or transparency.

**Whose standpoint:** This is an ethical issue from the standpoint of **the general public** and from the perspective of **engineering professional ethics** (IEEE/ACM), which require transparency in systems with safety implications.

When an AV must choose between two unavoidable harm outcomes (e.g., swerving into a pedestrian or maintaining course at the risk of the passenger), the algorithm encodes a moral priority. These decisions are currently made privately by software engineers and corporate product teams with no public consultation.

**Citation:** Awad, E. et al. (2018). 'The Moral Machine experiment', *Nature*, 563(7729), pp. 59–64. doi:10.1038/s41586-018-0637-6

---

#### Moral Perspective and Suggested Solution
From a **deontological moral perspective**, individuals have a right to know when decisions about their safety are being made by an algorithm, and to have input into the values encoded in that algorithm. No single engineer's or company's value system should be silently imposed on the public.

My suggested solution:
1. **Mandatory publication** of the decision logic used in collision avoidance systems, reviewed by an independent safety authority (similar to aviation accident investigation boards).
2. **International regulatory convergence**: the EU, UK, and US should establish a joint framework for AV ethics standards so that vehicles do not operate under different moral rules in different jurisdictions.
3. **Participatory design mechanisms**: before large-scale deployment, public consultations (like the MIT Moral Machine experiment at scale) should inform the ethical parameters of AV decision-making, ensuring democratic legitimacy.
