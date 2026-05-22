# Lesson 1: Concurrency v Parallelism

**Source:** 7.3 Lesson 1 + Introduction_to_concurrency.pdf (video transcript)

---

## Key Distinction

| Term | Definition |
|------|-----------|
| **Sequential** | One instruction at a time; total ordering |
| **Concurrent** | Designed to potentially run in parallel; partial ordering |
| **Parallel** | Actually executing simultaneously on multiple processors/cores |

The critical point: **concurrent programming is potential parallelism**. A concurrent program *can* run sequentially (on a single core) or in parallel (on multiple cores). A purely sequential program can never run in parallel.

> "Concurrent programs are an abstract view of parallelism. They provide an abstract setting in which to study parallelism without getting bogged down in the implementation details."
> — Introduction to Concurrency transcript

---

## Why the World Demands Concurrency

The real world is a parallel place. Transport systems, the human body (breathing and walking don't take turns), shopping — all involve many processes happening simultaneously. Computing, by contrast, has historically forced these naturally parallel systems into sequential models. This was largely a hardware limitation (single CPU). With multi-core machines and distributed systems, we now have the opportunity — and the need — to exploit concurrent design.

---

## Concurrency Requires a Change in Thinking

Adding concurrency isn't just about speed. The challenges arise at the **interaction points** — where parallel processes share data or need to synchronise. These points are where concurrent programming has its difficulties.

**Two core problems in concurrency:**
1. **Synchronisation** — bringing processes to an agreed point in time; making one process wait until others are ready
2. **Communication** — passing data between processes

---

## Sequential vs Concurrent Ordering

In a sequential program: **total ordering** — X happens before Y before Z, always.

In a concurrent program: **partial ordering** — some things must happen in order (data must be read before it can be processed), but many things have no required ordering relative to each other.

**Example (Pascal-FC):**  
```
co-begin
  X := 1;   { these two can run in any order }
  Y := 2;
co-end
Z := X + Y; { this must happen after both }
```

If processes P and Q run in parallel, the legal execution sequences are:
- All of P, then all of Q
- All of Q, then all of P
- P and Q truly simultaneously
- Interleaving: part of P, part of Q, rest of P, rest of Q

The **interleaving** case is where bugs emerge.

---

## The Maze Analogy

A single person solving a maze uses brute force sequentially — one path at a time. A team large enough to cover all paths tests multiple routes simultaneously — this is concurrent/parallel execution. Concurrency forks at each junction and is only needed at specific decision points; the initial single corridor before the first junction required no concurrency.

**Key insight:** Concurrency is not always needed throughout a program. It is most valuable at specific points, and decomposing problems correctly is part of concurrent design.

---

## Correctness in Concurrent Programs

Sequential correctness is straightforward: same input → same output, always.  
Concurrent correctness is harder because **non-determinism is expected and required**.

Two correctness properties:

| Property | Definition | Example |
|----------|-----------|---------|
| **Safety** | Must *always* hold true | "The user always has access to and visual perception of the mouse cursor" |
| **Liveness** | Must *eventually* become true | "If the mouse passes over a button it will change shape" |

A liveness property doesn't need an immediate response — but it cannot be permanently ignored.

---

## Two Approaches to Concurrent Programming

| Approach | Use Case | Python Support |
|----------|---------|----------------|
| **Shared variables** | Localised systems; understanding concurrency theory | `threading` module |
| **Message passing** | Distributed systems; large parallel applications | `multiprocessing`, `queue`, `asyncio` |

Not all languages support both. Python provides APIs for both, but the module focuses on shared variables as the more practical entry point.

---

## Terminology by Language

| Language | Term for concurrent unit |
|----------|--------------------------|
| Pascal-FC | Process |
| Java, Python | Thread |
| Ada | Task |

Note: "process" in concurrent programming ≠ OS-level process.

---

## Task Responses

**Week 7 Task 1 — Improving the maze strategy:**

*How to improve the single-person brute force:*  
- Mark visited paths to avoid re-exploring (memoisation)
- Use a heuristic to prioritise paths (e.g., keep right rule, A* direction bias)

*How to improve the team approach:*  
- Share information between team members so paths already explored aren't repeated
- Use coordination signals (semaphore-like flags at junctions) to communicate dead ends

*Team of 3 with a large maze:*  
- Assign each person a primary path at the first fork
- At subsequent forks, leave a person behind to cover branches and continue with the remainder
- Accept that with limited agents, some paths will be sequential rather than parallel
- Prioritise paths using heuristics (closer to exit) to allocate the 3 people where most likely to succeed

---

## Summary for Revision

- Concurrent ≠ Parallel. Concurrent is design; parallel is execution.
- Concurrent programs have partial ordering; sequential programs have total ordering.
- The challenges are at interaction points: synchronisation and communication.
- Correctness = safety (always holds) + liveness (eventually holds).
- Two approaches: shared variables (for understanding + localised) and message passing (for distributed).
