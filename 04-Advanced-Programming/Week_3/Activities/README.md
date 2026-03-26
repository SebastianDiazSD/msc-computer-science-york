# Week 3: Activities Summary

---

## Overview

Week 3 contains five graded activities and seven inline tasks. Each activity requires forum participation — posting your work and providing constructive feedback to at least two peers. This document summarises each activity, outlines what is expected, and provides a starting-point response that can be developed further before posting.

---

## Activity 1 — Event-Driven Programming (Discussion)

### What to Do

Analyse two systems from an **events and states** perspective. For each, identify the events that occur and explain how those events change the state of objects within the system.

**System A: Making a hot beverage (e.g., coffee)**
**System B: An automated (self-driving) car**

### Forum Post Starting Point

**Making a Coffee — Events and State Changes**

| Event | Object(s) Affected | State Before → State After |
|---|---|---|
| Fill kettle with water | Kettle | Empty → Full |
| Switch kettle on | Kettle | Cold, Off → Heating, On |
| Water reaches 100°C | Kettle | Heating → Boiled; auto-switches off |
| Place cup on surface | Cup | Not in use → In position |
| Add coffee granules | Cup, coffee jar | Empty → Contains coffee; jar level decreases |
| Pour boiling water into cup | Cup, kettle | Dry → Wet; kettle level decreases |
| Add milk / sugar | Cup, milk container | Plain → Modified; containers decrease |
| Stir | Contents of cup | Unmixed → Mixed |
| Beverage ready to drink | Cup | Complete |

**Key observation:** Even a simple domestic process is non-deterministic — the user may skip steps (no sugar), add steps (second cup), or trigger events out of order. This mirrors the challenge of event-driven software design.

**Automated Car — Selected Aspects (Lane Keeping + Emergency Braking)**

| Event | Object(s) Affected | State Change |
|---|---|---|
| Camera detects lane marking | Navigation module | Calibrated → Actively tracking |
| Vehicle drifts towards lane edge | Steering system | Neutral → Correcting |
| Lane correction achieved | Steering system | Correcting → Neutral |
| Proximity sensor detects obstacle | Brake system | Idle → Emergency alert |
| Distance falls below threshold | Brake system | Alert → Active braking |
| Obstacle cleared | Brake system | Active braking → Released |
| Driver overrides | All subsystems | Autonomous → Manual control |

**Key observation:** An autonomous car is a deeply non-deterministic system — events from sensors, user input, and external environment can occur simultaneously and in any sequence. State modelling (as in Activity 2) is essential for safe design.

---

## Activity 2 — Formal Tools: State Diagrams

### What to Do

Produce formal **UML state diagrams** for the two systems from Activity 1. Use a tool such as Lucidchart, Visual Paradigm, StarUML, or pencil/paper scanned.

Diagrams must include: **title, author, date, version number**, and a notation key if any adaptations are made.

### Forum Post Starting Point

**Coffee Making — State Diagram Notes**

The coffee-making process maps cleanly to a sequential state machine with optional branches (milk, sugar). States include: `Idle → KettleFilling → KettleHeating → KettleBoiled → CupPrepping → WaterAdded → IngredientsAdded → Ready`. Guard conditions control optional branches (e.g., `[wantsMilk]`).

**Self-Driving Car — State Diagram Notes**

Due to complexity, I focused on the emergency braking subsystem. Key states: `Cruising → ObstacleDetected → BrakingInitiated → Stopped/ObstacleCleared`. A fork is used to represent simultaneous alerts to the braking system and the driver notification system. A `[driverOverride]` guard transitions all states back to `ManualControl`.

*Diagrams will be attached as image files to the forum post.*

---

## Activity 4 — GUI Design: Digital Address Book Wireframe

### What to Do

**Exercise 1:** Design a wireframe UI for a digital address book application with three data categories: customers/suppliers, company employees, and company holdings. The UI must support search and update actions.

**Exercise 2:** Share your wireframe and explain your design rationale — component choices, grouping logic, and user task flow.

**Exercise 3:** Identify one or two interaction points and create a state machine to represent the interaction.

### Forum Post Starting Point

**Component Selection Rationale**

| Data / Action | Component Choice | Rationale |
|---|---|---|
| Category selection (Suppliers / Employees / Holdings) | `ttk.Notebook` (tabs) | Cleanly separates three distinct record types; user always knows which section they are in |
| Search input | `tk.Entry` + `ttk.Button` | Simple, familiar search-bar pattern |
| Search filter (by name / category / location) | `ttk.Combobox` (dropdown) | Limits input to valid options, reduces errors |
| Results display | `ttk.Treeview` (table) | Handles tabular data natively; sortable columns; search criteria shown first |
| Employee photo | `tk.Canvas` or `tk.Label` with image | Displays photo ID alongside text fields |
| Update form fields | `tk.Entry` widgets + `ttk.Button` (Save) | Standard form pattern, familiar to users |
| Authorisation prompt | Modal `tk.Toplevel` dialog | Interrupts workflow to confirm elevated action |

**Wireframe Layout (described)**

- **Top:** Menubar (File, Edit, View, Reports) + Search bar (Entry + Combobox filter + Search button)
- **Middle:** Three-tab Notebook (Customers/Suppliers | Employees | Holdings)
  - Each tab shows a Treeview results table below the search bar
  - Selecting a row opens a detail panel on the right
- **Right panel:** Read-only label fields + Edit button (visible only if user has permissions)
- **Employee tab only:** Photo ID displayed above detail fields

**User Task Flow (stepping through as a user)**

1. User selects "Customers/Suppliers" tab
2. Types company name into search entry, selects "Company Name" from filter dropdown, clicks Search
3. Treeview populates with results — company name in first column, then contact details
4. User clicks a row — detail panel updates on the right
5. If user is the registered primary contact for that company, the Edit button appears
6. User clicks Edit — fields become editable Entry widgets; Save and Cancel buttons appear
7. User saves — fields revert to read-only; confirmation label shows "Updated successfully"

**State Machine — Search Interaction**

States: `Idle → SearchInputActive → SearchSubmitted → ResultsDisplayed → RecordSelected → [EditMode | ReadOnly]`

Guard conditions:
- `[isPrimaryContact]` → Edit button visible
- `[hasAuthorisation]` → Holdings edit permitted
- `[inputEmpty]` → Search button disabled

---

## Activity 5 — Implementing Interaction

### What to Do

**Exercise 1:** Extend the provided `EventHandlers.ipynb` (Computing Definitions app):

1. Replace the two placeholder definitions with **real computing terms**
2. Add the ability for users to **add their own terms** (Entry + Submit button)
3. Add a **Save button** that writes all definitions to a file, loaded again on restart

**Exercise 2:** Using Tkinter, build part of the Activity 4 Address Book wireframe to demonstrate interaction.

**Exercise 3:** Identify potential errors in the Address Book application and document how they should be handled.

### Forum Post Starting Point

**Exercise 1 — Extended Definitions App**

Real definitions added:

```python
computer_defs = {
    'algorithm': 'A finite set of step-by-step instructions that solves a specific problem or performs a computation.',
    'abstraction': 'The process of hiding complex implementation details and exposing only the necessary functionality to the user.',
}
```

Add-your-own functionality requires:
- A `tk.Entry` for the new term
- A `tk.Entry` or `tk.Text` for the new definition
- A `ttk.Button("Add")` calling `add_def()` callback
- `add_def()` reads both fields, validates they are non-empty, and inserts into `computer_defs`

Save/load using JSON:

```python
import json

def save_defs():
    with open("definitions.json", "w") as f:
        json.dump(computer_defs, f, indent=2)

def load_defs():
    try:
        with open("definitions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {'algorithm': '...', 'abstraction': '...'}  # defaults

computer_defs = load_defs()
```

**JSON** was chosen over a plain text file because the dictionary structure maps directly to JSON objects, making serialisation and deserialisation trivial and eliminating the need for custom parsing.

**Exercise 3 — Error Handling: Address Book**

| Erroneous Input | System Response | User Message |
|---|---|---|
| Empty search field submitted | Prevent search; highlight field in red | "Please enter a search term before submitting." |
| Search returns no results | Display empty table with message | "No records found matching your search." |
| User edits a field with invalid email format | Disable Save; highlight field | "Please enter a valid email address." |
| User without permissions attempts to edit holdings | Edit button hidden; if forced via shortcut, show modal | "You do not have authorisation to edit company holdings." |
| File not found on load | Load empty default dictionary | "No saved definitions found. Starting with defaults." |
| File corrupted (JSON parse error) | Catch exception; load defaults | "Saved file could not be read. Defaults loaded." |

**Events captured and widgets used:**

- `<Key-Return>` on search Entry → triggers search (keyboard-friendly, intuitive)
- `<Button-1>` on Treeview row → loads record into detail panel (click-to-select, standard behaviour)
- `ttk.Button command` → Save, Edit, Add Definition (explicit action buttons, clear affordance)
- `tk.StringVar.trace()` → real-time validation of email field format as user types

---

## Inline Tasks Summary

| Task | Brief |
|---|---|
| **Task 1** | Investigate `nonlocal` vs `global` scope in Python using the `outerFun()` code sample |
| **Task 3** | Identify GUI components beyond the nine listed; share screenshots and evaluate effectiveness |
| **Task 4** | Replicate the example wireframe from Figure 2 in Pencil or Lucidchart; write a short tool review |
| **Task 5** | Write Tkinter code samples for: Checkbutton, Radiobutton, Listbox, Message, Scale, Text, Spinbox |
| **Task 6** | Reuse Task 5 components to demonstrate all three layout managers: pack(), grid(), place() |
| **Task 7** | Implement the wireframe layouts from the module document using Tkinter |

---

*Ground2Tech Engineering — MSc Computer Science, University of York*
*github.com/SebastianDiazSD*
