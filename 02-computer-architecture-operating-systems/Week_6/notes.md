# Week 6 — Networks, Distributed Systems, and Cloud Computing

## Topics Covered
- OSI reference model and TCP/IP
- Network security fundamentals
- IP addressing and domain names
- Sockets and network services
- Distributed systems
- Cloud computing and virtualisation

---

## Key Concepts

### OSI Reference Model
The OSI (Open Systems Interconnection) model provides a 7-layer framework for understanding network communication. Each layer abstracts complexity from the layer above it.

| Layer | Name | Function | Example |
|---|---|---|---|
| 7 | Application | User-facing services | HTTP, FTP, SMTP |
| 6 | Presentation | Data formatting/encryption | TLS, JPEG encoding |
| 5 | Session | Connection management | Session tokens |
| 4 | Transport | End-to-end delivery | TCP, UDP |
| 3 | Network | Routing between networks | IP |
| 2 | Data Link | Node-to-node within network | Ethernet, MAC |
| 1 | Physical | Bit transmission | Cables, radio signals |

### TCP/IP Model
The practical implementation used on the internet. Fewer layers than OSI — maps roughly to Application, Transport, Internet, and Network Access.

**TCP vs UDP:**
- **TCP** — reliable, ordered delivery, connection-oriented (used for web, email)
- **UDP** — fast, no delivery guarantee, connectionless (used for video streaming, DNS)

### Network Structures
- **Nodes** — devices on a network
- **Segments** — portions of a network
- **Bridges** — connect two network segments, filter traffic
- **Switches** — intelligent bridges (forward data only to the correct port)
- **Routers** — forward packets between different networks
- **Firewalls** — enforce security rules on network traffic

### IP Addressing and DNS
Every device on a network has a unique **IP address**:
- IPv4: 32-bit (e.g. 192.168.1.1)
- IPv6: 128-bit (e.g. 2001:0db8::1) — designed to address IPv4 exhaustion

**DNS (Domain Name System)** maps human-readable domain names (ground2tech.com) to IP addresses. Without DNS, users would need to type IP addresses directly.

### Sockets
A **socket** is a software interface for network communication — identified by IP address + port number. Applications use sockets to send and receive data across networks. FastAPI uses sockets internally when handling HTTP requests.

### Common Network Services
| Service | Protocol | Port | Use |
|---|---|---|---|
| Web | HTTP/HTTPS | 80/443 | Web browsing |
| Email | SMTP | 25 | Sending email |
| File transfer | FTP | 21 | File transfer |
| Secure shell | SSH | 22 | Remote terminal |

### Distributed Systems
A distributed system consists of multiple networked computers working together to perform tasks. Benefits:
- **Scalability** — add more nodes to handle more load
- **Reliability** — failure of one node does not bring down the system
- **Performance** — parallel processing across nodes

### Cloud Computing
Cloud computing provides on-demand access to computing resources via the internet. Models:
- **IaaS** (Infrastructure as a Service) — rent virtual machines and storage (AWS EC2)
- **PaaS** (Platform as a Service) — rent a platform for development (Heroku, Render.com)
- **SaaS** (Software as a Service) — use software hosted by provider (Streamlit Cloud)

**Shared responsibility model:** the cloud provider secures the infrastructure; the customer is responsible for configuration, access management, and data.

### Virtualisation
Virtualisation allows multiple independent operating systems to run on a single physical server:
- **Native virtualisation** — hypervisor runs directly on hardware (VMware ESXi)
- **Hosted virtualisation** — hypervisor runs on top of an OS (VirtualBox)
- **Containers** — lightweight virtualisation sharing the OS kernel (Docker)

---

## Personal Note
I use cloud services directly in my Ground2Tech work — Render.com (PaaS) for FastAPI backends, Streamlit Cloud (SaaS-like) for dashboards. Understanding the OSI model helps me debug network issues in deployed apps: when a frontend cannot reach a backend, I can trace the problem layer by layer — is it a DNS issue (layer 7/application), a routing issue (layer 3), or a firewall rule blocking the port (layer 4)?

---

## Week 6 Summary
Networks extend computer systems beyond individual machines. The OSI and TCP/IP models provide layered frameworks for understanding how data travels across networks. Cloud computing and virtualisation represent the modern evolution of distributed systems — moving infrastructure management from physical hardware to software-defined, scalable services.
