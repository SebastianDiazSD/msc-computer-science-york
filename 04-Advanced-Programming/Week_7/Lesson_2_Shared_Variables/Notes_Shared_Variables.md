# Lesson 2: Shared Variables

**Source:** 7.5 Lesson 2 + 7.5.1 More about shared variables + Atomicity.docx + Semaphores.docx + Monitors.docx

---

## Overview

The first approach to concurrent programming uses **shared variables** — processes share the same memory and communicate by reading from and writing to common variables. While conceptually simple, this raises fundamental problems that require careful design to avoid.

By the end of this lesson you should be able to:
- Articulate the problem with atomicity and the need for critical sections and mutual exclusion
- Understand semaphores and how they protect critical sections
- Understand monitors and condition variables for higher-level synchronisation

---

## 1. Atomicity

### The Problem

High-level languages like Python and Java sit at the top of a translation stack — they are compiled or interpreted into lower-level machine instructions before execution. A single high-level statement can expand into **multiple machine-level instructions**.

**Example: `C = C + 1`**  
At machine level, this is (at minimum) three operations:
1. Read value of C from memory into a register
2. Increment the register by 1
3. Write the register value back to memory address C

In sequential programming this is invisible. In concurrent programming, another process can **interleave** between these three steps, reading or writing C while another process is mid-update.

### The Multiple Update Problem (from Atomicity.docx)

Two processes P and Q, both running `C = C + 1` for 20 iterations each. Expected result: 40.

**What actually happens (race condition example):**
```
Q reads C = 0
P reads C = 0  (before Q has written back)
P increments: C = 1, writes back
Q increments: C = 1, writes back  (overwrites P's update)
Net result: only 1 added, not 2
```

This means the final result can be **anywhere between 20 and 40** and is non-deterministic — different on every run. It can even fall below 20 if processes read a stale value, complete their calculation, and then overwrite a more recent value.

This is called the **race condition** — one process races ahead with no regard for the state other processes left the shared resource in.

> "This is known as the race condition, where one process has raced ahead to complete with no regard for other processes."
> — Atomicity transcript

### Critical Sections

A **critical section** is a block of code that must execute atomically — with no interference from other processes.

Rules for critical sections:
- Keep them **small and specific** — large critical sections create bottlenecks and reduce concurrency benefit
- They must be accessed under **mutual exclusion** — only one process in the critical section at a time

---

## 2. Semaphores

### Concept

A semaphore is a **signalling primitive** that controls access to a critical section. Introduced by Dijkstra in 1968. The original notation used **P** (from Dutch *Proberen*, "to test") for `wait` and **V** (from *Verhogen*, "to increment") for `signal`.

A semaphore is an encapsulated integer with two atomic operations:

| Operation | Behaviour |
|-----------|-----------|
| `wait` (P) | If semaphore > 0: decrement and allow entry. If semaphore = 0: **block** the calling process |
| `signal` (V) | Increment semaphore by 1; unblock a waiting process if any |

### Binary vs Counting Semaphore

| Type | Values | Use |
|------|--------|-----|
| **Binary semaphore (mutex)** | 0 or 1 only | Mutual exclusion for a single critical section |
| **Counting semaphore** | Any non-negative integer | Controlling access to a pool of N identical resources |

**Mutex specifics:** A mutex (mutual exclusion semaphore) is a binary semaphore where only the thread that locked it can unlock it. A general semaphore can be signalled by any process.

### How Mutual Exclusion Works (from Semaphores.docx)

```
initialise semaphore 'gate' to 1

Process P:
  wait(gate)       ← acquires access (gate → 0, blocks others)
  [critical section]
  signal(gate)     ← releases access (gate → 1, unblocks waiting processes)
```

From the transcript:  
> "The order in which the processes access the variable C does not matter, what matters is that they can only do this one at a time, or atomically."

### Limitations of Semaphores

- No guarantee of **fairness** — a process can theoretically be permanently blocked if unlucky (starvation)
- Using multiple semaphores across multiple processes can lead to **deadlock**
- The critical section protected by `wait/signal` is not itself atomic — errors can still occur in complex programs
- Semaphores are low-level; easy to misuse (e.g., forgetting to call `signal`)

---

## 3. Monitors

### Why Monitors?

Semaphores are primitives — they require the programmer to correctly place every `wait` and `signal`. Monitors are a **higher-level construct** that guarantees mutual exclusion automatically.

A monitor encapsulates:
- The shared data it protects
- The procedures that operate on that data
- The mutual exclusion mechanism (a **lock**)

> "A monitor is a higher level construct that guarantees mutual exclusion and conditional critical sections. Once a process enters a monitor, what happens inside is protected from interference until it completes."
> — Lesson 7.5.1

Monitors were introduced by C.A.R. Hoare in 1974. Java and Python both use monitors internally — in Java, every object can act as a monitor (`synchronized`). Python's `threading.Lock`, `threading.Condition`, and `threading.RLock` all implement monitor semantics.

### Structure of a Monitor (Pascal-FC example from Monitors.docx)

```
monitor update
  var C: integer;
  
  procedure inc(var V: integer);
  begin
    V := V + 1
  end;
  
  export inc;
end;
```

Processes call `update.inc(C)` — the monitor handles mutual exclusion. No explicit `wait/signal` required around the call.

### Condition Variables

A monitor lock alone only handles mutual exclusion. Sometimes a process needs to wait for a **specific condition** (e.g., "wait until the buffer is not empty"). Condition variables provide this:

| Operation | Behaviour |
|-----------|-----------|
| `delay` / `wait` | Block the process and release the monitor lock; place process in the condition's queue |
| `resume` / `notify` | Unblock one waiting process from the condition's queue |

Condition variable queues operate **FIFO** (first in, first out) in Pascal-FC.

---

## 4. Classic Problems: Bounded Buffer and Readers/Writers

### The Bounded Buffer (Producer/Consumer) Problem

A shared buffer of fixed capacity N. Two types of processes:
- **Producers**: add items to the buffer; must block if buffer is **full**
- **Consumers**: remove items from the buffer; must block if buffer is **empty**

**Monitor solution (from Monitors.docx):**
```
monitor buffer_manager
  conditions: slots_available, items_available

  procedure place(item):
    if buffer is full:
      delay(slots_available)    ← block producer
    add item to buffer
    resume(items_available)     ← unblock a waiting consumer

  procedure take():
    if buffer is empty:
      delay(items_available)    ← block consumer
    remove item from buffer
    resume(slots_available)     ← unblock a waiting producer
```

**Key rule:** `resume` must be the **last statement** in each block to avoid interfering with the active process.

### The Readers and Writers Problem (Task 5)

**What it is:** A shared resource (e.g., a file or database) that multiple concurrent processes want to access. Readers only read; writers read and modify. The constraint:
- Multiple readers can access simultaneously (reading doesn't corrupt data)
- A writer needs **exclusive access** (no readers or other writers)

**Pseudocode solution:**
```
Readers:
  lock(readers_mutex)
    readers_count += 1
    if readers_count == 1:
      lock(resource)    ← first reader locks out writers
  unlock(readers_mutex)
  
  [read resource]
  
  lock(readers_mutex)
    readers_count -= 1
    if readers_count == 0:
      unlock(resource)  ← last reader releases resource
  unlock(readers_mutex)

Writers:
  lock(resource)
  [write resource]
  unlock(resource)
```

**Limitations:**  
- **Writer starvation**: if readers arrive continuously, a writer may never get access (the resource is never free)
- The "second readers/writers problem" reverses priority (writers preferred) but then causes **reader starvation**
- Neither solution is fully satisfactory — there is always a fairness trade-off

---

## Task Responses

**Week 7 Task 2 — Controlling access to shared variables:**

Real-world analogies for access control mechanisms:
- *Preventing access:* A toilet lock — the engaged sign shows the resource is in use; no one else can enter
- *Allowing access:* A traffic light — red means block, green means proceed
- *Fair access:* A ticket system at a deli counter — each customer gets a number ensuring FIFO fairness

Programming constructs:
- Preventing: mutex lock, `threading.Lock()`
- Allowing: semaphore, `threading.Semaphore()`
- Fair access: condition variable with FIFO queue, `threading.Condition()`

**Week 7 Task 3 — P and V notation:**

Dijkstra used **P** (from Dutch *Proberen* = "to test/try") for `wait` and **V** (from *Verhogen* = "to increment") for `signal`. P is `wait`; V is `signal`.

**Mutex vs semaphore:**
- A semaphore is a general signalling primitive; any process can call `wait` or `signal`
- A mutex adds **ownership** — only the thread that acquired the mutex can release it
- Mutex examples: `threading.Lock()` in Python; `synchronized` blocks in Java; file locks in OS

**Week 7 Task 4 — Python and Java concurrency models:**

*Python:* Uses `threading.Lock()` (mutex/binary semaphore), `threading.Semaphore()` (counting semaphore), and `threading.Condition()` (monitor with condition variables). The GIL itself acts as a coarse-grained lock on the interpreter.

```python
import threading

sem = threading.Semaphore(1)  # binary semaphore
counter = 0

def increment():
    global counter
    for _ in range(20):
        sem.acquire()   # wait (P)
        counter += 1
        sem.release()   # signal (V)
```

*Java:* Every object has an intrinsic lock. `synchronized` methods/blocks implement monitor semantics. `java.util.concurrent.Semaphore` provides explicit semaphore access.

```java
synchronized void increment() {  // monitor — only one thread enters at a time
    counter++;
}
```

**Week 7 Task 5 — Readers and Writers summary (150 words):**

The Readers and Writers problem models a shared resource (e.g., a database record) accessed by concurrent readers and writers. Multiple readers may access simultaneously since reading does not modify state; however, a writer needs exclusive access to prevent data corruption.

The first solution (readers-preference) uses a readers counter protected by a mutex. The first reader acquires the resource lock, excluding all writers; the last reader releases it. Writers simply acquire the resource lock directly.

The limitation is writer starvation: if readers arrive in a continuous stream, the resource lock is never released and writers block indefinitely.

The second solution (writers-preference) gives writers priority — new readers block if a writer is waiting. This eliminates writer starvation but can cause reader starvation instead.

Neither solution is universally satisfactory. Fair solutions exist using FIFO queues for all waiting processes, but these add complexity and reduce throughput.

---

## Summary for Revision

| Concept | Definition |
|---------|-----------|
| Atomicity | A sequence of operations that executes as a single indivisible unit |
| Critical section | Code that must execute under mutual exclusion |
| Mutual exclusion | Only one process in the critical section at a time |
| Semaphore | Signalling primitive: `wait` (P) blocks if 0; `signal` (V) increments and unblocks |
| Mutex | Binary semaphore with ownership — only the acquirer can release |
| Monitor | Higher-level construct guaranteeing mutual exclusion on a code block |
| Condition variable | Queue of blocked processes waiting on a specific condition |
| Bounded buffer | Producer/consumer problem with a finite shared buffer |
| Readers/Writers | Multiple simultaneous readers; exclusive single writer |
