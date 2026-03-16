# Week 4 — Encryption

## Topics Covered
- Role of encryption in security strategy
- Symmetric vs Asymmetric encryption
- TLS and HTTPS
- Cryptanalysis basics
- Non-repudiation and authentication

---

## Key Concepts

### Encryption's Role
Encryption does NOT prevent access — it raises the cost of understanding data that has been stolen. It primarily addresses Confidentiality and Integrity, with limited impact on Availability (some argue it reduces availability by adding processing steps).

Encryption comes into play **after** an attacker has accessed a resource. Even if they extract data, they cannot read it without the key.

### Symmetric Encryption
- Same key used to encrypt and decrypt
- Fast and computationally efficient
- **Problem: key distribution** — how do you securely share the key in the first place without it being intercepted?
- Examples: AES (Advanced Encryption Standard), AES-256 is the current gold standard for data at rest

### Asymmetric Encryption
- Two mathematically related keys: **public key** (shareable) and **private key** (secret)
- Data encrypted with public key can only be decrypted with the private key
- Solves the key distribution problem — share public key freely, keep private key secret
- More computationally expensive than symmetric encryption
- Examples: RSA, Elliptic Curve Cryptography (ECC)

### TLS (Transport Layer Security)
In practice, TLS uses **both** asymmetric and symmetric encryption:
1. Asymmetric encryption to securely exchange a symmetric session key
2. Symmetric encryption for the actual data transfer (efficient)

This is what HTTPS uses — the padlock in your browser = TLS is active.

### Non-Repudiation and Authentication
Good encryption systems should provide:
- **Non-repudiation** — guarantee that what is received is what was originally sent (digital signatures)
- **Authentication** — guarantee that only the intended sender/recipient could have originated or read the data

With symmetric encryption, both parties have the same key — either could produce a fake message. Asymmetric encryption (digital signatures) solves this: only the private key holder can sign.

### Quantum Computing Threat
Current encryption relies on the computational difficulty of certain mathematical problems (factoring large numbers for RSA). Quantum computers could solve these problems far faster, potentially breaking current encryption. This is an active research area — post-quantum cryptography standards are being developed.

---

## Connection to Summative Assessment
In my coursework I specified AES-256 for data at rest and TLS for data in transit — directly applying the Week 4 concepts. I also noted that encryption addresses Confidentiality and Integrity (supporting GDPR Article 32) but does not replace access controls.

---

## Week 4 Summary
Encryption is a defence-in-depth tool — not a silver bullet. Symmetric encryption is efficient but has a key distribution problem. Asymmetric encryption solves distribution but is computationally expensive. In practice (TLS/HTTPS), both are combined. Digital signatures add non-repudiation. Quantum computing represents a future threat to current cryptographic assumptions.
