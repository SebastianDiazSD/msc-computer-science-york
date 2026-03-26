# Week 3: Event-Driven Programming & GUI Design

---

## Learning Objectives

- Articulate the main concepts within event-driven programming and compare it to other paradigms
- Define programs using UML state diagrams
- Write Python code using closures and lambda expressions
- Select and justify GUI components for representing specific program requirements
- Apply wireframe diagrams to express GUI design ideas
- Generate interaction between GUI components using Tkinter
- Input and output data from an interface to file
- Articulate how event-driven programming underpins other areas of software development

---

## Lesson 1 — Event-Driven Programming

### Core Concept

In event-driven programming, an **event** is the key element (analogous to the object in OOP). Events can be user interactions (mouse clicks, key presses) or system signals (sensor readings, incoming network messages).

The **event handler** continuously listens for events in a loop. When an event occurs, a **callback function** is triggered to perform the associated action.

### Deterministic vs Non-Deterministic Programs

| Sequential / Deterministic | Event-Driven / Non-Deterministic |
|---|---|
| All possible paths can be mapped | Paths cannot be fully predetermined |
| Program flow is fixed | Events can occur at any point during runtime |
| Easier to reason about statically | Requires state modelling to manage complexity |

In event-driven systems, what *can* be captured is the **state** of the program at any given point. For a program with 10 binary-state buttons, there are 2¹⁰ = 1024 potential states — not all of which may be reachable, but all must be considered.

### Key Terms

- **Event:** An action or occurrence detected by the program (click, keypress, sensor signal)
- **Event Handler:** The loop actively listening for events and routing them to the correct callback
- **Callback Function:** The function executed in response to a specific event
- **State:** The condition of the program/objects at any given moment in time

---

## Lesson 2 — Formal Tools: UML State Diagrams

### Why State Diagrams?

State diagrams from UML (Unified Modelling Language) help map out what an event-driven program *may potentially do*, even when full paths cannot be determined. They communicate design intent clearly and are an industry standard used by governments and businesses alike.

### State Diagram Notation (Common Elements)

| Symbol | Meaning |
|---|---|
| Filled black dot with arrow | Start point |
| Arrow pointing to circled dot | End point |
| Arrow with label | Transition (event/action that changes state) — may include a `[Guard]` condition |
| Simple box | State |
| Box with horizontal divider | State with internal transitions |
| Composite box | Nested state with internal structure |
| Note box (folded corner) | Additional information / annotation |
| Fork / Join bars | Splitting or merging transitions |

### Best Practices

- Split complex systems into **groups of meaningful functionality** — avoid one enormous diagram
- Always include: **title, author, date, version number**, and any notation adaptations
- Treat diagrams like code: **copy and edit, never overwrite**

### Recommended Tools

- [Lucidchart](https://lucidchart.com) — online, integrates with Google Drive, free tier available
- [StarUML](https://staruml.io) — cross-platform desktop app, free license (prompts upgrade on save)
- Visual Paradigm / Eclipse Papyrus — more formal/professional options

---

## Lesson 3 — Closures and Lambda Expressions

### Why These Matter for GUIs

Closures and lambda expressions are two powerful Python features frequently used when building complex GUIs — particularly for assigning dynamic behaviors to multiple widgets with minimal code.

### First-Class Functions

In Python, functions are **first-class entities** — they can be assigned to variables, passed as arguments, and returned from other functions.

```python
def addValues(num1, num2):
    return num1 + num2

myFunction = addValues   # Function assigned to a variable
myFunction(11, 4)        # Returns 15
```

### Variable Scope and `nonlocal`

Nested functions can access the enclosing function's scope. However, to *modify* a variable from the outer scope inside an inner function, the `nonlocal` keyword must be used:

```python
def addValues(num1, num2):
    total = num1 + num2
    def printSum():
        nonlocal total
        total += 5
        print("Sum:", total)
    printSum()
```

### Closures

A **closure** is a nested function returned from its enclosing function, **carrying its enclosing scope with it** — even after the outer function no longer exists.

```python
def addValues(num1, num2):
    total = num1 + num2
    def printSum():
        print("The sum is:", total)
    return printSum         # Return the inner function, not its result

result = addValues(6, 7)
del addValues               # Outer function deleted
result()                    # Still works — prints: The sum is: 13
```

The inner function `printSum` *closes over* the variable `total`, preserving it even after `addValues` is gone.

### Lambda Expressions

A **lambda** is a short, anonymous, single-expression function:

```python
lambda arguments : expression
```

Example:

```python
double = lambda y : y * 2
print(double(5))   # 10
```

Lambda + Closure pattern for generating related functions dynamically:

```python
def includeVAT(price):
    return lambda x : (price * 1.2) * x

itemCost = includeVAT(0.57)
itemCost(10)   # 6.84

# Generate a list of VAT calculators for prices £1–£8
itemCosts = [includeVAT(i) for i in range(1, 9)]
print(itemCosts[6](5))   # 5 items at £7 including VAT = £42.0
```

This pattern is widely used for assigning event handlers to multiple GUI buttons with different parameters.

---

## Lesson 4 — GUI Design Principles

### Interface Components (Common Tkinter Widgets)

| Widget | Purpose |
|---|---|
| `Label` | Display static text |
| `Button` | Trigger an action |
| `Entry` | Single-line text input |
| `Text` | Multi-line text input/output |
| `RadioButton` | Select exactly one from a group |
| `CheckButton` | Select one or more options |
| `Listbox` | Select from a list |
| `Scale` | Slide to select a value from a range |
| `Spinbox` | Select from a range with up/down arrows |
| `Message` | Multi-line display text |
| `Menu` / `Menubar` | Navigation and command menus |
| `Scrollbar` | Scroll through content |

### Wireframes

A **wireframe** is a low-fidelity sketch of the interface layout produced *before* coding begins. It clarifies:

- Which components belong together
- How user tasks flow from one screen to another
- The hierarchical relationship between container and child widgets

Recommended tools: [Pencil Project](https://pencil.evolus.vn) (open source desktop), [Lucidchart](https://lucidchart.com)

### Design Heuristics

Jakob Nielsen's 10 Usability Heuristics remain widely cited. Key principles relevant to this module:

- Visibility of system status
- Match between system and the real world
- User control and freedom
- Consistency and standards
- Error prevention

**Colour:** Use hex values or CSS colour names (e.g., `#9ACD32` = yellow green). Consider accessibility — colour is perceived differently across individuals and has cultural associations.

---

## Lesson 5 — Tkinter for GUIs in Python

### Why Tkinter?

Tkinter is part of Python's **standard library** — no installation required. It is simple, uses familiar OOP concepts, and is well-suited for building prototype interfaces.

Key packages:

- `tkinter` — core widgets
- `tkinter.ttk` — themed widgets with more flexible styling
- `tkinter.tix` — extended widget set

### Main Window

```python
import tkinter as tk
window = tk.Tk()
window.title("My App")
window.geometry("400x200")
window.mainloop()   # Starts the event loop
```

> **Note:** In Jupyter Notebook, the exit button may not work as expected — stop the kernel manually.

### Layout Managers

| Manager | Description | Best For |
|---|---|---|
| `pack()` | Stacks widgets into minimum space | Simple row/column arrangements |
| `grid()` | Places widgets on a row/column grid | Structured, multi-component layouts |
| `place()` | Absolute x/y pixel positioning | Maximum control, overlapping elements |

**`grid()` tip:** Use `grid_rowconfigure(i, weight=1)` and `grid_columnconfigure(i, weight=1)` so widgets expand to fill the window when it is resized.

### Adding Style

**Standard `tk` widgets** — style via attributes directly:

```python
tk.Label(window, text='York', fg='SteelBlue', bg='LightGray')
```

**`ttk` widgets** — use a `Style` object:

```python
ttk.Style().configure("TButton", foreground='SteelBlue', background='LightGray')

# Sub-tag for specific instances
style = ttk.Style()
style.configure("Yell.TLabel", foreground="blue", background="yellow", padding=3)
ttk.Label(window, text='A', style='Yell.TLabel')
```

### Container Widgets

Container widgets hold and group other widgets:

- `Frame` — basic grouping container
- `ttk.LabelFrame` — labelled grouping container
- `ttk.Notebook` — tabbed interface
- `PanedWindow` — resizable pane divider

### Canvas Component

A free-form drawing area supporting shapes, images, and text:

```python
c = tk.Canvas(window, width=350, height=400)
c.pack()
c.create_rectangle(40, 40, 110, 110, fill="#FD6707")
c.create_oval(90, 120, 190, 170, outline='#FD6707', width=10)
img = tk.PhotoImage(file="image.png")
c.create_image(20, 180, anchor=tk.NW, image=img)
```

Coordinates start at `(0, 0)` top-left. Elements drawn later overlap earlier ones.

---

## Lesson 6 — Implementing Interaction

### Binding Event Handlers (Callbacks)

The simplest way: pass a function name to a widget's `command` parameter:

```python
def on_click():
    print("Button clicked")

tk.Button(window, text="Click me", command=on_click).pack()
```

### Special Variables (Listeners)

Tkinter provides special variable types that act as listeners — when their value changes, any widget linked to them updates automatically:

| Variable Type | Used For |
|---|---|
| `tk.StringVar` | Text entry, labels |
| `tk.IntVar` | Radio buttons, checkboxes |
| `tk.DoubleVar` | Scale widgets |
| `tk.BooleanVar` | Checkbox state |

```python
entryValue = tk.StringVar()
entryValue.set("default text")
userInput["textvariable"] = entryValue
```

### `bind()` for Advanced Events

Use `bind()` to attach a callback to any specific event type:

```python
userInput.bind('<Key-Return>', my_callback)   # Fires on Enter key
```

Common event strings: `<Button-1>` (left click), `<Key-Return>`, `<FocusIn>`, `<FocusOut>`, `<Motion>`

### Reading from and Writing to File

Use Python's built-in file I/O within callback functions to save/load GUI state:

```python
import json

def save_data():
    with open("data.json", "w") as f:
        json.dump(my_dict, f)

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)
```

---

## Lesson 7 — Other Event-Driven Contexts

Event-driven programming extends far beyond GUIs:

### Client-Server Architecture

A **server** listens for incoming **requests** (events) from multiple **clients** and handles each with an appropriate **action** (response). This is conceptually identical to a GUI event handler, but operating over a network.

### Internet of Things (IoT)

IoT devices communicate via:

- **Push architecture:** Sensors push data to a central controller
- **Peer-to-peer:** Devices communicate directly with each other

In all cases, the central node must **listen** for incoming messages, **handle** the data appropriately, and perform some **action** — the core event-driven paradigm applied at hardware scale.

### Key Takeaway

Whenever an application needs to **respond to external events** — user input, network requests, sensor signals — the event-driven paradigm provides a natural and effective design framework. This will be revisited in the context of **concurrent programming** in later weeks.

---

## Week 3 Summary

| Topic | Key Concepts |
|---|---|
| Event-Driven Programming | Events, handlers, callbacks, non-determinism, state |
| UML State Diagrams | Notation, tools, best practices for complex systems |
| Closures | Nested functions retaining enclosing scope after outer function ends |
| Lambda Expressions | Anonymous single-expression functions; closure + lambda for dynamic handlers |
| GUI Design | Wireframes, Nielsen heuristics, colour theory, component selection |
| Tkinter | Widgets, layout managers (pack/grid/place), styling, Canvas |
| Interaction | Callbacks, special variables, bind(), file I/O |
| Beyond GUIs | Client-server, IoT — event-driven paradigm at system scale |
