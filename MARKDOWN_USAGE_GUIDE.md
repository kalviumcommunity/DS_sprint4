# Milestone 6: Writing Markdown for Headings, Lists, and Code Blocks in Notebooks

**Estimated Reading Time:** 20 minutes  
**Difficulty Level:** Beginner-Intermediate  
**Focus Area:** Documentation, clear communication, notebook structure, readability  

---

## Table of Contents

1. [Overview](#overview)
2. [Why Markdown Matters](#why-markdown-matters)
3. [Markdown Basics](#markdown-basics)
4. [Headings and Hierarchy](#headings-and-hierarchy)
5. [Lists: Ordered and Unordered](#lists-ordered-and-unordered)
6. [Inline Code and Code Blocks](#inline-code-and-code-blocks)
7. [Markdown Cell Placement](#markdown-cell-placement)
8. [Professional Notebook Structure](#professional-notebook-structure)
9. [Common Mistakes and Best Practices](#common-mistakes-and-best-practices)
10. [Real-World Example](#real-world-example)

---

## Overview

A Jupyter Notebook is more than code—it's a **communication document**. The code executes your analysis; the Markdown explains it.

### What This Milestone Teaches

By completing this milestone, you'll demonstrate:
- Clear heading hierarchy to organize sections
- Effective use of lists (ordered and unordered)
- Inline code and code block formatting
- Logical placement of Markdown for readability
- Professional documentation standards

### Why This Matters

**Without good Markdown:**
- ❌ Readers can't follow the notebook's logic
- ❌ Code appears isolated without context
- ❌ Collaborators waste time understanding intent
- ❌ Notebooks look unprofessional and hard to maintain

**With good Markdown:**
- ✓ Clear structure guides readers through analysis
- ✓ Explanations clarify why code is written
- ✓ Collaborators understand the workflow immediately
- ✓ Notebooks appear professional and intentional

---

## Why Markdown Matters

### The Two Languages of Notebooks

A professional Jupyter Notebook uses two complementary languages:

| Language | Purpose | Example |
|----------|---------|---------|
| **Markdown** | Explain, document, structure | "# Data Cleaning" or "Load CSV file here" |
| **Python (Code)** | Execute, compute, transform | `df = pd.read_csv('data.csv')` |

Neither is complete without the other:
- **Code alone**: Readers see `df = pd.read_csv('file.csv')` but don't know why or what comes next
- **Markdown alone**: Readers see explanations but can't run anything

### Markdown as a Reader's Guide

Think of Markdown as **roadmap signage**:

**Without signage:**
```
→ →→ ← → → →  ← → ← →
```
(Readers are lost!)

**With signage:**
```
↓
SECTION 1: Data Loading
↓ Load the CSV file from S3
↓
SECTION 2: Data Cleaning  
↓ Remove NaN values, fix types
↓
SECTION 3: Analysis
↓ Compute statistics and visualize
```

This is what good Markdown does in notebooks.

---

## Markdown Basics

### What Is Markdown?

Markdown is **simple text formatting** that's human-readable and converts to formatted output. In notebooks, it renders as styled text, headings, lists, and more.

### Basic Syntax Reference

| Element | Markdown | Renders As |
|---------|----------|-----------|
| **Bold** | `**bold text**` | **bold text** |
| **Italic** | `*italic*` or `_italic_` | *italic* |
| **Bold + Italic** | `***bold italic***` | ***bold italic*** |
| **Strikethrough** | `~~strikethrough~~` | ~~strikethrough~~ |
| **Monospace (inline code)** | `` `code` `` | `code` |

---

## Headings and Hierarchy

### The Six Levels of Headings

Markdown supports 6 heading levels using `#` symbols:

```markdown
# Heading Level 1 (Main title)
## Heading Level 2 (Major section)
### Heading Level 3 (Subsection)
#### Heading Level 4 (Sub-subsection)
##### Heading Level 5 (Minor section)
###### Heading Level 6 (Very minor section)
```

### Hierarchy Visualization

```
# Main Title (Level 1)
    ├── ## Section A (Level 2)
    │   ├── ### Subsection A1 (Level 3)
    │   └── ### Subsection A2 (Level 3)
    ├── ## Section B (Level 2)
    │   ├── ### Subsection B1 (Level 3)
    │   └── ### Subsection B2 (Level 3)
    └── ## Section C (Level 2)
        └── ### Subsection C1 (Level 3)
```

### Professional Heading Practices

**✓ Good: Clear hierarchy**
```markdown
# Data Analysis Notebook

## Part 1: Data Loading
### Step 1: Read CSV File
### Step 2: Inspect Data

## Part 2: Data Cleaning
### Step 1: Remove Duplicates
### Step 2: Fix Missing Values

## Part 3: Analysis
### Step 1: Statistical Summary
### Step 2: Visualization
```

**✗ Bad: Confusing or missing hierarchy**
```markdown
# Data Analysis

Data loading
Data Cleaning
Analysis
Statistical summary
Visualization
```

### Hierarchy Rules

1. **Start with `#` (Level 1)** for the main title
2. **Use `##` (Level 2)** for major sections
3. **Use `###` (Level 3)** for subsections within sections
4. **Don't skip levels**: Don't jump from `#` to `###` (go through `##`)
5. **Be consistent**: Use the same level for parallel concepts

### Real Example: Data Science Notebook

```markdown
# Customer Churn Analysis

## 1. Introduction
### 1.1 Problem Statement  
### 1.2 Data Overview

## 2. Data Preparation
### 2.1 Load Data
### 2.2 Exploratory Data Analysis
### 2.3 Data Cleaning

## 3. Feature Engineering
### 3.1 Create New Features
### 3.2 Encode Categorical Variables

## 4. Model Training
### 4.1 Train Models
### 4.2 Evaluate Performance

## 5. Results and Recommendations
### 5.1 Key Findings
### 5.2 Business Recommendations
```

---

## Lists: Ordered and Unordered

### Unordered Lists (Bullets)

Use unordered lists when **order doesn't matter**:

**Markdown:**
```markdown
## Data Requirements

- Python 3.8 or higher
- pandas library
- numpy library
- matplotlib for visualization
```

**Renders as:**
- Python 3.8 or higher
- pandas library
- numpy library
- matplotlib for visualization

### Nested Unordered Lists

```markdown
## Project Structure

- Data Folder
  - Raw data
  - Processed data
- Code Folder
  - Data loading scripts
  - Analysis scripts
- Results Folder
  - Outputs
  - Visualizations
```

### Ordered Lists (Numbered)

Use ordered lists when **order matters** or **you're showing steps**:

**Markdown:**
```markdown
## Data Processing Pipeline

1. Read the CSV file from disk
2. Remove duplicate rows
3. Handle missing values
4. Verify data types are correct
5. Export cleaned data
```

**Renders as:**
1. Read the CSV file from disk
2. Remove duplicate rows
3. Handle missing values
4. Verify data types are correct
5. Export cleaned data

### Nested Ordered Lists

```markdown
## Machine Learning Workflow

1. Data Preparation
   1. Load raw data
   2. Split into train/test sets
   3. Normalize numerical features
2. Model Selection
   1. Test multiple algorithms
   2. Compare performance metrics
   3. Choose best model
3. Model Training
   1. Fit selected model
   2. Optimize hyperparameters
   3. Evaluate on test set
```

### Mixed Lists (Ordered + Unordered)

```markdown
## Analysis Steps

1. Load data and inspect structure
   - Check for missing values
   - Verify column names
   - Review data types
   
2. Perform statistical analysis
   - Calculate mean and median
   - Identify outliers
   - Test hypotheses
   
3. Create visualizations
   - Line charts for trends
   - Histograms for distributions
   - Correlation heatmaps
```

### When to Use Each List Type

| List Type | Use When | Example |
|-----------|----------|---------|
| **Unordered** | Order is optional | Libraries needed, Requirements, Features |
| **Ordered** | Order matters | Steps to follow, Workflow, Process |
| **Numbered + Bullets** | Steps with multiple items | Complex procedures, Multi-stage processes |

---

## Inline Code and Code Blocks

### Inline Code (Backticks)

Use **backticks** `` ` `` for single words or short code snippets **within text**:

**Markdown:**
```markdown
To load data, use the `pd.read_csv()` function. The parameter `header=0` tells pandas
that the first row contains column names.
```

**Renders as:**
To load data, use the `pd.read_csv()` function. The parameter `header=0` tells pandas that the first row contains column names.

### When to Use Inline Code

- Variable names: `df`, `x`, `my_list`
- Function names: `len()`, `pd.read_csv()`, `print()`
- Parameters: `header=0`, `sep=','`
- Keywords: `True`, `False`, `None`
- File paths: `data/file.csv`
- Short code: `for i in range(10)`

### Fenced Code Blocks (Triple Backticks)

Use **triple backticks** ` ``` ` for multi-line code examples **in Markdown cells** (not executable, just for display):

**Markdown:**
````markdown
```python
# This is example code (not executable)
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```
````

**Renders as:**
```python
# This is example code (not executable)
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

### Code Block with Language Specification

Specify the language after the opening backticks for syntax highlighting:

**Python:**
```python
for i in range(5):
    print(f"Iteration {i}")
```

**SQL:**
```sql
SELECT * FROM customers
WHERE age > 18
ORDER BY name;
```

**JavaScript:**
```javascript
function addNumbers(a, b) {
  return a + b;
}
```

### Code Blocks: Don't vs Do

**✗ Bad: Code block without context**
````
```python
df = pd.read_csv('file.csv')
df.head()
```
````

**✓ Good: Code block with explanation**
```markdown
Load the customer data from CSV:

```python
df = pd.read_csv('file.csv')
df.head()
```

This displays the first 5 rows to verify the data loaded correctly.
```

---

## Markdown Cell Placement

### Strategic Placement: The Markdown-Code-Markdown Pattern

**Professional structure:**

```
[Markdown Cell 1: Overview]
  ↓ Explains what we're about to do
[Code Cell 1: Implementation]
  ↓ Executes the logic
[Markdown Cell 2: Analysis]
  ↓ Explains what the output means
[Code Cell 2: More implementation]
  ↓ Next step
[Markdown Cell 3: Summary]
  ↓ Conclusion
```

### Example: Three-Cell Block

**Cell 1 - Markdown:**
```markdown
## Loading the Dataset

We'll read a CSV file containing customer purchase history.
The file has the following columns:
- `customer_id`: Unique identifier for each customer
- `purchase_amount`: Total purchase value
- `purchase_date`: Date of purchase
```

**Cell 2 - Code:**
```python
import pandas as pd

df = pd.read_csv('customers.csv')
print(df.shape)
print(df.head())
```

**Cell 3 - Markdown:**
```markdown
The dataset contains 10,000 records with information about customer purchases.
The output above shows:
- **Shape**: 10,000 rows and 3 columns
- **First few rows**: Sample data showing typical purchase records
```

### Placement Rules

1. **Before code**: Markdown explains what the code cell will do
2. **After code**: Markdown explains what the output means or what comes next
3. **Summary sections**: Markdown summarizes findings
4. **Between major sections**: Markdown marks transitions

---

## Professional Notebook Structure

### The Complete Structure Template

```markdown
# Main Project Title

## 1. Introduction
- Problem statement
- Data source overview
- Success criteria

## 2. Data Loading and Inspection
### 2.1 Load Data
[Markdown: Explain file location and format]
[Code: Load data]
[Markdown: Show data shape and types]

### 2.2 Exploratory Analysis
[Markdown: Questions to explore]
[Code: Basic statistics and visualizations]
[Markdown: Findings and observations]

## 3. Data Cleaning
### 3.1 Missing Values
### 3.2 Duplicate Records
### 3.3 Data Type Fixes

## 4. Analysis
### 4.1 Statistical Tests
### 4.2 Correlated Variables
### 4.3 Trend Analysis

## 5. Results and Recommendations
- Key findings
- Business implications
- Next steps

## 6. Appendix (Optional)
- Raw code without commentary
- Alternative approaches tried
- References and resources
```

### Table of Contents (Optional but Professional)

At the very top, after the title:

```markdown
# Project Analysis

## Table of Contents
- [1. Introduction](#1-introduction)
- [2. Data Loading](#2-data-loading)
- [3. Analysis](#3-analysis)
- [4. Conclusions](#4-conclusions)

---

## 1. Introduction
...
```

This allows readers to jump to sections quickly.

---

## Common Mistakes and Best Practices

### ❌ Mistake 1: No Markdown at All

**Problem:**
```
[Code Cell 1]
[Code Cell 2]
[Code Cell 3]
[Code Cell 4]
```
Readers have no idea what's happening!

**Solution:**
```
[Markdown: Section title and explanation]
[Code Cell 1]
[Markdown: Explain what Cell 1 did]
[Code Cell 2]
[Markdown: Explain what Cell 2 did]
...
```

### ❌ Mistake 2: Inconsistent Heading Hierarchy

**Problem:**
```markdown
# My Analysis
### Data Loading    (skipped Level 2!)
# Processing       (back to Level 1!)
#### Visualization (jumped to Level 4!)
```

**Solution:**
```markdown
# My Analysis
## Data Loading
## Processing
### Visualization Details
```

### ❌ Mistake 3: Inline Code Not Used

**Problem:**
```
To filter data, use the pd.read_csv function. Set the parameter header equals 0.
```

**Solution:**
```
To filter data, use the `pd.read_csv()` function. Set the parameter `header=0`.
```

### ❌ Mistake 4: Code Blocks Without Language

**Problem:**
````
```
for i in range(5):
    print(i)
```
````
(No syntax highlighting!)

**Solution:**
````
```python
for i in range(5):
    print(i)
```
````

### ✓ Best Practice 1: Every Section Starts with Markdown

Always introduce code cells with Markdown explaining intent:

```markdown
## Step 1: Remove Outliers

Outliers can skew analysis results. We'll identify outliers 
using the IQR (Interquartile Range) method and remove them.

[Code cell follows here]
```

### ✓ Best Practice 2: Explain Non-Obvious Code

```markdown
The following code creates a list of all unique values in the 
'category' column. We use `set()` instead of `.unique()` because 
it's faster for large datasets.

```python
categories = set(df['category'])
```
```

### ✓ Best Practice 3: Use Lists to Break Down Complex Ideas

```markdown
## Data Quality Checks

Before analysis, we verify:
1. No column contains 100% missing values
2. Date columns are in consistent format
3. Numerical columns have reasonable ranges
4. No duplicate rows exist
```

### ✓ Best Practice 4: Heading Levels Match Section Importance

```markdown
# Marketing Analysis Report

## Executive Summary
### Key Metrics
### Business Impact

## Data Processing
### Data Loading
### Cleaning Steps
### Feature Engineering

## Analysis Results
### Customer Segmentation
### Revenue Trends
### Recommendations
```

---

## Real-World Example

### Before (Poor Documentation)

```
[Cell 1 - Code]
import pandas as pd
df = pd.read_csv('sales.csv')

[Cell 2 - Code]
df = df[df['amount'] > 100]

[Cell 3 - Code]
print(df.groupby('region').sum())

[Cell 4 - Code]
import matplotlib.pyplot as plt
plt.plot(df['date'], df['amount'])
plt.show()
```

**Problem:** Readers don't know what the notebook does or why. Code is isolated.

### After (Good Documentation)

```markdown
# Sales Analysis Report

## 1. Data Loading
[Markdown]
We'll analyze sales data from Q1 2024. The data includes:
- `date`: Transaction date
- `amount`: Sale amount in USD
- `region`: Geographic region (North, South, East, West)
- `product`: Product category

[Cell 1 - Code]
import pandas as pd
df = pd.read_csv('sales.csv')
print(f"Loaded {len(df)} records")
```

```markdown
## 2. Filter High-Value Sales
[Markdown]
We focus on significant transactions (over $100) to identify 
profitable sales patterns. This filters out small purchases.

[Cell 2 - Code]
df = df[df['amount'] > 100]
print(f"After filtering: {len(df)} records")
```

```markdown
## 3. Regional Analysis
[Markdown]
Next, we group by region and calculate total sales:

[Cell 3 - Code]
regional_sales = df.groupby('region')['amount'].sum()
print(regional_sales)
```

```markdown
### Finding:
The **East region** leads with the highest total sales, 
followed by West. North region has the lowest sales, indicating 
a growth opportunity.

## 4. Sales Trend Over Time
[Markdown]
Finally, we visualize how sales have evolved throughout Q1:

[Cell 4 - Code]
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
df_sorted = df.sort_values('date')
plt.plot(df_sorted['date'], df_sorted['amount'], marker='o')
plt.title('Daily Sales Trends')
plt.xlabel('Date')
plt.ylabel('Sale Amount ($)')
plt.show()
```

```markdown
### Interpretation:
Sales show an upward trend, with a notable spike mid-quarter.
This correlates with a promotional period in mid-January.
```

**Improvement:** Readers understand every step, the intent, and the meaning of results.

---

## Summary

### The Markdown Checklist

Before submitting a notebook, verify:

- [ ] **Headings**: Clear hierarchy from # to ##
- [ ] **Sections**: Each major step has a heading
- [ ] **Lists**: Complex ideas are broken into ordered/unordered lists
- [ ] **Inline code**: Variables and functions use backticks
- [ ] **Code blocks**: Example code in Markdown uses triple backticks
- [ ] **Placement**: Markdown explains code before and after
- [ ] **Readability**: A new reader can understand the notebook's flow
- [ ] **Consistency**: Formatting is consistent throughout

### The Three Questions Test

1. **Can someone opening this notebook understand what it does without reading code first?**
2. **Are the reasons for each step clear from Markdown explanations?**
3. **Is the notebook organized logically with clear sections?**

If yes to all three, your Markdown is professional and effective.

---

## Key Takeaways

1. **Markdown is communication** - Use it to guide readers through analysis
2. **Headings create structure** - Use proper hierarchy (# → ## → ###)
3. **Lists improve clarity** - Ordered for steps, unordered for options
4. **Code formatting improves readability** - Inline code for short, blocks for examples
5. **Strategic placement matters** - Markdown before and after code cells
6. **Professional notebooks explain intent** - Not just what, but why
7. **Readers come first** - Write Markdown for someone else, not just yourself

---

**Next Steps:**

Now that you understand Markdown fundamentals, you'll create a demonstration notebook showing best practices in action. The notebook will include:
- ✓ Proper heading hierarchy
- ✓ Ordered and unordered lists
- ✓ Inline code and code blocks
- ✓ Professional section organization
- ✓ Clear explanations at each step

Then you'll record a video explaining your choices and answering: *"How would better Markdown fix a confusing notebook?"*
