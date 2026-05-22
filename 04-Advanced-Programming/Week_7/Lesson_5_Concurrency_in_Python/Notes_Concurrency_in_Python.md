# Lesson 5: Concurrency in Python

**Source:** 7.10 Lesson 5

---

## Overview

Having covered the theory, this lesson applies it to Python. Python provides multiple approaches to concurrency — from the basic `threading` module to distributed frameworks — each with different trade-offs. Threads are the simplest starting point for understanding concurrent design, even though Python's threading model has a significant constraint: the GIL.

By the end of this lesson you should be able to:
- Build simple concurrent programs using the Python Thread API
- Understand what design decisions need to be made when selecting a concurrent approach

---

## 1. The Global Interpreter Lock (GIL)

The GIL is a **mutex** that protects CPython's internal state. Only one thread can hold the GIL and execute Python bytecode at a time.

**Consequences:**
- In CPython (the standard Python implementation), multiple threads **do not run in true parallel** — they interleave on a single core
- The GIL makes Python's memory management thread-safe without requiring the programmer to lock every individual object
- CPU-bound tasks do NOT benefit from threading (they are still serialised by the GIL)
- I/O-bound tasks DO benefit — threads release the GIL while waiting on I/O, allowing other threads to run

**Example:**
```
Thread A: waiting for network response → releases GIL
Thread B: runs while Thread A waits
Thread A: response arrives → re-acquires GIL, continues
```

**Workarounds:**
- `multiprocessing` module — uses OS processes instead of threads; each process has its own GIL (true parallelism)
- NumPy — can release the GIL for numerical operations (written in C), enabling genuine parallel execution
- Jython (Java-based Python) and PyPy STM — alternative implementations without the GIL

---

## 2. The threading Module

### Basic Thread Creation

```python
import threading

def task(name, n):
    for i in range(n):
        print(f"{name}: {i}")

t1 = threading.Thread(target=task, args=("Thread-1", 5))
t2 = threading.Thread(target=task, args=("Thread-2", 5))

t1.start()
t2.start()

t1.join()  # main thread waits for t1 to finish
t2.join()  # main thread waits for t2 to finish
```

### Key Thread Methods

| Method | Description |
|--------|-------------|
| `Thread(target, args, kwargs)` | Create a thread |
| `t.start()` | Start the thread |
| `t.join(timeout=None)` | Wait for the thread to complete |
| `t.is_alive()` | Check if thread is still running |
| `t.daemon = True` | Thread dies when main program exits |

### Synchronisation Primitives in Python

| Primitive | Python class | Maps to concept |
|-----------|-------------|-----------------|
| Mutex | `threading.Lock()` | Binary semaphore with ownership |
| Counting semaphore | `threading.Semaphore(n)` | Dijkstra semaphore; initial value n |
| Monitor/condition | `threading.Condition(lock)` | Monitor with condition variable |
| Read/write hint | `threading.Event()` | One-shot signal between threads |
| Barrier | `threading.Barrier(n)` | All n threads wait until all have arrived |
| RLock | `threading.RLock()` | Reentrant lock — same thread can acquire multiple times |

### Using Lock (Mutex)

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100):
        lock.acquire()   # wait (P)
        counter += 1
        lock.release()   # signal (V)

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # guaranteed to be 500
```

### Using Condition (Monitor pattern)

```python
import threading

condition = threading.Condition()
data_ready = False

def producer():
    global data_ready
    with condition:
        # produce data
        data_ready = True
        condition.notify()  # signal a waiting consumer

def consumer():
    global data_ready
    with condition:
        while not data_ready:
            condition.wait()  # block, release lock, wait for notify
        # consume data
```

---

## 3. Alternatives to threading

### multiprocessing

Uses OS-level processes rather than threads — each process has its own memory space and its own GIL. Achieves **true parallelism** on multi-core machines.

```python
from multiprocessing import Process

def worker():
    print("Running in separate process")

p = Process(target=worker)
p.start()
p.join()
```

Trade-off: Higher overhead than threads (process creation, IPC, memory duplication via copy-on-write); harder to share state (must use `multiprocessing.Queue` or `multiprocessing.Value`).

### concurrent.futures

High-level API wrapping both threads and processes:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    results = [f.result() for f in futures]
```

- `ThreadPoolExecutor` — thread-based; good for I/O-bound tasks
- `ProcessPoolExecutor` — process-based; good for CPU-bound tasks

### asyncio

Event-loop-based concurrency — single-threaded but uses cooperative multitasking. Coroutines yield control voluntarily (using `await`), allowing other coroutines to run.

```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)  # simulates I/O wait
    return "data"

async def main():
    results = await asyncio.gather(fetch_data("url1"), fetch_data("url2"))

asyncio.run(main())
```

Best for: high-concurrency I/O (many simultaneous network requests). Not suitable for CPU-bound work.

### NumPy's GIL Release

NumPy releases the GIL during C-extension execution for simple element-wise operations. This means threading actually achieves parallel computation for NumPy operations.

### Other Libraries

| Library | Model | Use case |
|---------|-------|---------|
| Twisted | Event-driven (reactor pattern) | Simulated concurrency via callbacks |
| Celery | Task queue over message broker | Distributed background jobs |
| Dask | Distributed computing | Large-scale data processing |
| Ray | Actor model | ML distributed training |

---

## 4. Design Decision Framework

When selecting a concurrency approach in Python:

| Task type | Best approach | Reason |
|-----------|--------------|--------|
| I/O-bound (many requests) | `threading` or `asyncio` | GIL released on I/O; threads or coroutines interleave effectively |
| CPU-bound (computation) | `multiprocessing` | Bypasses GIL; true parallelism |
| Simple parallel tasks | `concurrent.futures` | Clean API; choose Thread or Process pool easily |
| Distributed across machines | `Celery`, `Dask`, `Ray` | Full distributed computing |

Python may not be the best option for large-scale parallel systems — it is often used alongside C/C++ extensions (e.g., NumPy, TensorFlow) where performance-critical code runs natively.

> "Which library to select will depend very much on the level of concurrent activity required by the application or the problem solution. Python may not be the best option for large parallel systems and quite often it is used alongside other languages such as C."
> — Lesson 7.10

---

## Summary for Revision

| Concept | Detail |
|---------|--------|
| GIL | CPython mutex; only one thread runs Python bytecode at a time |
| threading | Simplest concurrency; good for I/O-bound; NOT parallel due to GIL |
| multiprocessing | True parallelism; each process has own GIL; higher overhead |
| asyncio | Single-threaded cooperative concurrency; best for high-concurrency I/O |
| concurrent.futures | High-level API for thread and process pools |
| Lock | Binary semaphore with ownership in Python |
| Semaphore | Counting or binary; `threading.Semaphore(n)` |
| Condition | Monitor + condition variable; `threading.Condition()` |
| Thread safety | Shared mutable state requires locks; immutable data is always safe |

**Key reference:** Beazley, D., Jones, B. K. (2013) *Python Cookbook*. 3rd ed. O'Reilly — Ch. 12
