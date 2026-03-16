# Week 1 — Terminology, Threats, Risks, and Risk Modelling

## Topics Covered
- Definitions: Computer Security, Information Security, Cyber Security
- CIA Triad
- Threats vs Risks
- Risk = Likelihood × Impact
- Risk modelling and organisational context (BS7799-3)

---

## Key Concepts

### Core Definitions
- **Computer Security** — protecting computer systems and the information they process
- **Information Security** — protecting information itself, regardless of format (digital or physical)
- **Cyber Security** — combines computer and information security, extending to communication systems. The "cyber" prefix implies digital focus but non-digital forms still matter

These are often confused even in industry — the key distinction is scope: computer security focuses on systems, information security on data, cyber security on the full digital ecosystem.

### CIA Triad
The three fundamental properties any security system must protect:
- **Confidentiality** — information is accessible only to authorised parties
- **Integrity** — information is accurate and has not been tampered with
- **Availability** — information and systems are accessible when needed

A threat is anything that could break one or more of these properties.

### Threats vs Risks
These are NOT the same thing:
- **Threat** — something that might happen and would break the CIA triad. No concept of likelihood or impact embedded.
- **Risk** — a threat for which likelihood and impact have been estimated

**Risk Model:**
```
Risk = Likelihood × Impact
```
This formula is the foundation of practical security management. It allows prioritisation: a high-likelihood, low-impact threat may require less attention than a low-likelihood, very-high-impact threat.

### Why Risk Modelling Matters
Security resources are always limited. Starting with a full list of all possible threats is counterproductive — most will not apply to your specific organisation. The correct approach:
1. Understand the organisation and what it is trying to protect (assets)
2. Identify threats relevant to those assets
3. Estimate likelihood and impact for each
4. Prioritise response accordingly

**Analogy from the module:** sharks are a threat. But if your operations never involve the sea, the shark threat has zero impact on your risk model. Knowing this lets you safely ignore it and focus on what actually matters.

### BS7799-3 Framework
The British Standard for information security risk management. Provides a structured process for any organisation, of any size, to:
- Identify what matters to the organisation
- Understand consequences and severity of breaches
- Guide effort toward the most relevant threats

Used as the primary framework in the Cyber Security Threats module alongside NIST RMF.

---

## Connection to Summative Assessment
In my coursework (Risk Management Plan for a Digital Health Services Provider), I applied the NIST RMF rather than ISO 27001 because NIST provides more detailed, traceable controls — particularly useful for demonstrating GDPR Article 32 compliance. The CIA triad framing from Week 1 was the foundation for the entire risk categorisation in that report.

---

## Week 1 Summary
Cyber security is about protecting the CIA triad. The distinction between threats (what could happen) and risks (what is likely to happen and how bad it would be) is foundational to all practical security work. Risk = Likelihood × Impact is the core formula. Understanding your organisation first — before listing threats — is the correct approach.
