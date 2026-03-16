# Week 2 — Data Encoding, File I/O, Exceptions, Regex, Parsing, and Databases

## Topics Covered
- Data encoding (binary, text, encodings)
- File formats overview
- File input and output (reading, writing, binary)
- Exception handling (try/except, re-raising, custom exceptions)
- Regular expressions
- Parsing: CSV, XML, JSON
- Databases (SQLite with Python)

---

## Key Concepts

### Data Encoding
Computers store everything as binary (0s and 1s). Encoding defines how binary maps to human-readable characters.

Key encodings:
- **ASCII** — 128 characters, English only, 1 byte per character
- **UTF-8** — Universal, backwards compatible with ASCII, variable length (1-4 bytes), handles all languages including German (ä, ö, ü) and Spanish (ñ, á, é)
- **Binary encoding** — raw bytes, no text interpretation

Always specify encoding explicitly when reading/writing files:
```python
with open("report.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### File Formats
| Format | Human-readable | Use case |
|---|---|---|
| CSV | Yes | Tabular data, simple exchange |
| JSON | Yes | API responses, config files |
| XML | Yes | Structured documents, legacy systems |
| Binary | No | Images, executables, compressed files |

### File Input and Output
```python
# Reading a file (text)
with open("data.csv", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Writing a file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Cost deviation report\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Appending
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New entry\n")

# Binary access
with open("image.jpg", "rb") as f:  # r = read, b = binary
    data = f.read()
```

The `with` statement (context manager) automatically closes the file — always use it.

### Exception Handling
```python
# Basic try/except
try:
    value = int(input("Enter a number: "))
except ValueError as e:
    print(f"Invalid input: {e}")
except (TypeError, ZeroDivisionError) as e:
    print(f"Calculation error: {e}")
else:
    print("Success")   # runs if no exception
finally:
    print("Always runs")  # cleanup code

# Re-raising an exception
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Logging error...")
    raise  # re-raises the same exception

# Custom exceptions
class DeviationExceededException(Exception):
    def __init__(self, rate: float):
        super().__init__(f"Deviation {rate:.1%} exceeds threshold")
        self.rate = rate

raise DeviationExceededException(0.25)
```

### Regular Expressions
Regular expressions (regex) are patterns for matching text. Essential for parsing unstructured data.

```python
import re

text = "Project PFA 9.0 — Budget: €5,500,000 — Status: Active"

# Basic patterns
re.findall(r"\d+", text)           # find all digit sequences
re.findall(r"€[\d,]+", text)       # find currency amounts
re.search(r"PFA \d+\.\d+", text)   # find project code

# Groups
match = re.search(r"Budget: €([\d,]+)", text)
if match:
    budget_str = match.group(1)    # "5,500,000"

# Common pattern symbols
# \d = digit, \w = word char, \s = whitespace, . = any char
# + = one or more, * = zero or more, ? = zero or one
# ^ = start of string, $ = end of string
# [abc] = character class, [^abc] = negated class
```

### Parsing: CSV, XML, JSON

**CSV:**
```python
import csv

# Reading
with open("projects.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["project_name"], row["budget"])

# Writing
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "budget", "deviation"])
    writer.writeheader()
    writer.writerow({"name": "Karlsruhe-Basel", "budget": 5500000, "deviation": 0.127})
```

**JSON:**
```python
import json

# Parse JSON string / file
data = json.loads('{"name": "Project A", "budget": 1000000}')
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)  # ensure_ascii=False for ä, ö, ü
```

**XML:**
```python
import xml.etree.ElementTree as ET

tree = ET.parse("report.xml")
root = tree.getroot()
for project in root.findall("project"):
    name = project.find("name").text
```

### Databases (SQLite)
```python
import sqlite3

# Connect (creates file if not exists)
conn = sqlite3.connect("projects.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        budget REAL,
        actual_cost REAL
    )
""")

# Insert — ALWAYS use parameterised queries (prevents SQL injection)
cursor.execute(
    "INSERT INTO projects (name, budget, actual_cost) VALUES (?, ?, ?)",
    ("Karlsruhe-Basel", 5500000, 6198500)
)
conn.commit()

# Query
cursor.execute("SELECT * FROM projects WHERE budget > ?", (1000000,))
rows = cursor.fetchall()

conn.close()
```

**Never use string formatting in SQL queries** — always use `?` placeholders (parameterised queries). This prevents SQL injection attacks covered in Cyber Security Week 5.

---

## Personal Note
This week covers the exact stack I use in my G2T apps. In the Cost Deviation Tracker, I read CSV files with pandas (built on csv), process them with Python, and serve results via Streamlit. In App 4, I parse JSON from FastAPI request bodies. The regex knowledge is directly applicable to App 2 (Contract Risk Analyzer) — I use PyMuPDF to extract text from PDFs and regex to identify VOB/B clause numbers like §4, §8, §13, §16. The database section reinforces the SQL injection prevention practice I already apply — always parameterised queries, never string concatenation.

---

## Week 2 Summary
Week 2 covers the full data pipeline: encoding and format → reading and writing files → error handling → pattern matching with regex → parsing structured formats (CSV, JSON, XML) → persisting data in SQLite. These are the practical building blocks of almost every data-driven application. The connection between SQL injection (Cyber Security) and parameterised queries (this week) shows how security and programming concepts are deeply linked.
