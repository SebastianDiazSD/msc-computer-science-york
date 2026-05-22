# Lesson 2 – Data Visualisation
**Core text:** McKinney (2017), *Python for Data Analysis*, Chapter 9  
**Key libraries:** `matplotlib` (https://matplotlib.org/), `seaborn` (https://seaborn.pydata.org/)

## Why Visualise?
Visualisation is not just for presenting final results — it is a tool used **throughout** the analysis process:
- **During cleaning**: scatter plots reveal outliers; histograms show skewed distributions
- **During wrangling**: line charts expose missing time periods; heatmaps reveal correlation patterns
- **For presentation**: bar charts, pie charts, and line graphs communicate findings to non-technical audiences

The type of chart chosen must match the type of data and the message being conveyed.

---

## 1. Chart Types and When to Use Them

| Chart type | Best for | Example |
|---|---|---|
| **Bar chart** | Comparing discrete categories | Monthly sales by store |
| **Pie chart** | Parts of a whole (≤6 categories) | Market share breakdown |
| **Line graph** | Trends over time (continuous) | Sales over 12 months |
| **Histogram** | Distribution of a single variable | Distribution of income values |
| **Scatter plot** | Relationship between two numerical variables | Height vs weight |
| **Box plot** | Distribution spread, outliers, quartiles | Salary distribution by department |
| **Heatmap** | Correlation matrix, 2D frequency | Correlation between features |

> Rule of thumb: **Bar** for categories, **Line** for time, **Scatter** for relationships, **Histogram** for distributions.

---

## 2. Matplotlib — Low-Level, High Control

Matplotlib is the foundation of Python plotting. It gives you full control over every element of the figure. The standard import convention is:

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

### Basic anatomy of a Matplotlib figure
```
Figure
└── Axes (the actual plot area)
    ├── Title
    ├── x-axis label, y-axis label
    ├── x-ticks, y-ticks
    └── Plot elements (lines, bars, patches)
```

### Creating figures and subplots
```python
# Single plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Multiple subplots in a grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].plot(x, y1, label='Store L1')
axes[0, 1].bar(months, sales)
axes[1, 0].hist(data, bins=20)
axes[1, 1].scatter(x, y)
plt.tight_layout()   # prevents overlap
plt.show()
```

### Common plot types
```python
# Line plot
ax.plot(x, y, color='blue', linewidth=2, linestyle='--', marker='o', label='L1')

# Bar chart
ax.bar(categories, values, color='steelblue', edgecolor='black')

# Histogram
ax.hist(data, bins=20, color='salmon', edgecolor='black', density=True)

# Scatter plot
ax.scatter(x, y, c='green', s=50, alpha=0.6)

# Pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
```

### Formatting
```python
ax.set_title('Monthly Sales by Store', fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Sales (£)')
ax.legend(loc='upper left')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(0, 12)
ax.set_ylim(0, 800)

# Rotate x-tick labels (useful for month names)
plt.xticks(rotation=45, ha='right')
```

### Saving figures
```python
fig.savefig('sales_chart.png', dpi=150, bbox_inches='tight')
fig.savefig('sales_chart.pdf')   # publication-quality vector format
```

### Plotting directly from Pandas
Pandas DataFrames have a built-in `.plot()` method that wraps Matplotlib:
```python
df.plot(kind='line', figsize=(10, 5), title='Store Sales')
df.plot(kind='bar')
df.plot(kind='hist', bins=15)
df.plot(kind='scatter', x='month_num', y='sales')
plt.show()
```

---

## 3. Seaborn — High-Level, Statistics-Oriented

Seaborn is built on top of Matplotlib and is designed to produce statistically meaningful visualisations with minimal code. It natively accepts Pandas DataFrames and uses column names directly.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Key Seaborn plots

```python
# Distribution plot (histogram + KDE)
sns.histplot(data=df, x='income', kde=True, bins=30)

# Box plot
sns.boxplot(data=df, x='job_title', y='income', palette='Set2')

# Violin plot (box + distribution shape)
sns.violinplot(data=df, x='education', y='income')

# Bar plot with error bars
sns.barplot(data=df, x='city', y='sales', ci=95)

# Scatter plot with regression line
sns.regplot(x='x_col', y='y_col', data=df)

# Heatmap (correlation matrix)
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

# Pair plot — scatter matrix of all numerical columns
sns.pairplot(df, hue='category_column')
```

### `FacetGrid` — multiple plots by category
```python
g = sns.FacetGrid(df, col='city', row='year', height=4)
g.map(sns.histplot, 'income')
g.add_legend()
plt.show()
```

### Seaborn themes
```python
sns.set_theme(style='whitegrid')    # clean grid background
sns.set_theme(style='darkgrid')     # dark background
sns.set_theme(style='ticks')        # minimal
sns.set_palette('husl')             # colour palette
```

---

## 4. Matplotlib vs Seaborn — When to Use Each

| Aspect | Matplotlib | Seaborn |
|---|---|---|
| Control level | Full — every element configurable | High-level — sensible defaults |
| Code volume | More verbose | Concise |
| Statistical plots | Manual | Built-in (CI, KDE, regression) |
| Data input | Arrays | Prefers Pandas DataFrames |
| Best for | Custom, publication figures, GUI integration | Exploratory data analysis |
| Built on | — | Matplotlib |

**Rule of thumb**: Use Seaborn for quick exploratory visualisation; use Matplotlib for precise customisation and GUI embedding.

---

## 5. Embedding Matplotlib in a Tkinter GUI

Matplotlib provides a Tkinter-compatible backend via `FigureCanvasTkAgg`:

```python
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = tk.Tk()
root.title("Sales Dashboard")

# Create a Matplotlib figure
fig = Figure(figsize=(8, 5), dpi=100)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [100, 200, 150, 300])
ax.set_title('Monthly Sales')

# Embed in tkinter Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Optional: add navigation toolbar (zoom, pan, save)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack()

root.mainloop()
```

### Dynamic updates (live data)
```python
def update_chart(new_data):
    ax.clear()
    ax.plot(new_data)
    canvas.draw()   # refresh the widget
```

---

## Key Takeaways
- Choose the chart type based on **data type** and **message**, not aesthetics.
- **Matplotlib** gives maximum control; use it when you need precision or GUI integration.
- **Seaborn** is faster for exploratory work; its statistical plots (boxplot, pairplot, heatmap) reveal distribution and correlation patterns with minimal code.
- Visualisation is **iterative** — it informs cleaning and wrangling decisions, not just final presentation.
- Pandas `.plot()` is a convenient shortcut for quick charts without switching to Matplotlib syntax.
