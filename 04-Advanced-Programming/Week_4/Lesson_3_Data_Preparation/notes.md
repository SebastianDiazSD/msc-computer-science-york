# Lesson 3 – Preparing for Data Analysis

## Why Data Cleaning Matters
Raw data is rarely analysis-ready. It typically contains missing values, inconsistencies, duplicates, and sensitive information. Cleaning and preparing data before analysis is critical to ensure valid, reproducible results. This stage is often called **data wrangling** or **data munging**.

---

## Common Data Quality Issues

| Issue | Example |
|---|---|
| Missing values | `NaN`, `null`, `none`, `""`, `0`, `" "` |
| Inconsistent representation | Mixed null symbols (`none`, `null`, `0`, `""`) |
| Duplicate records | Same customer appearing twice |
| Sensitive/identifiable data | Names, emails that need anonymisation |
| Inconsistent formats | Dates, capitalisation, units |

---

## Step-by-Step Data Cleaning Process

### 1. Explore the Data First
Before cleaning, understand what you have:
```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.shape)         # rows × columns
print(df.head())        # first 5 rows
print(df.info())        # dtypes, non-null counts
print(df.isnull().sum()) # null count per column
print(df.duplicated().sum()) # duplicate count
```

### 2. Standardise Null Values
Different symbols may represent "no data": `none`, `null`, `0`, `""`, `" "`. Replace them all with a single standard (`NaN` is the Pandas standard):

```python
null_symbols = ['none', 'null', '0', '', ' ', 'NaN', 'N/A']
df.replace(null_symbols, pd.NA, inplace=True)

# Or when loading:
df = pd.read_csv('data.csv', na_values=['none', 'null', '0', ''])
```

> Be careful with `0` — only replace with `NaN` if 0 is not a valid data value in that column.

### 3. Remove Duplicates
```python
df.duplicated().sum()              # count duplicates
df.drop_duplicates(inplace=True)   # remove exact duplicates
df.drop_duplicates(subset=['email']) # deduplicate on specific columns
```

### 4. Drop Rows with Missing Critical Fields
```python
# Drop rows where any of these columns are null
critical_cols = ['first_name', 'last_name', 'email']
df.dropna(subset=critical_cols, inplace=True)
```

### 5. Anonymise Sensitive Data
When data is used for analysis, personal identifiers (names, emails) should be replaced with a unique, non-identifiable key:

```python
# Generate a unique ID for each row
df.insert(0, 'customer_id', ['CUST_{:04d}'.format(i) for i in range(1, len(df)+1)])

# Drop the identifying columns
df.drop(columns=['first_name', 'last_name'], inplace=True)
```

Alternatively use a hash for reproducibility:
```python
import hashlib
df['customer_id'] = df['email'].apply(
    lambda x: hashlib.md5(str(x).encode()).hexdigest()[:8].upper() if pd.notna(x) else None
)
```

### 6. Export the Cleaned Data
```python
df.to_csv('cleaned_data.csv', index=False)
```

---

## Selecting Appropriate Structures

| Scenario | Best structure |
|---|---|
| Pure numerical operations | NumPy ndarray |
| Tabular data with labels | Pandas DataFrame |
| Mixed types, missing values | Pandas DataFrame |
| Simple 1D labelled data | Pandas Series |

---

## Common Pandas Cleaning Methods Summary

| Method | Purpose |
|---|---|
| `df.isnull()` | Boolean mask of null values |
| `df.dropna(subset=[...])` | Drop rows missing specific columns |
| `df.fillna(value)` | Fill nulls with a value |
| `df.replace(old, new)` | Replace specific values |
| `df.drop_duplicates()` | Remove duplicate rows |
| `df.drop(columns=[...])` | Remove columns |
| `df.rename(columns={...})` | Rename columns |
| `df.to_csv(...)` | Export to CSV |

---

## Key Takeaways
- **Always explore data before cleaning** — understand what the issues are first.
- **Standardise null representations early** — inconsistent nulls cause silent errors downstream.
- **Anonymise before sharing or storing** — remove names and emails, replace with IDs.
- **Document every cleaning decision** — what was removed and why (important for reproducibility and ethics).
- The appropriate data structure depends on the data's nature: NumPy for homogeneous numerical data, Pandas for heterogeneous or labelled tabular data.