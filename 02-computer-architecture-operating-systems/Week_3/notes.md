# Week 3 — System Components: Buses, Storage, and Peripherals

## Topics Covered
- Bus systems (data, address, control buses)
- Bus standards (PCI, USB, I2C, CAN)
- Storage technologies (HDD vs SSD, RAID)
- Peripherals and interfaces
- Networking basics (wired and wireless)

---

## Key Concepts

### Bus Systems
A **bus** is a communication pathway that transfers data between components (CPU, memory, I/O devices). Three types of signals travel on buses:
- **Data bus** — carries actual data
- **Address bus** — specifies memory or I/O location
- **Control bus** — carries control signals (read/write, interrupt requests)

**System bus vs dedicated bus:**
- System bus: shared by all components (simpler, but creates bottlenecks)
- Dedicated point-to-point: direct connection between specific components (faster, used in modern architectures like PCIe)

**Performance factors:**
- Bus width (number of parallel wires) — wider = more data per cycle
- Bus frequency — higher = more cycles per second
- Concurrency and buffering techniques reduce bottlenecks

### Bus Standards
| Standard | Use case |
|---|---|
| PCI/PCIe | Graphics cards, high-speed expansion cards |
| USB | Universal peripheral connection |
| I2C | Short-distance embedded communication (sensors) |
| CAN bus | Industrial and automotive embedded systems |

**CAN bus is particularly relevant to railway systems** — it is used in train control networks for reliable, real-time communication between embedded controllers.

### Storage Technologies

**HDD (Hard Disk Drive):**
- Mechanical read/write head on spinning magnetic platter
- Performance limited by physical mechanics (seek time, rotational latency)
- Still used for bulk/archival storage due to cost per GB

**SSD (Solid State Drive):**
- No moving parts — uses flash memory (NAND)
- Much faster access times, lower latency
- Higher cost per GB but improving rapidly
- Issue: write endurance (flash cells wear out after finite write cycles)

**RAID (Redundant Array of Independent Disks):**
| Level | Strategy | Use |
|---|---|---|
| RAID 0 | Striping (speed, no redundancy) | Performance |
| RAID 1 | Mirroring (full redundancy) | Safety |
| RAID 5 | Striping + parity | Balance of speed and redundancy |
| RAID 6 | Double parity | High reliability |

### Peripherals and Interfaces
Input devices (keyboard, mouse, biometric scanners, cameras) and output devices (monitors, printers) connect through standardised interfaces. Modern peripherals increasingly use wireless connectivity (Bluetooth, Wi-Fi).

Key concept: **human-computer interaction design affects system performance** — poorly designed interfaces increase cognitive load and reduce efficiency, relevant to dashboard design in construction tools.

### Networking Basics
- **Wired (Ethernet)** — reliable, high bandwidth, used in fixed infrastructure
- **Wireless (Wi-Fi, Bluetooth)** — convenient but susceptible to interference
- Network communication introduces overhead from protocols — important to consider in real-time data systems

---

## Personal Note
CAN bus is something I have encountered indirectly in railway systems — train control units use field buses for sensor and actuator communication. The reliability requirements for industrial buses (fault tolerance, deterministic timing) mirror the requirements I have seen in railway safety systems. Understanding this at the architecture level helps connect the field experience to the computer science theory.

---

## Week 3 Summary
Week 3 completed the hardware picture: buses connect components and their design directly affects system throughput. Storage technologies have shifted from mechanical HDD to SSD, with RAID providing redundancy strategies. Peripherals and networks extend the computer system outward to interact with the physical world — a boundary increasingly relevant in infrastructure and IoT contexts.
