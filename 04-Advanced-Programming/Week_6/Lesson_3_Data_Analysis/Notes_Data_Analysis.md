# Lesson 3 – Data Analysis
**Core text:** McKinney (2017), *Python for Data Analysis*, Chapter 10

## The Data Analysis Pipeline

This lesson introduces a complete framework for data analysis. Rather than treating the individual Pandas/NumPy functions as isolated tools, the pipeline provides a structured flow from raw data to presented results:

```
Information Need → Gather Data → Clean Data → Reshape Data → Analyse Data → Present Data
```

| Stage | What happens | Key tools |
|---|---|---|
| **Information Need** | Define what question you are answering | — |
| **Gather Data** | Load from CSV, database, API | `pd.read_csv()`, `pd.read_json()` |
| **Clean Data** | Handle nulls, duplicates, inconsistencies | `dropna()`, `fillna()`, `replace()` |
| **Reshape Data** | Merge, pivot, stack, groupby | `merge()`, `pivot()`, `groupby()` |
| **Analyse Data** | Counts, statistics, correlations | `groupby()`, `agg()`, `corr()` |
| **Present Data** | Charts, tables, GUI | Matplotlib, Seaborn, tkinter |

The process is **not linear** — visualisation during analysis can reveal the data needs further cleaning or reshaping.

---

## 1. The Split-Apply-Combine Pattern

The core idea of data analysis is described as **split-apply-combine**:
1. **Split** the data into groups based on some criterion
2. **Apply** a function (sum, mean, count, custom) to each group independently
3. **Combine** the results back into a single output

This is implemented in Pandas via `groupby()`.

---

## 2. `groupby()` — The Core Analysis Tool

```python
import pandas as pd
import numpy as np

df = pd.read_csv('sales.csv', index_col=0)

# Split by store, apply sum to each group
df.groupby('store')['sales'].sum()

# Group by multiple keys
df.groupby(['store', 'month'])['sales'].sum()

# Apply multiple aggregations at once
df.groupby('store')['sales'].agg(['sum', 'mean', 'max', 'min', 'count'])
```

### Iterating over groups
```python
for name, group in df.groupby('store'):
    print(f"Store: {name}")
    print(group.head())
```

### Groupby with custom functions
```python
# Custom aggregation using lambda
df.groupby('store')['sales'].agg(lambda x: x.max() - x.min())

# Named aggregation (Pandas ≥0.25)
df.groupby('store').agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean'),
    peak_month=('sales', 'idxmax')
)
```

### `transform()` vs `agg()`

| Method | Output shape | Use case |
|---|---|---|
| `agg()` | One row per group | Compute group-level summary |
| `transform()` | Same shape as input | Add group stat back to original rows |

```python
# Add each store's mean back to the original DataFrame (for % of average calculation)
df['store_mean'] = df.groupby('store')['sales'].transform('mean')
df['pct_of_mean'] = df['sales'] / df['store_mean'] * 100
```

---

## 3. Aggregation Functions

```python
# Built-in aggregation methods on groupby
g = df.groupby('store')['sales']

g.sum()       # Total per group
g.mean()      # Average per group
g.median()    # Median per group
g.std()       # Standard deviation per group
g.var()       # Variance per group
g.min()       # Minimum per group
g.max()       # Maximum per group
g.count()     # Non-null count per group
g.size()      # Total count including nulls
g.first()     # First value per group
g.last()      # Last value per group
g.cumsum()    # Running total
g.describe()  # Count, mean, std, min, quartiles, max — all at once
```

---

## 4. Pivot Tables — Groupby as a Table

`pivot_table()` is essentially `groupby()` with a table layout:

```python
pivot = pd.pivot_table(
    df,
    values='sales',
    index='store',        # row groups
    columns='month',      # column groups
    aggfunc='sum',        # what to compute per cell
    fill_value=0          # replace NaN with 0
)
print(pivot)
```

Add row/column totals:
```python
pivot = pd.pivot_table(df, values='sales', index='store', columns='month',
                       aggfunc='sum', margins=True, margins_name='Total')
```

---

## 5. Correlation and Covariance

```python
# Correlation matrix — all numerical columns
corr_matrix = df.corr()

# Correlation between two specific columns
df['sales'].corr(df['month_num'])

# Covariance
df.cov()
```

---

## 6. Cross-tabulation

`pd.crosstab()` counts frequency combinations between categorical variables:

```python
pd.crosstab(df['store'], df['region'])
# Normalise to percentages
pd.crosstab(df['store'], df['region'], normalize='index')
```

---

## 7. Apply — Custom Functions Over Groups

`apply()` passes each group as a DataFrame to a custom function:

```python
def top_n(group, n=3):
    """Return the n highest-sales months for a given store."""
    return group.nlargest(n, 'sales')

df.groupby('store').apply(top_n, n=3)
```

---

## 8. Full Example: Sales Data Pipeline

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load
df = pd.read_csv('sales.csv', index_col=0)

# 2. Reshape — stack to long format for groupby
df_long = df.stack().reset_index()
df_long.columns = ['store', 'month', 'sales']

# 3. Analyse — total and average per store
summary = df_long.groupby('store')['sales'].agg(
    total='sum',
    average='mean',
    best_month='idxmax'
)
print(summary)

# 4. Analyse — monthly average across all stores
monthly = df_long.groupby('month')['sales'].mean()

# 5. Present
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
summary['total'].plot(kind='bar', ax=axes[0], title='Total Sales by Store', color='steelblue')
monthly.plot(kind='line', ax=axes[1], title='Average Monthly Sales', marker='o')
plt.tight_layout()
plt.show()
```

---

## Key Takeaways
- The data analysis pipeline — Information Need → Gather → Clean → Reshape → Analyse → Present — is the framework that ties all the individual functions together.
- **Split-apply-combine** via `groupby()` is the core pattern for analytical computation in Pandas.
- `agg()` reduces each group to a summary; `transform()` keeps the original shape (useful for computing percentage-of-group).
- `pivot_table()` is `groupby()` displayed as a cross-tabulation — use it when you want a matrix view.
- Always start from the **information need** — choosing the right grouping key and aggregation function depends on what question you are trying to answer.
