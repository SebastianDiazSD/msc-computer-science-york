# Lesson 1 – NumPy

## What is NumPy?
NumPy (Numerical Python) is a foundational library for scientific computing in Python. Its core object is the **ndarray** (n-dimensional array), which provides fast, memory-efficient storage and operations on homogeneous numerical data.

NumPy is implemented in C, which gives it a significant speed advantage over standard Python loops for numerical computation.

---

## Key Concepts

### 1. The ndarray
- All elements must be **the same data type** (unlike Python lists).
- Data is stored in a **contiguous block of memory**, which allows efficient access and computation.
- The default type when no dtype is specified is **`float64`**.

```python
import numpy as np

a = np.array([1, 2, 3])          # 1D array
b = np.array([[1, 2], [3, 4]])   # 2D array (matrix)
print(a.dtype)   # int64
print(b.shape)   # (2, 2)
```

### 2. Creating Arrays

| Method | Description |
|---|---|
| `np.array([...])` | From a Python list |
| `np.zeros((m, n))` | Array of zeros |
| `np.ones((m, n))` | Array of ones |
| `np.arange(n)` | Sequential integers 0 to n-1 |
| `np.random.randn(m, n)` | Random values from standard normal distribution |
| `np.random.randint(low, high, size)` | Random integers |

### 3. Vectorisation
Operations are applied **element-wise** to every element in the array without an explicit loop. This is called **vectorisation** and is one of NumPy's main performance advantages.

```python
arr = np.array([1.0, 4.0, 9.0, 16.0])
print(np.sqrt(arr))   # [1. 2. 3. 4.]
```

### 4. Broadcasting
**Broadcasting** is NumPy's mechanism for performing arithmetic between arrays of **different shapes**. The smaller array is "broadcast" across the larger one.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr + 10   # 10 is broadcast to every element
```

Rules: NumPy compares shapes element-wise from the trailing dimensions. Dimensions are compatible if they are equal or one of them is 1.

### 5. Universal Functions (ufuncs)
ufuncs are functions that operate element-wise on arrays:
- **Unary** (single array): `np.sqrt()`, `np.exp()`, `np.abs()`, `np.log()`
- **Binary** (two arrays): `np.add()`, `np.multiply()`, `np.maximum()`

### 6. Indexing and Slicing

```python
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

arr[1, 2]       # 60 — row 1, col 2
arr[0:2, 1:3]   # rows 0-1, cols 1-2
arr[[0, 2], :]  # rows 0 and 2 (fancy indexing)
arr[:, [0, 2]]  # columns 0 and 2
```

> ⚠️ **Important**: In NumPy, slices create **views** (not copies). Modifying a slice modifies the original array. Use `.copy()` to avoid this.

### 7. Boolean Indexing

```python
data = np.array([10, 25, 5, 30, 15])
mask = data > 15
print(data[mask])   # [25 30]
```

### 8. Type Casting
When casting from `float` to `int`, values are **truncated** (not rounded):

```python
arr = np.array([1.7, 2.9, 3.1])
print(arr.astype(int))   # [1 2 3]
```

### 9. Matrix Operations

| Operation | Code | Notes |
|---|---|---|
| Element-wise product | `A * B` | Default `*` operator |
| Dot product | `np.dot(A, B)` | Matrix multiplication |
| Column-wise product | `np.cumprod(A, axis=0)` | `axis=0` = column |
| Row-wise product | `np.cumprod(A, axis=1)` | `axis=1` = row |

### 10. Statistical Functions

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(arr)           # 21
np.sum(arr, axis=0)   # column sums: [5, 7, 9]
np.sum(arr, axis=1)   # row sums: [6, 15]
np.mean(arr)          # 3.5
np.std(arr)           # standard deviation
np.min(arr)           # minimum value
np.max(arr)           # maximum value
np.sort(arr)          # sort (along last axis by default)
```

### 11. Sorting Algorithms in `numpy.sort()`
NumPy's `sort()` supports three algorithms via the `kind` parameter:

| Algorithm | `kind` | Best For |
|---|---|---|
| Quicksort | `'quicksort'` (default) | General purpose, large arrays |
| Mergesort | `'mergesort'` | Stable sort, linked structures |
| Heapsort | `'heapsort'` | Worst-case O(n log n) guarantee |
| Timsort | `'stable'` | Real-world data with partial ordering |

**When to use which:**
- **Quicksort**: Best average-case performance O(n log n), good for large, uniformly distributed datasets. Not stable.
- **Mergesort/Timsort**: Use when a stable sort is needed (preserves relative order of equal elements). Good for partially sorted data.
- **Heapsort**: Use when memory is constrained (in-place) and worst-case guarantees are needed.

### 12. Loading CSV Data

```python
data = np.genfromtxt('file.csv', delimiter=',')           # no headers
data = np.genfromtxt('file.csv', delimiter=',', skip_header=1)  # skip header row
```

---

## Benefits vs Limitations

| Benefits | Limitations |
|---|---|
| Very fast (C implementation) | Homogeneous data only (same dtype) |
| Memory efficient (contiguous blocks) | Less intuitive for labelled/tabular data |
| No type-checking overhead | No built-in support for mixed data types |
| Rich mathematical library | Harder to work with missing values |
| Broadcasting simplifies operations | Less readable code for non-numerical tasks |

---

## Key Takeaways
- NumPy is ideal for **homogeneous numerical data** and mathematical operations.
- Use **vectorisation** instead of loops wherever possible.
- Be careful with **views vs copies** when slicing.
- For labelled, tabular, or heterogeneous data → prefer **Pandas**.