# Week 1 — Python Fundamentals

## Topics Covered
- Variables and calculations
- Decision structures (if/elif/else)
- Iteration structures (for/while)
- Best practices
- Strings and I/O (formatting, console input/output)
- Data structures (list, tuple, set, dictionary)
- Functions (arguments, return, scope)
- Modules and classes

---

## Key Concepts

### Variables and Calculations
Python is dynamically typed — no need to declare variable types explicitly.
```python
project_budget = 5_500_000        # int (underscores for readability)
deviation_rate = 0.127            # float
project_name = "Karlsruhe-Basel"  # str
is_active = True                  # bool
```

Arithmetic operators: `+`, `-`, `*`, `/` (float division), `//` (integer division), `%` (modulo), `**` (exponentiation)

### Decision Structures
```python
if deviation_rate > 0.10:
    print("High deviation — escalate to project manager")
elif deviation_rate > 0.05:
    print("Moderate deviation — monitor closely")
else:
    print("Within tolerance")
```

**Ternary (one-line):**
```python
status = "over budget" if deviation_rate > 0.10 else "on track"
```

### Iteration Structures
```python
# for loop — iterate over a sequence
work_packages = ["earthworks", "concrete", "track", "signalling"]
for package in work_packages:
    print(f"Reviewing: {package}")

# while loop — repeat until condition is false
attempts = 0
while attempts < 3:
    attempts += 1

# range()
for i in range(1, 8):   # 1 to 7 inclusive
    print(f"Week {i}")
```

### Best Practices
- Use descriptive variable names (`deviation_rate` not `dr`)
- Follow PEP 8 style guide (4-space indentation, snake_case for variables)
- Write functions for reusable logic (DRY — Don't Repeat Yourself)
- Add comments for non-obvious logic, not obvious ones
- Use constants for magic numbers: `MAX_DEVIATION = 0.10`

### Strings and I/O
```python
# f-strings (preferred for formatting)
budget = 5_500_000
print(f"Project budget: €{budget:,.0f}")  # €5,500,000

# Console input
project_name = input("Enter project name: ")

# String methods
name = "  karlsruhe-basel  "
name.strip()      # remove whitespace
name.upper()      # KARLSRUHE-BASEL
name.split("-")   # ["karlsruhe", "basel"]
```

### Data Structures
| Structure | Syntax | Ordered | Mutable | Duplicates | Use |
|---|---|---|---|---|---|
| List | `[]` | Yes | Yes | Yes | Ordered collection |
| Tuple | `()` | Yes | No | Yes | Fixed data, function returns |
| Set | `{}` | No | Yes | No | Unique values, fast lookup |
| Dictionary | `{K:V}` | Yes (Python 3.7+) | Yes | Keys: No | Key-value mapping |

```python
# List
projects = ["Nuremberg-Regensburg", "Karlsruhe-Basel"]
projects.append("Stuttgart-Ulm")

# Dictionary — most commonly used in data pipelines
project_data = {
    "name": "Karlsruhe-Basel",
    "budget": 5_500_000,
    "deviation": 0.127
}
print(project_data["budget"])        # 5500000
project_data["status"] = "active"   # add key

# Set
unique_contractors = {"Hochtief", "Strabag", "Hochtief"}  # {"Hochtief", "Strabag"}
```

### Functions
```python
def calculate_deviation(planned: float, actual: float) -> float:
    """Calculate cost deviation as a percentage."""
    return (actual - planned) / planned

# Default arguments
def format_cost(amount: float, currency: str = "EUR") -> str:
    return f"{currency} {amount:,.2f}"

# *args and **kwargs
def log_event(*args, **kwargs):
    print(args, kwargs)
```

**Variable Scope:**
- **Local** — defined inside a function, not accessible outside
- **Global** — defined at module level
- Use `global` keyword sparingly — prefer passing values as arguments

### Modules and Classes
```python
# Importing modules
import pandas as pd
from pathlib import Path

# Defining a class
class ProjectReport:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.actual_cost = 0.0
    
    def set_actual_cost(self, cost: float):
        self.actual_cost = cost
    
    @property
    def deviation(self) -> float:
        return (self.actual_cost - self.budget) / self.budget
    
    def __repr__(self):
        return f"ProjectReport({self.name}, deviation={self.deviation:.1%})"
```

---

## Personal Note
Python was already my main language before this module — I have used it for all four G2T apps. The class design exercise in Week 1 is directly applicable to how I structure data models in FastAPI (Pydantic BaseModel is a class with type annotations). The best practices section reinforced habits I have been developing: descriptive names, type hints, and DRY functions.

---

## Week 1 Summary
Week 1 establishes Python fundamentals: variables, control flow, iteration, data structures, functions, and classes. The key shift from scripting to proper software development is applying best practices consistently — naming, structure, and documentation. These fundamentals are the foundation for everything in the module.
