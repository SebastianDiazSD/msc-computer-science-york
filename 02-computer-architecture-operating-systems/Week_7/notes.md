# Week 7 — Security, Resilience, and Module Review

## Topics Covered
- Types of security threats (viruses, exploits, architectural attacks)
- Firewalls and virus checkers
- Encryption basics
- Buffer overflows and memory safety
- System resilience and fault tolerance
- UPS systems and redundancy
- Module review summary

---

## Key Concepts

### Types of Security Threats
- **Viruses** — malicious code that replicates and spreads, can damage data, encrypt files (ransomware), steal information, or use the host for remote attacks (DDoS)
- **Architectural exploits** — attacks that target hardware or system design flaws (e.g. Spectre, Meltdown — exploit CPU speculative execution)
- **Buffer overflows** — writing data beyond allocated memory boundaries to overwrite adjacent memory, potentially hijacking program execution

### Virus Checkers and Firewalls
- **Virus checkers** — scan files for known malicious signatures or suspicious behaviour patterns
- **Firewalls** — monitor and filter network traffic based on rules (block unauthorised ports, IP ranges, or protocols)

Limitation: firewalls and virus checkers reduce risk but cannot prevent all attacks. They raise the cost to attackers, not eliminate it.

### Buffer Overflows and Memory Safety
A buffer overflow occurs when a program writes more data than allocated memory can hold. The excess data overwrites adjacent memory, potentially:
- Corrupting data
- Overwriting return addresses to redirect execution to malicious code

Prevention: bounds checking, use of safe language constructs, memory-safe languages (Rust), compiler protections (stack canaries, ASLR).

Using `gdb` (GNU Debugger) allows tracing program execution to identify out-of-bounds memory access.

### Encryption in Security Context
Encryption does not prevent access — it raises the cost of understanding stolen data. Key concepts:
- **Symmetric encryption** — same key for encryption and decryption (fast, efficient, but key distribution problem)
- **Asymmetric encryption** — public/private key pair (solves key distribution, used in TLS/HTTPS)
- **TLS** — secures data in transit between client and server (HTTPS)
- **AES-256** — standard for encrypting data at rest

Encryption addresses Confidentiality and Integrity but has limited impact on Availability.

### System Resilience
Resilience means the system continues operating (or recovers quickly) despite failures. Key concepts:

**Reliability calculation:**
- System reliability = product of individual component reliabilities
- More components = higher chance that at least one fails
- Redundancy compensates by providing backup components

**Fault tolerance strategies:**
- **Redundant components** — duplicate critical parts (RAID for disks, UPS for power)
- **Failover** — automatic switch to backup system on failure
- **Graceful degradation** — system continues with reduced functionality rather than failing completely

**UPS (Uninterruptible Power Supply):**
- Provides battery backup during power outages
- Gives systems time to shut down safely or switch to generator
- Critical in data centres and safety-critical infrastructure

### Safety vs Resilience vs Reliability
- **Reliability** — probability that a system performs its function correctly over time
- **Resilience** — ability to recover from disruption
- **Safety** — system does not cause harm, even when it fails

All three are interdependent and must be designed in from the start.

---

## Module Review — Key Points Per Week

| Week | Core Topic | Key Takeaway |
|---|---|---|
| 1 | Hardware fundamentals | Von Neumann architecture, clock, ALU |
| 2 | Memory systems | Cache hierarchy bridges CPU-memory speed gap |
| 3 | Buses and storage | Bus protocols affect throughput; SSD replacing HDD |
| 4 | Operating systems | OS abstracts hardware; scheduling enables multitasking |
| 5 | Memory management + file systems | Virtual memory, paging, file organisation |
| 6 | Networks and cloud | OSI model, TCP/IP, distributed systems, virtualisation |
| 7 | Security and resilience | Threats, encryption, redundancy, fault tolerance |

---

## Personal Note
The security and resilience concepts from this week are directly applicable to the infrastructure tools I am building. When deploying FastAPI apps on Render.com, I need to think about: what happens when the server restarts? Is sensitive data (API keys) protected? Are requests logged for audit purposes? The module review makes clear that hardware knowledge, OS concepts, and network/security understanding are all interconnected — you cannot design a reliable system without understanding all three layers.

---

## Week 7 Summary
Security and resilience complete the picture of computer systems. Threats range from software viruses to hardware-level architectural exploits. Encryption, firewalls, and virus checkers reduce risk but not eliminate it. System resilience requires redundancy, fault tolerance, and safety design from the ground up — not added as an afterthought. This concludes the Computer Architecture and Operating Systems module.
