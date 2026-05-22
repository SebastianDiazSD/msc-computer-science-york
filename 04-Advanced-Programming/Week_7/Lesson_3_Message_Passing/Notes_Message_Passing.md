# Lesson 3: Message Passing

**Source:** 7.6 Lesson 3 (both pages) + MessagePassingModels.docx

---

## Overview

The second approach to concurrent programming replaces shared memory with **message passing**. Processes are autonomous — each has its own private memory — and communicate exclusively by sending and receiving messages. This approach is more naturally suited to distributed systems (multiple machines) where shared memory is physically impossible.

By the end of this lesson you should be able to:
- Articulate the different models for using message passing in concurrency
- Identify the considerations required when using specific configurations in message passing

---

## 1. Why Message Passing?

Shared variable concurrency requires all processes to have access to the **same memory location**. This is fine on a single machine (even with multiple cores), but it is impossible across a network of machines. Message passing solves this:

- Each process has **independent memory**
- Data is exchanged by explicitly **sending** and **receiving** messages
- No need for mutual exclusion mechanisms (no shared state to protect)
- Naturally models client-server and IoT architectures

> "Without the concern for mutual exclusion, message passing models are often seen as being a lot simpler to implement, and in some senses this is true. However, this simplicity is soon absorbed into the complexity that can be achieved by this method."
> — Lesson 3

---

## 2. The send/receive Primitives

Every message passing system needs two fundamental operations:

| Operation | Behaviour |
|-----------|-----------|
| `send(destination, message)` | Sends a message to a destination; may or may not block |
| `receive(source)` | Receives a message; **always potentially blocking** (cannot receive before something is sent) |

The key design question is: **when does `send` block, if ever?**

---

## 3. Three Send Models (from MessagePassingModels.docx)

### Asynchronous (Non-blocking send)

The sender sends and immediately continues — it does not wait for the receiver to be ready.

```
Sender:
  send(msg)    ← returns immediately
  [continue with other work]

Receiver:
  [periodically checks mailbox]
  receive(msg)
```

- Requires a **buffer** to hold messages until the receiver is ready
- No guarantee the receiver has processed the message
- High throughput for the sender
- Analogous to: **posting a letter in a postbox**
- Used in: AJAX web requests, fire-and-forget event systems

### Synchronous (Blocking send)

Both sender and receiver must be ready simultaneously. The sender blocks until the receiver acknowledges; the receiver blocks until a message arrives.

```
Sender:
  send(msg)    ← blocks until receiver is ready
  [continues after receiver confirms]

Receiver:
  receive(msg) ← blocks until sender sends
  [processes message]
```

- No buffer required (the synchronisation itself is the handshake)
- Lower throughput but higher reliability
- Analogous to: **making a telephone call** — neither party acts until the other picks up
- Used in: real-time control systems, synchronised pipelines

### Remote Invocation

A variation on synchronous: the sender blocks until the receiver not only acknowledges but also **sends a reply**.

```
Sender:
  result = send(request)  ← blocks until reply received
  [uses result]

Receiver:
  receive(request)
  [process request]
  send(reply)
```

- Models a **function call** — you call and wait for a return value
- Analogous to: **asking for something over the counter** — you wait while they get it
- Used in: RPC (Remote Procedure Call), gRPC, RESTful API calls

---

## 4. Naming Conventions (from MessagePassingModels.docx)

When a process sends a message, how does it identify the recipient? There are four possibilities from two orthogonal choices:

| Dimension | Options |
|-----------|---------|
| **Direct vs Indirect** | Direct: send to a specific named process. Indirect: send to an intermediary (mailbox, channel, queue) |
| **Symmetric vs Asymmetric** | Symmetric: both sender and receiver name each other. Asymmetric: only one side names the other |

Combined options:

| Model | Description | Example |
|-------|-------------|---------|
| **Direct symmetric** | Sender names receiver AND receiver names sender | Telephone call — both parties have each other's number |
| **Direct asymmetric** | Sender names receiver, receiver accepts from anyone | Server listening on a port |
| **Indirect symmetric** | Both send to/receive from a named mailbox | Two people sharing a named inbox |
| **Indirect asymmetric** | Sender sends to a mailbox; receiver takes from any mailbox | P.O. box — sender addresses the box, receiver collects |

---

## 5. Coordination Models Summary

| Send model | Blocks sender? | Blocks receiver? | Buffer needed? |
|------------|---------------|-----------------|----------------|
| Asynchronous | No | Yes | Yes |
| Synchronous | Yes | Yes | No |
| Remote invocation | Yes (until reply) | Yes (until reply sent) | No |

---

## 6. Languages Built for Message Passing

| Language | Model | Domain |
|----------|-------|--------|
| **Ada** | Synchronous (rendezvous) | Embedded and real-time systems |
| **Erlang** | Asynchronous (actor model) | Telecoms, fault-tolerant distributed systems (WhatsApp) |
| **Rust** | Channel-based (ownership system) | Modern IoT, distributed, systems programming |
| **Python** | `multiprocessing.Queue`, `asyncio` | General, but not primary strength for large distributed |

> "WhatsApp is built using Erlang which was designed by Ericsson for managing their telecommunications systems."
> — Lesson 3

Language selection is a **fundamental part of solving a concurrent problem effectively** — not all languages are suitable for all problems and some do not scale as effectively as others.

---

## 7. Message Passing vs Shared Variables

| Aspect | Shared Variables | Message Passing |
|--------|-----------------|-----------------|
| Memory model | Shared | Private per process |
| Synchronisation | Locks, semaphores, monitors | Protocol of send/receive |
| Scale | Single machine | Distributed systems |
| Complexity source | Mutual exclusion, atomicity | Message ordering, buffering, naming |
| Python APIs | `threading` | `multiprocessing`, `queue`, `asyncio` |

---

## Further Reading References

- Watt, D. A., Findlay, W. *Programming Language Design Concepts* — §10.5.6 (Messages), §10.5.7 (Remote procedure calls), §10.6.3 (Rendezvous)
- Sebesta, R. W. (2016) *Concepts of Programming Languages* — §13.5

---

## Summary for Revision

| Term | Definition |
|------|-----------|
| Message passing | Concurrency model where processes communicate by sending/receiving messages; no shared memory |
| Asynchronous send | Sender does not block; requires buffer |
| Synchronous send | Both sender and receiver block until the exchange completes |
| Remote invocation | Sender blocks until receiver sends a reply; models a function call |
| Direct naming | Sender explicitly identifies the receiver process |
| Indirect naming | Sender addresses a mailbox/channel; receiver collects from there |
| Symmetric naming | Both sender and receiver name each other |
| Asymmetric naming | Only one party names the other |
| Rendezvous | Synchronous message passing construct used in Ada |
| Actor model | Each process (actor) has a private mailbox; used in Erlang |
