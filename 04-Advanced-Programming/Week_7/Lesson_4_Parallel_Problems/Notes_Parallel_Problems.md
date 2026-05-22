# Lesson 4: Parallel Problems

**Source:** 7.8 Lesson 4

---

## Overview

Concurrent programs face a set of well-documented failure modes. These are not hypothetical — they occur in production systems. Each has a specific set of conditions that must be met for the problem to be diagnosed, and each has a specific undesirable outcome.

Understanding these problems allows concurrent designers to:
- Reason about the correctness of their designs before they fail
- Add targeted constraints and checks to prevent them
- Recognise that solving one problem often introduces another

> "Often the solution of one will result in the generation of another. For instance, a solution to deadlock often results in livelock. Sometimes an additional problem is generated alongside, such as deadlock often generating resource starvation as well."
> — Lesson 7.8

---

## The Four Problems

### 1. Deadlock

**Conditions (Coffman, 1971 — all four must hold simultaneously):**
1. **Mutual exclusion** — at least one resource must be held in a non-sharable mode
2. **Hold and wait** — a process holds at least one resource and is waiting to acquire additional resources held by other processes
3. **No preemption** — resources cannot be forcibly taken from a process; they must be voluntarily released
4. **Circular wait** — a circular chain of processes exists, each holding a resource needed by the next

**End result:** All involved processes are permanently blocked. None can proceed. The program halts.

**Example:**
```
Process A holds Resource 1, waiting for Resource 2
Process B holds Resource 2, waiting for Resource 1
→ Neither can proceed. Deadlock.
```

**Prevention strategies:**
- Break circular wait: enforce a global ordering on resource acquisition (always acquire lower-numbered resource first)
- Break hold-and-wait: require processes to request all resources at once
- Allow preemption: forcibly reclaim resources from blocked processes
- Break mutual exclusion where possible (not always feasible)

---

### 2. Livelock

**Conditions:**
- Two or more processes repeatedly change state in response to each other
- Neither is blocked (both are "active" from the OS perspective)
- Neither is making progress

**End result:** The program runs indefinitely but accomplishes nothing. CPU is consumed. No thread blocks — they just keep spinning.

**Example:**
```
Process A tries resource, sees B, steps back
Process B tries resource, sees A, steps back
Both step back at the same time, then try again simultaneously
→ Cycles forever
```

Real-world analogy: two people trying to pass each other in a corridor — both step the same way to let the other pass, indefinitely.

**Key distinction from deadlock:** In deadlock, processes block. In livelock, processes are technically running but not progressing.

**Prevention:** Introduce randomised back-off delays (like Ethernet's CSMA/CD collision detection) so the two processes don't mirror each other's behaviour.

---

### 3. Race Condition

**Conditions:**
- Two or more processes access a shared resource concurrently
- At least one access is a write
- The result depends on the non-deterministic interleaving of instructions

**End result:** Inconsistent, non-repeatable output. The program may produce correct results sometimes and incorrect results other times, making bugs very hard to reproduce.

**Example (from the Atomicity video):**
```
P reads C = 16
Q reads C = 16  (before P writes back)
P calculates 17, writes back
Q calculates 17, writes back  (overwrites P — P's update is lost)
Result: 17 instead of 18
```

**Prevention:** Protect critical sections with semaphores, locks, or monitors; ensure all shared reads/writes are atomic.

---

### 4. Starvation

**Conditions:**
- A process is perpetually denied access to a resource it needs to make progress
- Other processes continue to receive service
- The starved process may not be blocked — it is simply never selected

**End result:** One or more processes never complete. Liveness property violated.

**Example:** A low-priority thread in a scheduling system — if high-priority threads always arrive, the low-priority thread is indefinitely deferred.

**Note:** Deadlock often causes starvation as a side effect (deadlocked processes can never access the resources they need). Starvation can also occur without deadlock (e.g., the readers-preference solution to Readers/Writers starves writers).

**Prevention:** Use fair scheduling (FIFO queues), priority ageing (increase priority of waiting processes over time), or set explicit time limits.

---

## Relationships Between Problems

```
Deadlock ─────────────────────────────→ Starvation (deadlocked processes starve)
   ↓
Solution to deadlock (e.g., back-off)  →  Livelock (processes keep backing off)
   
Race Condition → corrupt data → may cause effective deadlock or starvation
```

These problems interact. A complete concurrent design must consider all four simultaneously.

---

## The Dining Philosophers Problem

Introduced by Dijkstra (1965). Five philosophers sit at a circular table. Between each pair of philosophers is a single fork. Each philosopher alternates between thinking and eating. To eat, a philosopher needs **both** the fork on their left and the fork on their right.

**Why it's a classic:**

| Problem | How it manifests |
|---------|-----------------|
| **Deadlock** | All philosophers pick up their left fork simultaneously. Each waits for their right fork. No one can eat. The program halts. |
| **Livelock** | All philosophers pick up their left fork, fail to get the right fork, put the left fork down simultaneously, try again — in sync, indefinitely. |
| **Starvation** | One philosopher is repeatedly beaten to the forks by neighbours. They never eat, even though others do. |
| **Race condition** | Two philosophers race to pick up the shared fork between them — without proper synchronisation, both may believe they have exclusive access. |

**Standard solution (resource hierarchy):**
- Number the forks 0–4
- Each philosopher always picks up the lower-numbered fork first
- This breaks the circular wait condition
- Philosopher 4 picks up fork 0 (not fork 4) first — they compete with Philosopher 0 for fork 0, eliminating the cycle

---

## Summary for Revision

| Problem | State of processes | Making progress? | Key condition |
|---------|-------------------|-----------------|---------------|
| Deadlock | Blocked | No | Circular wait for resources |
| Livelock | Running | No | Mirroring each other's retreat |
| Race condition | Running | Incorrectly | Unprotected concurrent access |
| Starvation | Running or blocked | Some are, one isn't | Perpetual resource denial |

**Key reference:** Sebesta, R. W. (2016) *Concepts of Programming Languages* — §10.3
