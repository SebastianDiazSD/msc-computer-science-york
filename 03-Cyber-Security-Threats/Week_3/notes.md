# Week 3 — Network Attacks and Penetration Testing Tools

## Topics Covered
- Network-based attacks after initial compromise
- Eavesdropping and packet capture
- Data alteration and spoofing
- Denial of Service (DoS and DDoS)
- SMTP security issues
- Penetration testing basics

---

## Key Concepts

### Post-Compromise Lateral Movement
Once an attacker compromises one system, they move from outside the organisation to inside it — where defences are typically weaker. From a compromised internal system, attackers can:
- Explore the internal network freely
- Access resources using credentials stored on the compromised machine
- Implant malware or cause data exfiltration
- Attack other systems on the same network

### Categories of Network Attacks

**Eavesdropping (Bugging / Wiretapping):**
- Attacker passively observes data flowing on the network
- In modern switched networks, the attacker can usually only observe traffic on the same subnet (switches prevent broadcast to all ports)
- Wireless networks are more vulnerable — any device within signal range can attempt to capture traffic

**Packet Capture:**
- Tools like Wireshark capture raw network packets
- Unencrypted data (HTTP, plain SMTP) is trivially readable
- This is why HTTPS and encrypted protocols are essential

**Data Alteration (Modification / Fabrication):**
- Attacker intercepts and modifies data in transit
- **MAC spoofing** — attacker fakes their hardware address to appear as a legitimate device
- **IP spoofing** — fakes IP address to hide identity or impersonate another host

**Denial of Service (DoS / DDoS):**
- DoS: single attacker overwhelms a service with requests, making it unavailable
- DDoS: Distributed DoS — multiple compromised machines (botnet) coordinate the attack
- Impact: loss of Availability (CIA triad)

### SMTP Security Issues
SMTP (email protocol) was designed without security in mind. Problems:
- No sender authentication by default — easy to spoof "from" addresses (basis of phishing emails)
- Modern extensions (SPF, DKIM, DMARC) partially address this but adoption is incomplete
- Difficult to retrofit security onto a protocol designed for an open, trusted network

### Penetration Testing
Ethical hackers use the same tools as attackers to test defences:
- **Port scanning** — identify which services are running and potentially vulnerable
- **Packet capture** — verify what data is exposed in unencrypted traffic
- **Vulnerability scanners** — automated identification of known weaknesses
- **DDoS simulation** — test service resilience under load

The starting point for everything is **understanding the network itself** and the humans who use it.

---

## Personal Note
When I deploy apps on Render.com, understanding network attack vectors helps me make better security decisions: use HTTPS only (TLS encrypts data in transit, preventing packet capture), avoid exposing unnecessary ports, and implement rate limiting on API endpoints to reduce DoS risk.

---

## Week 3 Summary
Once inside a network, attackers have multiple tools: passive eavesdropping, active data modification, identity spoofing, and service disruption. Many attacks exploit the fact that foundational internet protocols (SMTP, early HTTP) were designed for trusted networks and retrofitted with security imperfectly. Penetration testing uses the same tools to identify vulnerabilities before attackers do.
