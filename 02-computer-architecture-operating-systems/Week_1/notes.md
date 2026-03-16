# Week 1 — Hardware Fundamentals and Computer Architecture Basics

## Topics Covered
- Von Neumann Architecture
- Basic hardware and software components
- Clock signals and synchronisation
- History of computing (vacuum tubes → transistors → integrated circuits)
- Types of computing systems (general-purpose, embedded, supercomputers)

---

## Key Concepts

### Von Neumann Architecture
The foundational model behind almost all modern computers. Three essential components:
- **Control Unit (CU)** — directs operations of the processor
- **Arithmetic Logic Unit (ALU)** — performs arithmetic and logical operations
- **Memory** — stores both data and instructions

All components are connected via a **system bus**. The key limitation is the **Von Neumann Bottleneck**: data and instructions share the same bus, creating a throughput constraint between CPU and memory.

### Units of Measurement
Computer systems are described using standard prefixes:
- **Kilo** (10³), **Mega** (10⁶), **Giga** (10⁹), **Tera** (10¹²)
- These apply to storage (bytes), frequency (Hz), and data transfer rates (bits/s)

### Clock Signals
The clock is the heartbeat of the system. It generates a regular sequence of electrical pulses (clock cycles) that synchronise all components. Key properties:
- **Clock cycle** — one complete pulse (rising edge + falling edge)
- **Clock period** — time for one cycle (T = 1/f)
- **Frequency (f)** — cycles per second, measured in Hz (GHz in modern CPUs)

Higher frequency = more operations per second, but also more heat and power consumption.

### Logic Gates and Truth Tables
Logic gates (AND, OR, NOT, NAND, NOR, XOR) are the fundamental building blocks of digital circuits. They operate on binary inputs (0 and 1).
Truth tables map every possible input combination to its output — essential for designing and verifying digital logic.

### History of Computing — Key Milestones
| Generation | Technology | Example |
|---|---|---|
| 1st | Vacuum tubes | ENIAC (1945) |
| 2nd | Transistors | IBM 7090 (1959) |
| 3rd | Integrated circuits | IBM System/360 (1964) |
| 4th | Microprocessors | Intel 4004 (1971) |

Each transition brought improvements in speed, reliability, and power efficiency.

### Types of Computing Systems
- **General-purpose computers** — handle a wide range of tasks (desktops, laptops)
- **Mobile computers** — smartphones, tablets (ARM-based processors dominate)
- **Supercomputers** — extreme parallel processing for scientific computation (e.g. El Capitan)
- **Embedded systems** — dedicated hardware for specific tasks (industrial, automotive, IoT)
- **Wearables and implantables** — emerging category with strict power constraints

### ARM Architecture
ARM (Advanced RISC Machines) dominates embedded and mobile computing due to RISC (Reduced Instruction Set Computing) principles — simpler instructions, lower power consumption, high efficiency. Relevant to IoT and edge computing in infrastructure monitoring.

---

## Personal Note
The Von Neumann Bottleneck is directly relevant to my work in railway data systems — when processing large sensor datasets in real time, the speed at which data moves between memory and CPU is often the limiting factor, not the processing logic itself. Understanding this bottleneck clarifies why caching and data structure choices matter so much in performance-sensitive applications.

---

## Quiz — Key Questions
**Q: Name the three essential components of Von Neumann architecture.**
A: Control Unit, Arithmetic Logic Unit (ALU), Memory

**Q: What is the primary purpose of the clock in a computer system?**
A: To synchronise operations by generating a regular sequence of electrical pulses

**Q: What does a Bus do in a computer system?**
A: Provides a communication pathway to exchange data between components (CPU, memory, I/O)

**Q: What is the function of logic gates and truth tables?**
A: Logic gates perform basic logical operations on binary inputs; truth tables show the output for all possible input combinations
