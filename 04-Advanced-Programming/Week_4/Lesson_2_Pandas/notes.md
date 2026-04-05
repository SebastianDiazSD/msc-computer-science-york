# Lesson 2 – Pandas

## What is Pandas?
Pandas is a Python library built on top of NumPy that provides high-level data structures and tools for data analysis. Its two primary structures are the **Series** and the **DataFrame**, both of which support labelled indexing, mixed data types, and built-in handling of missing values.

---

## Key Data Structures

### 1. Series
A **one-dimensional** labelled array. Think of it as a dict-like structure: it holds two aligned arrays — one for **values** and one for **labels (index)**.

```python
import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s['b'])    # 20
print(s[1])      # 20 (positional — only if no ambiguity)
```

> ⚠️ When labels are **numerical**, positional indexing can be ambiguous. Pandas will use label-based indexing by default.

**Slicing in Pandas is inclusive at both ends** (unlike Python lists where the endpoint is excluded):
```python
s['a':'c']   # returns a, b, c — all three
```

#### Non-unique labels
If a label is not unique, indexing with that label returns a **Series** (multiple values). If it is unique, it returns a **scalar**. This means code may need to handle both types.

### 2. DataFrame
A **two-dimensional** table with labelled rows and columns. Each column can hold a different data type (heterogeneous data).

```python
df = pd.DataFrame({
    'Name':  ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78],
    'Grade': ['B', 'A', 'C']
})
```

> A DataFrame is **not** a 2D NumPy array — it is a collection of Series (one per column), each sharing the same row index.

---

## Indexing

| Method | Type | Inclusive endpoint |
|---|---|---|
| `df['col']` | Column selection | — |
| `df.loc['row']` | **Label-based** | Yes |
| `df.iloc[0]` | **Position-based** | No (standard Python) |
| `df.loc['a':'c']` | Label slice | Yes |
| `df.iloc[0:3]` | Position slice | No |

```python
df.loc['L3', 'Nov-18']    # label-based
df.iloc[0, 7]             # position-based
df.loc[:, ['Nov-18', 'Feb-19']]   # all rows, specific columns
```

---

## Creating Series and DataFrames

Pandas objects can be created from:
- `list[]`
- `tuple()`
- `dict{}`
- NumPy `ndarray`
- Combinations of the above

```python
s = pd.Series(np.arange(5.))           # from NumPy
df = pd.DataFrame(np.random.randn(4, 3), columns=['A','B','C'])
```

---

## Key Operations

### Sorting
```python
df.sort_values('column_name')                 # ascending by default
df.sort_values('column_name', ascending=False)
df.sort_index()                               # sort by row index
```

### Ranking
```python
s.rank()                    # default: average for ties
s.rank(method='first')      # first occurrence gets lower rank
s.rank(method='average')    # tied values get the mean rank
# Note: 'last' is NOT a valid method
```

**Example**: Ranking [9, 4, 3, 4] from highest:
- Sorted: 9(1st), 4(2nd), 4(3rd), 3(4th)
- `method='average'`: the two 4s get rank **2.5**
- `method='first'`: the first 4 gets rank **2**, second gets **3**

### Missing Values
```python
df.isnull()          # Boolean mask of missing values
df.dropna()          # Drop rows with any NaN
df.dropna(axis=1)    # Drop columns with any NaN
df.fillna(value)     # Replace NaN with a specified value
df.fillna(method='ffill')  # Forward fill
```

When converting data from other structures, any missing values are replaced with **NaN** by default.

### Dropping Data
```python
df.drop('row_label')          # drop a row
df.drop('col_label', axis=1)  # drop a column
df.drop('col', axis=1, inplace=True)  # permanent deletion
```

> ⚠️ Data is only **permanently deleted** when `inplace=True` is set. The default is `inplace=False` (returns a new object).

### Applying Functions
Both **NumPy ufuncs** and **lambda expressions** can be used with Pandas:

```python
df.apply(np.sqrt)              # NumPy ufunc
df.apply(lambda x: x * 2)     # lambda
df['col'].apply(lambda x: x if x > 0 else 0)
```

---

## Statistical Functions

```python
df.mean()           # mean per column
df.sum()            # sum per column
df.describe()       # count, mean, std, min, max, quartiles
df.pct_change()     # percentage change between consecutive rows
df.cumsum()         # cumulative sum
```

---

## Loading and Exporting CSV

```python
df = pd.read_csv('file.csv', index_col=0)   # first column as index
df.to_csv('output.csv')
```

---

## Pandas vs NumPy — When to Use Each

| Feature | NumPy | Pandas |
|---|---|---|
| Data type | Homogeneous (all same) | Heterogeneous (mixed types) |
| Labels | Integer index only | Custom labels (strings, etc.) |
| Missing values | No built-in support | Native `NaN` handling |
| Performance | Faster for pure maths | Slightly overhead but more flexible |
| Best for | Matrix math, simulations | Tabular/business data |

**Rule of thumb**: Use NumPy when doing pure numerical computation on homogeneous data. Use Pandas when working with labelled, tabular, or mixed-type data (like a spreadsheet or database table).

---

## Key Takeaways
- A **Series** is like a labelled 1D array; a **DataFrame** is a labelled 2D table.
- Pandas slicing with `.loc` is **inclusive** at both ends — different from standard Python.
- Non-unique labels can cause `Series` to be returned instead of scalars — handle both types in code.
- Data is only permanently changed when `inplace=True`.
- NumPy ufuncs and lambda functions work seamlessly with Pandas structures.