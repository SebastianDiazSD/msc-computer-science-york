# Week 4 — Operating Systems: Concepts and Workload Management

## Topics Covered
- Operating system structure (kernel, drivers, services)
- System calls and exceptional control flow
- Process and thread management
- Scheduling algorithms
- Concurrency and thread safety
- Multicore and hyperthreading

---

## Key Concepts

### What is an Operating System?
An OS is the **abstraction layer** between hardware and software applications. It makes diverse, complex hardware appear uniform and simple to applications running above it.

OS layers (bottom to top):
```
Hardware
    ↓
Firmware / BIOS
    ↓
Kernel (core OS — manages CPU, memory, devices)
    ↓
Drivers / Services / Utilities
    ↓
User Applications
```

### Key OS Functions
- **Process management** — create, schedule, terminate processes
- **Memory management** — allocate and protect memory for each process
- **File system management** — organise and retrieve data from storage
- **Device management** — provide uniform interface to hardware via drivers
- **Security** — enforce access control and process isolation

### System Calls
Programs communicate with the OS kernel via **system calls** — a controlled interface that allows applications to request services (open a file, allocate memory, send data over network) without direct hardware access. This enforces security and stability.

### Exceptional Control Flow
Events that interrupt normal program execution:
- **Interrupts** — hardware signals (e.g. keyboard press, timer tick)
- **Traps** — intentional software interrupts (system calls)
- **Faults** — recoverable errors (e.g. page fault — missing memory page)
- **Aborts** — unrecoverable errors (hardware failure)

### Process and Thread Management
- **Process** — an independent program in execution, with its own memory space and Process ID (PID)
- **Thread** — a lightweight execution unit within a process, sharing memory with other threads

**Thread models:**
- User-level threads (managed by application)
- Kernel-level threads (managed by OS)

### Scheduling Algorithms
The OS shares CPU time across multiple processes using scheduling:
- **FIFO** — first in, first out (simple, but can cause long waits)
- **Round Robin** — each process gets a fixed time slice (fair)
- **Priority scheduling** — higher-priority processes run first
- **Preemptive scheduling** — OS can interrupt a running process to switch to another

### Concurrency and Thread Safety
When multiple threads access shared data simultaneously, **race conditions** can occur — unpredictable results depending on execution order. Solutions:
- **Mutex (mutual exclusion)** — only one thread accesses a resource at a time
- **Semaphores** — control access to a limited number of resources
- **Reentrant functions** — safe to call from multiple threads simultaneously

### Multicore and Hyperthreading
- **Multicore** — multiple independent CPU cores on one chip, true parallelism
- **Hyperthreading / SMT (Simultaneous Multithreading)** — one physical core appears as two logical cores, interleaving execution to hide latency
- Note: Intel removed hyperthreading from desktop chips in 2024 — trade-offs between throughput and security (Spectre/Meltdown vulnerabilities exploited thread-sharing)

### POSIX Threads (pthreads)
Standard C interface for thread management in Unix/Linux systems:
- `pthread_create()` — create thread
- `pthread_join()` — wait for thread to finish (joinable threads)
- `pthread_detach()` — release resources immediately on termination (detached threads)

---

## Personal Note
Process scheduling is directly relevant to how I think about API performance in my FastAPI applications. When multiple clients call the `/generate-report` endpoint simultaneously, the OS schedules those threads. Understanding scheduling helps explain why async programming (non-blocking I/O) improves throughput — it allows the OS to switch to other tasks while waiting for API responses, rather than blocking a thread.

---

## Week 4 Summary
The operating system is the critical abstraction layer that makes hardware usable. It manages CPU time through scheduling, enforces process isolation for security and stability, and provides system calls as a controlled interface for applications. Modern multi-core and multithreaded architectures introduce concurrency challenges that require careful programming to avoid race conditions and data corruption.
