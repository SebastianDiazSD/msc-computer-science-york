# Activity 1 — Padlet: Concurrency v Parallelism

**Activity label:** Activity 1 - Concurrency v parallelism

---

## Padlet Post

Here are four applications — two that are clearly designed to run concurrently, and two that aren't (but would benefit from it):

---

**1. Web browser — designed to run concurrently**  
You can tell because while a page is still loading in one tab, you can interact with another tab, watch a video, and download a file all at the same time. Each tab and each network request runs as a separate thread or process. Without concurrency, the entire browser would freeze every time it fetched a resource. The benefit isn't just speed — it's responsiveness. The UI thread staying live while I/O happens in the background is a classic concurrent design.

---

**2. Git (standard command-line) — not designed to run concurrently**  
By default, `git fetch` or `git pull` on a single remote is a single-threaded sequential operation. You can't run multiple git operations on the same repo at the same time either — it uses a lock file to prevent this explicitly. If you have a monorepo pulling from many remotes, parallelising those fetch operations would significantly speed things up. Some newer tooling (like Bazel or Turborepo) does add parallel fetching on top, but native git is sequential.

---

**3. VS Code — designed to run concurrently**  
Extensions run in separate worker processes, the language server (e.g., Pylance) runs in its own process, and the file watcher runs independently from the UI thread. You can see this if you open Task Manager while running VS Code — multiple processes. The benefit beyond speed: if a language server crashes, VS Code keeps running. Isolation between concurrent processes adds resilience, not just performance.

---

**4. Excel (traditional formula recalculation) — not designed to run concurrently (or was limited)**  
Historically, Excel recalculated all formulas sequentially in dependency order. On large spreadsheets this caused noticeable pauses. Microsoft added multi-threaded recalculation in Excel 2007 for "thread-safe" functions, but many functions are still single-threaded. Fully concurrent recalculation across all cells would require resolving inter-cell dependencies correctly — which is essentially a parallel DAG execution problem. The benefit would be dramatically faster recalculation on large models.

---

*Speed isn't the only benefit — resilience, responsiveness, and resource isolation are all valid reasons to design concurrently.*
