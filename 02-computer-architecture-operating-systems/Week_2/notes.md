# Week 2 — Computer Memory Systems

## Topics Covered
- Types of memory (volatile vs non-volatile, SRAM vs DRAM)
- Memory hierarchy and performance
- Cache memory (L1, L2, L3)
- Cache management policies
- Error detection and correction (ECC)
- Memory mapping and cache coherency

---

## Key Concepts

### Volatile vs Non-Volatile Memory
| Type | Power off = data lost? | Example | Use |
|---|---|---|---|
| Volatile | Yes | SRAM, DRAM | Working memory (RAM) |
| Non-volatile | No | Flash, ROM | Storage, firmware |

### SRAM vs DRAM
| | SRAM | DRAM |
|---|---|---|
| Speed | Faster | Slower |
| Cost | More expensive | Cheaper |
| Density | Lower | Higher |
| Use | Cache memory | Main memory (RAM) |
| Refresh needed | No | Yes (capacitors leak) |

DRAM requires constant refresh cycles to maintain data — this is one reason it is slower than SRAM.

### Memory Hierarchy
Speed and cost are inversely related in memory systems. The hierarchy (fastest/most expensive → slowest/cheapest):

```
Registers (CPU)
    ↓
L1 Cache (fastest, smallest ~32KB)
    ↓
L2 Cache (~256KB)
    ↓
L3 Cache (shared, ~8-32MB)
    ↓
Main Memory / RAM (GB range)
    ↓
Secondary Storage / SSD/HDD (TB range)
```

The key insight: **cache exists to bridge the speed gap between CPU and main memory.**

### Cache Memory
Cache is a small, fast buffer that stores frequently accessed data close to the CPU. When the CPU requests data:
- **Cache hit** — data is found in cache → fast access
- **Cache miss** — data not in cache → must fetch from RAM → slow

**Cache management policies:**
- **Placement** — where in cache a block is stored (direct-mapped, set-associative, fully associative)
- **Replacement** — which block to evict when cache is full (LRU = Least Recently Used is most common)
- **Write policy** — write-through (update cache and memory immediately) vs write-back (update memory only when evicted)

### Principle of Locality
Programs tend to access data in predictable patterns:
- **Temporal locality** — if you access a memory location, you will likely access it again soon
- **Spatial locality** — if you access a location, you will likely access nearby locations soon

Cache design exploits both principles. Writing cache-friendly code (sequential access patterns, avoiding random jumps) significantly improves performance.

### Error Detection and Correction (ECC)
Memory errors are classified as:
- **Hard failures** — permanent physical defects
- **Soft errors** — temporary disruptions (e.g. alpha particles, power fluctuations)

ECC (Error Correcting Code) adds extra bits to stored data to detect and correct single-bit errors automatically. Critical in servers and safety-critical systems.

### Memory Mapping
I/O devices are assigned memory addresses in the same address space as RAM — this is **memory-mapped I/O**. Programmers and engineers interact with hardware by reading and writing to these addresses. Essential for embedded systems and low-level driver development.

### Cache Coherency
When multiple processors or cores share memory, or when caches interact with I/O devices, **cache coherency** becomes critical. If one core updates a value in its cache but another core still reads the old value, data inconsistency occurs. Coherency protocols (e.g. MESI) ensure all caches stay synchronised.

---

## Personal Note
Memory hierarchy concepts are directly applicable to optimising Python data pipelines. When processing large CSV files for railway cost deviation analysis, loading data into memory efficiently (using pandas chunking, for example) reflects the same principle as cache management — keep frequently accessed data close, avoid unnecessary re-reads from disk.

---

## Week 2 Summary
Memory systems are a critical performance bottleneck in computer architecture. The hierarchy from registers to secondary storage represents a fundamental trade-off between speed and cost. Cache memory, with its management policies and coherency requirements, is the main mechanism for bridging the CPU-memory speed gap. Understanding memory behaviour is essential for writing performant code.
