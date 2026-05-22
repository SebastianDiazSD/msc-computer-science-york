# Activity 3 — Parallel Problems (Discussion Board)

**Activity label:** Activity 3 - Parallel problems

---

## Exercise 1 — Livelock, Deadlock, Race Conditions, Starvation

---

### 1. Livelock

**Conditions for livelock:**
- Two or more processes are actively responding to each other's state
- Neither is blocked (the OS considers them "running")
- Each detects a conflict and backs off — but both back off in the same way, at the same time
- This creates a cycle of state changes with no net progress

**End result:**  
The program keeps running, consuming CPU, but no thread makes progress towards completion. Unlike deadlock, the system appears active. This makes livelock harder to detect — profiling or timeouts are typically needed to diagnose it.

**Real-world example:**  
Two people walking towards each other in a narrow corridor. Both step right to let the other pass. Both then step left. They mirror each other indefinitely.

**Programming example:**  
```
Thread A: tries to acquire Lock 1 → sees Lock 2 is held → releases Lock 1 → retries
Thread B: tries to acquire Lock 2 → sees Lock 1 is held → releases Lock 2 → retries
→ Both retry simultaneously, repeat forever
```

---

### 2. Deadlock

**Conditions for deadlock (Coffman, 1971 — all four must hold):**
1. **Mutual exclusion** — a resource can only be held by one process at a time
2. **Hold and wait** — a process holds at least one resource while waiting for another
3. **No preemption** — resources cannot be forcibly taken from a process
4. **Circular wait** — a circular chain of processes exists: A waits for B, B waits for C, C waits for A

**End result:**  
All involved processes are permanently blocked. No process can release its resources because it's waiting for another resource. The program halts — this is a permanent state unless externally interrupted (timeout, watchdog, OS intervention).

**Key distinction from livelock:** In deadlock, processes are truly blocked. In livelock, they are technically running.

---

### 3. Race Conditions

**Conditions:**
- Two or more processes access a shared resource concurrently
- At least one access is a write (read-read is safe)
- There is no synchronisation controlling the order of access
- The outcome depends on the non-deterministic interleaving of low-level instructions

**End result:**  
The program produces incorrect, inconsistent results. The outcome changes between runs depending on scheduling, timing, and hardware. Data may be silently corrupted — the worst kind of bug because it doesn't crash the program, it just produces wrong answers.

**Classic example (from Atomicity video):**  
Two threads both executing `C = C + 1`. At machine level this is three steps: READ, INCREMENT, WRITE. If two threads interleave between READ and WRITE, both can read the same stale value, and one thread's update overwrites the other's — two increments produce a net change of only 1.

---

### 4. Starvation

**Conditions:**
- A process repeatedly fails to gain access to a resource it needs
- Other processes continue to receive service
- The deprived process may not be blocked — it simply keeps losing to higher-priority or faster processes

**End result:**  
The starved process never completes, or takes an arbitrarily long time. A liveness property is violated — the process will never make progress. The rest of the system may appear to work correctly.

**Example:**  
In the readers-preference solution to the Readers/Writers problem, if readers arrive in a continuous stream, the resource lock is never fully released, and any waiting writer starves indefinitely.

---

## Exercise 2 — Dining Philosophers and the Four Problems

The Dining Philosophers: five philosophers at a circular table, one fork between each adjacent pair (five forks total). To eat, a philosopher needs both adjacent forks. They alternate between thinking and eating.

---

### Deadlock in Dining Philosophers

**How it happens:**  
All five philosophers pick up their **left fork** simultaneously. Each philosopher now holds one fork and is waiting for the fork on their right — which is held by the philosopher to their right. This forms a circular wait:
```
Phil 0 holds fork 0, wants fork 1 (held by Phil 1)
Phil 1 holds fork 1, wants fork 2 (held by Phil 2)
...
Phil 4 holds fork 4, wants fork 0 (held by Phil 0)
```
All four Coffman conditions are met: mutual exclusion (forks are non-shareable), hold-and-wait (each holds one, waits for another), no preemption (no one forcibly takes a fork), circular wait (the ring). The system permanently halts.

---

### Livelock in Dining Philosophers

**How it happens:**  
Each philosopher implements a "polite" retry — if they can't pick up the right fork, they put down the left fork and wait before trying again. If all five do this simultaneously, they:
1. All pick up left forks
2. All fail to get right forks
3. All put down left forks
4. All wait the same duration
5. All try again simultaneously → same result

This repeats indefinitely. No philosopher is blocked by the OS (they keep looping) but no one eats.

---

### Starvation in Dining Philosophers

**How it happens:**  
Even without deadlock or livelock, one philosopher may be unlucky enough that every time they try to pick up forks, both neighbours are eating (or just about to eat). If scheduling is unfair — or if the two neighbours collude (alternately eating) — the middle philosopher is perpetually denied access to both forks.

The other four philosophers may be dining successfully throughout. The starved philosopher's liveness property is violated.

**Standard fix:** resource hierarchy solution — always pick up the lower-numbered fork first. This breaks circular wait (deadlock prevention) without introducing livelock, and with fair scheduling, starvation is also avoided.
