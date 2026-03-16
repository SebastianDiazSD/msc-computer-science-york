# Week 2 — Human Factors and Social Engineering

## Topics Covered
- Humans as the weakest link in security systems
- Social engineering attacks
- Website trust and authentication
- Phishing, pharming, and credential theft
- Input sanitisation and interface restrictions

---

## Key Concepts

### Humans as a Security Vulnerability
People are generally poor at cyber security. Reasons:
- Intangible digital assets feel less valuable than physical ones
- Convenience consistently defeats caution (leaving laptops unlocked, reusing passwords, sharing credentials)
- Even trained users can be manipulated through psychological techniques

"Never underestimate the power of human stupidity" — the key lesson is that technical controls must be reinforced by organisational safeguards and interface design.

### Social Engineering
Attackers manipulate humans rather than exploiting technical vulnerabilities. Common techniques:
- **Phishing** — fraudulent emails impersonating trusted entities to steal credentials
- **Pharming** — redirecting users from legitimate websites to fake ones
- **Pretexting** — creating a fabricated scenario to manipulate the target
- **Appeals to greed or urgency** — "You have won a prize" or "Your account will be closed"

### Multi-Factor Authentication (MFA) Limitations
MFA raises the cost to attackers (they must also control the secondary channel) but does not eliminate social engineering risk. If an attacker gains access to an email account, they may use it to reset passwords on other systems via weak "Forgotten Password" mechanisms.

### Website Trust and Common Attacks
- **CMS vulnerabilities** — popular platforms like WordPress expose many sites to the same exploit
- **Third-party code** — embedding scripts from external sources (YouTube widgets, analytics) introduces supply chain risk — compromise of one library affects all sites using it
- **Session hijacking** — stealing session tokens to impersonate authenticated users

### Input Sanitisation
User inputs must never be trusted directly. Always validate and sanitise inputs before processing:
- Prevents SQL injection (malicious database queries embedded in form fields)
- Prevents XSS (Cross-Site Scripting — injecting malicious scripts into web pages)
- Use restricted input controls where possible (dropdowns vs free text)

---

## Personal Note
Input sanitisation is directly relevant to my FastAPI applications. Any endpoint that accepts user-provided data (project names, file uploads, observations) must validate inputs before passing them to the database or AI model. This is one of the first security improvements I will make when reviewing App 4 code.

---

## Week 2 Summary
Human error and social engineering are often more dangerous than technical exploits because they bypass technical controls entirely. Security design must account for human behaviour — both restricting what users can do and educating them about manipulation techniques. Interface design choices directly affect security posture.
