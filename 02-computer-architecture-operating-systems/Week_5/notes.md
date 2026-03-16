# Week 5 — Memory Management and File Systems

## Topics Covered
- OS memory management (partitioning, paging, swapping)
- Virtual memory
- Inter-process communication (IPC)
- File systems fundamentals
- File compression and encryption
- File formats and encodings

---

## Key Concepts

### OS Memory Management
The OS is responsible for allocating memory to processes and protecting each process's memory from others.

**Techniques:**
- **Partitioning** — divide memory into fixed or variable regions for each process
- **Paging** — divide memory into fixed-size pages; allocate non-contiguous pages to a process (OS maps them to appear contiguous)
- **Swapping** — move inactive processes from RAM to disk (slow but extends effective memory)

### Virtual Memory
Virtual memory gives each process the **illusion of having more memory than physically available**. The OS maps virtual addresses to physical addresses using a **page table**.

When a process accesses a page not currently in RAM:
- **Page fault** occurs
- OS loads the required page from disk into RAM
- Execution resumes

Trade-off: page faults are expensive (disk access is slow). Excessive swapping = **thrashing** — system spends more time moving pages than executing code.

### Access Control and Process Isolation
Each process has its own protected memory space. The OS enforces this through:
- Memory address restrictions (processes cannot access each other's memory)
- **Privilege levels** — user mode vs kernel mode
- System calls as the only legitimate way to cross privilege boundaries

### Inter-Process Communication (IPC)
When processes need to share data:
- **Pipes** — one-directional data stream between processes
- **Message queues** — structured messages passed between processes
- **Shared memory** — a memory region accessible by multiple processes (fastest IPC, but requires synchronisation to avoid race conditions)

### File Systems
A file system is a structured method for organising and storing data on a storage device. It defines:
- How data is physically written to disk
- How files and directories are named and organised
- Access permissions and metadata

**Directory structure:** hierarchical tree from root (`/` on Unix, `C:\` on Windows) down through subdirectories.

**File attributes:** name, size, type, permissions (read/write/execute), ownership, timestamps.

**Symbolic links:** references to another file or directory — allows flexible organisation without duplicating data.

### Boot Sector
The boot sector is a special region of the disk read by firmware (BIOS/UEFI) on startup. It contains the bootloader, which loads the OS kernel into memory. Critical for system startup — corruption of the boot sector can make a system unbootable.

### File Compression
Compression reduces file size by encoding redundant data more efficiently:
- **Run-length encoding (RLE)** — replace repeated sequences with count + value (e.g. `AAAAA` → `5A`)
- **Lossless compression** — original data fully recoverable (ZIP, PNG)
- **Lossy compression** — some data discarded for higher compression ratio (JPEG, MP3)

### File Encryption
Encryption protects file contents from unauthorised access. Even if storage is stolen, encrypted files cannot be read without the key. Relevant to GDPR compliance for any system storing personal data.

### Common File Formats
| Format | Use |
|---|---|
| CSV | Tabular data, simple and universal |
| JSON | Structured data, API responses |
| XML | Structured documents with schema |
| Binary | Compact storage, not human-readable |

---

## Personal Note
Virtual memory and paging are relevant to my Python data processing work. When a pandas DataFrame is too large to fit in RAM, Python starts using virtual memory — which dramatically slows execution. Understanding this explains why chunked processing (`pd.read_csv(chunksize=...)`) is necessary for large infrastructure datasets. The OS-level concept has a direct practical implication in how I write data pipelines.

---

## Week 5 Summary
The OS manages memory through paging and virtual memory, creating the illusion of unlimited memory while enforcing process isolation. File systems provide the structured layer that organises data on storage devices. Compression and encryption are key techniques for managing file size and protecting data — both with direct relevance to GDPR-compliant data systems.
