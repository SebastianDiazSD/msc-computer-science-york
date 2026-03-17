# Week 2 — Advanced Programming Activities

**Module:** Advanced Programming — MSc Computer Science, University of York  
**Topics:** Data formats, File I/O, Exception handling, Regular expressions, Format translation, Databases

---

## Files in this folder

| File | Activity | Description |
|---|---|---|
| `Activity1_DataFormats.ipynb` | Activity 1 | XML and JSON data structuring with discussion |
| `GradeDataToXML.txt` | Activity 1 Ex.1 | XML document with DTD — grade data |
| `RaceDataToJSON.txt` | Activity 1 Ex.2 | JSON document — horse race data |
| `Activity2_FileProcessing.ipynb` | Activity 2 | CSV parsing, sorting, and update processing |
| `PeopleTrainingDate.csv` | Activity 2 | Main dataset |
| `PeopleTrainingDateUpdate.csv` | Activity 2 Ex.3 | Update dataset (different column order) |
| `sorted_output.csv` | Activity 2 output | Final merged, date-sorted CSV |
| `Activity3_Exceptions_Assertions.ipynb` | Activity 3 | Exception handling and assertions |
| `Activity4_Regex.ipynb` | Activity 4 | Regular expressions on The Raven.txt |
| `The_Raven.txt` | Activity 4 | Source text for regex exercises |
| `Activity5_FormatTranslation.ipynb` | Activity 5 | JSON → XML translation with integrity check |
| `People_output.xml` | Activity 5 output | Generated XML from People.json |
| `Activity6_MongoDB.ipynb` | Activity 6 | MongoDB setup, data load, and queries |
| `People.json` | Activities 5 & 6 | Student records dataset |

---

## Activity 1 — Constructing Data Formats

**Exercise 1:** Grade data structured in XML with a DTD that enforces element hierarchy (`gradedata > student > id/name/grades`). Validated at xmlvalidation.com.

**Exercise 2:** Horse race data structured in JSON. Design uses two top-level arrays (`races`, `horses`) to avoid repeating horse metadata in every result. `null` is used explicitly for missing positions and DNF reasons.

**Exercise 3:** Discussion on type systems (DTD vs JSON), duck typing, and the trade-offs between CSV, JSON, and XML for modern application development.

---

## Activity 2 — File Processing

**Exercise 1:** CSV parsed using string functions only (`split`, `strip`, `join`) — no `csv` module. Records stored as a list of dicts with field access by name, not by index.

**Exercise 2:** Records sorted by `Updated` date (oldest first) using `datetime.strptime` and `sorted()`. Output written to `sorted_output.csv` with `Updated` as the first column.

**Exercise 3:** Update file (`PeopleTrainingDateUpdate.csv`) has a different column order (`ID,Email,Updated,Title,Company,Name`). The parser handles this dynamically by building a `field_index` map from the file's own header row — no hardcoded column indices. Duplicate IDs are detected, reported, and overwritten with the update record. Final output is re-sorted and written back.

---

## Activity 3 — Exception Handling and Assertions

Four broken code blocks from `MissingExceptions.ipynb` corrected with specific exception types (`ValueError`, `ZeroDivisionError`, `IndexError`, `FileNotFoundError`, `PermissionError`, `IsADirectoryError`). Exception handler for the list loop is placed *inside* the loop so valid elements are still processed after the bad one.

Assertions demonstrated in two functions from the Ground2Tech cost deviation project: `calculate_deviation` (preconditions on input types and ranges, postcondition on result bounds) and `parse_project_row` (precondition on required dict keys, postcondition on output structure).

---

## Activity 4 — Regular Expressions

All five tasks on `The_Raven.txt`:
1. Find `shrieked` — found once
2. Find `bleak` — not present in this excerpt (correct result)
3. Words containing `pp` — `napping`, `tapping`, `rapping` (5 occurrences, 3 unique)
4. Replace `!` with `#` — 6 replacements
5. Words starting with `t` not ending with `e` (case-insensitive) — `tapping`, `this`, `that`, `tempest`, `token`, `thy`, `Tis`

Discussion connects regex to real use: VOB/B clause extraction (`§ 4 Abs. 7`) in the Tender Document Risk Analyzer app.

---

## Activity 5 — Format Translation

`People.json` translated to `People_output.xml` using `xml.etree.ElementTree`. Round-trip verification parses the generated XML back and compares every field against the original JSON — all match.

Key design decision: JSON `null` middle names are represented as empty XML elements (`<middleName />`), preserving the structural presence of the field while expressing the absence of a value.

---

## Activity 6 — MongoDB

Setup, data insertion, and three queries against `People.json`:
1. Full name of anyone over 25 — uses `{ "age": { "$gt": 25 } }`
2. ID of anyone with no middle names — uses `$not $elemMatch $ne null` to match `"other": [null]`
3. Count men and women not in Tokyo — implemented as both Python-side filtering and a MongoDB aggregation pipeline

> **Note:** Activity 6 requires a running MongoDB instance. Run `mongod` before executing the notebook cells.
