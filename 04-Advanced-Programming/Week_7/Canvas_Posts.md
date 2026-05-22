# Canvas Posts — Week 7: Concurrent Programming

---

## Activity 1 - Concurrency v parallelism
*(Padlet post — paste to the appropriate group Padlet)*

Here are four applications — two designed concurrently and two that aren't but would benefit from it:

**1. Web browser (concurrent):** While a page loads in one tab, I can watch a video, interact with another tab, and run a download simultaneously. Each tab and each network request runs on its own thread. Without concurrency, the entire browser would freeze on every fetch. The benefit here isn't just speed — it's responsiveness. The UI thread stays alive because I/O happens on background threads.

**2. Git CLI (not concurrent):** Running `git fetch` on a single remote is sequential, and git explicitly uses a lock file to prevent multiple operations on the same repo at once. If you're working with a monorepo pulling from many remotes, parallelising those fetches would give a significant speed-up. Some tools built on top of git (Turborepo, Bazel) do add this, but native git doesn't.

**3. VS Code (concurrent):** Extensions run in separate worker processes, the language server runs independently from the UI thread, and the file watcher is its own process. You can see the multiple processes in Task Manager. The benefit beyond speed: if the language server crashes, the editor keeps working. Isolation gives resilience, not just performance.

**4. Traditional Excel recalculation (not fully concurrent):** Historically, Excel recalculated all formulas sequentially in dependency order. Microsoft added multi-threaded recalculation in 2007 for "thread-safe" functions, but many functions are still single-threaded. Fully parallel recalculation across all cells is essentially a parallel DAG execution problem — interesting and solvable, but not trivially. The benefit would be dramatically faster recalculation on large financial models.

*Takeaway: speed isn't always the primary motivation — responsiveness, resilience, and resource isolation are all valid concurrent design goals.*

---

## Activity 2 - Message passing
*(Discussion board / Week 7 Lab)*

**Exercise 1 — Prime Sieve pseudocode:**

I designed this as a concurrent pipeline where each discovered prime gets its own filter thread. The generator feeds numbers into a queue. The main thread pulls the first number from the current queue — that's a prime by definition — spawns a filter thread for it, and moves to the next queue. Each filter thread passes on only numbers not divisible by its prime.

Termination works by propagating a `None` sentinel downstream: the generator puts a `None` after the last number; each filter stage, on receiving it, passes it on and exits; the main thread exits when it receives the sentinel.

For variant 1 (limit by numbers examined): generator stops at `limit` and sends the sentinel.  
For variant 2 (limit by primes found): main thread breaks out of the loop once `len(primes) == k` and signals cleanup.

The sieve is elegant for teaching message passing — each stage maps cleanly to a thread and there's no shared state. But it's not efficient at scale: you need one thread per prime, which for primes up to 1000 is 168 threads. For real workloads, a segmented parallel sieve would be better.

**Exercise 2 — Chinese Whispers pseudocode:**

I modelled this as N processes in a circular ring. Each process has one input queue and one output queue. The starter sends the original message, waits for it to return, then prints the comparison and sends a `None` termination sentinel around the ring. Each non-starter player receives a message, rolls a random number against `error_chance`, optionally swaps two characters, and forwards it.

The circular topology is the key design detail — Player N-1's output queue wraps back to Player 0's input queue. This is indirect asymmetric naming: each player only knows its next neighbour's queue, not who sent to it. Termination propagates as a sentinel the same way as the sieve.

---

## Activity 3 - Parallel problems
*(Discussion board)*

**Exercise 1:**

**Livelock:** Conditions — two or more processes repeatedly change state in response to each other; neither is blocked (the OS sees them as running); neither makes progress. End result: indefinite CPU consumption with no useful work. The classic example is two processes each backing off when they detect a conflict, but both backing off simultaneously, then retrying simultaneously, repeating forever. Think of two people trying to pass each other in a corridor by stepping the same way.

**Deadlock:** Conditions — all four Coffman conditions must hold simultaneously: mutual exclusion (resource held non-sharably), hold-and-wait (holding one while waiting for another), no preemption (can't forcibly take resources), circular wait (A waits for B, B waits for A). End result: permanent halt. All involved processes block forever unless externally interrupted.

**Race conditions:** Conditions — concurrent access to a shared resource where at least one access is a write, with no synchronisation controlling ordering. End result: non-deterministic, incorrect output that varies between runs. The data may be silently corrupted — no crash, just wrong answers, which makes race conditions particularly dangerous.

**Starvation:** Conditions — a process is perpetually denied a resource it needs, while other processes continue to receive service. The deprived process isn't necessarily blocked — it simply keeps losing. End result: that process never completes. A liveness property is violated.

**Exercise 2 — Dining Philosophers:**

**Deadlock:** All five philosophers pick up their left fork simultaneously. Each then waits for their right fork, which is held by the philosopher to their right. A circular wait forms: 0 waits for 1, 1 for 2, 2 for 3, 3 for 4, 4 for 0. All four Coffman conditions are satisfied. The system permanently halts.

**Livelock:** A "polite" retry strategy where each philosopher puts down their left fork if they can't get the right one, waits, then tries again. If all five do this simultaneously, they pick up left forks together, fail to get right forks together, put down left forks together, wait the same duration, and retry together. No one is blocked — everyone is active — but no one eats.

**Starvation:** Even without deadlock or livelock, one philosopher can be consistently beaten to the forks by both neighbours. If scheduling is unfair or the two neighbours happen to alternate eating, the philosopher between them is perpetually denied both forks. The other four may be dining normally throughout.

---

## Activity 4 - Concurrency in Python
*(Week 7 Lab — share notebook link or upload file)*

I implemented all six problems from the activity in Python using the `threading` and `queue` modules. Here's a summary of the design decisions:

**Update problem (semaphore):** Used `threading.Semaphore(1)` — a binary semaphore — to wrap the increment critical section. `acquire()` = Dijkstra's P (wait); `release()` = V (signal). Without the semaphore, the race condition causes non-deterministic results between 20 and 40. With it, always 40.

**Bounded Buffer:** Used `threading.Condition` with two condition variables (`not_full`, `not_empty`). This is Python's monitor implementation — `condition.wait()` atomically releases the lock and blocks. Used `while` not `if` for the condition check to guard against spurious wakeups.

**Readers/Writers:** First-readers-preference solution using two locks: `readers_lock` protects `readers_count`; `resource_lock` gives exclusive access to writers. The first reader acquires `resource_lock` (blocking writers); the last reader releases it. Known limitation: writer starvation if readers arrive continuously.

**Dining Philosophers:** Implemented the naive (left-then-right) version as commented-out code to demonstrate the deadlock risk, and the resource hierarchy solution as the live implementation. The fix: always acquire `min(left, right)` first. Philosopher 4 picks up fork 0 before fork 4, breaking the circular wait.

**Prime Sieve:** Thread pipeline — one generator thread, one filter thread per discovered prime. First number from each stage is prime by definition; filter stage drops multiples. Sentinel-based termination propagates downstream.

**Chinese Whispers:** Circular ring of threads communicating via `queue.Queue`. Starter sends the initial message, waits for it to return, compares to original. Non-starters apply `error_chance` probability to swap two characters. Termination propagates as `None` sentinel around the full ring.

All code is in `Activity_4_Concurrency_in_Python.ipynb`. Happy to discuss any of the implementations.
