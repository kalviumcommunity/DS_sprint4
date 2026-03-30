# Milestone 5: Running, Restarting, and Interrupting Jupyter Kernels

**Estimated Reading Time:** 15 minutes  
**Difficulty Level:** Intermediate  
**Focus Area:** Execution discipline, kernel state management, debugging execution order

---

## Table of Contents

1. [Overview](#overview)
2. [What is a Jupyter Kernel?](#what-is-a-jupyter-kernel)
3. [Kernel State and Memory](#kernel-state-and-memory)
4. [Running Cells Intentionally](#running-cells-intentionally)
5. [Interrupting Execution](#interrupting-execution)
6. [Restarting the Kernel](#restarting-the-kernel)
7. [Best Practices for Kernel Management](#best-practices-for-kernel-management)
8. [Common Mistakes and How to Fix Them](#common-mistakes-and-how-to-fix-them)
9. [Scenario Analysis: The Undefined Variable Problem](#scenario-analysis-the-undefined-variable-problem)
10. [Troubleshooting Guide](#troubleshooting-guide)

---

## Overview

The Jupyter kernel is the engine that executes your code. Understanding how to control it—running cells in order, interrupting long operations, and restarting cleanly—is essential for:

- **Reproducible notebooks**: Ensure your work runs the same way every time
- **Debugging**: Identify when hidden state causes failures
- **Collaboration**: Share notebooks that work for others, not just on your machine
- **Production readiness**: Build notebooks that are execution-disciplined and clean

### Why Kernel Management Matters

**Beginner mistakes:**
- Run cells out of order, creating hidden dependencies
- Forget that deleted cells' variables still exist in kernel memory
- Share a notebook that works on their machine but fails for others
- Spend hours debugging "undefined variable" errors that disappear after restart

**Professional approach:**
- Execute cells deliberately, from top to bottom
- Interrupt long operations without restarting
- Restart regularly to ensure clean state
- Always test "Restart and Run All" before sharing

---

## What is a Jupyter Kernel?

### The Kernel as an Interpreter

A Jupyter kernel is a **Python interpreter running in the background** that:

1. **Receives code** from your notebook cells
2. **Executes** that code in its memory space
3. **Maintains state** (variables, imports, function definitions) between cell executions
4. **Returns outputs** (print statements, errors, visualizations)

### The Notebook as an Interface

Your Jupyter notebook is a **frontend** that:

- Displays cells and outputs
- Sends code to the kernel
- Collects and displays results
- Allows you to interrupt or restart the kernel

**Key insight:** The notebook file (`.ipynb`) is just a static record of cells. The actual execution happens in the kernel, which is a separate, active process running in memory.

---

## Kernel State and Memory

### Understanding State

When you execute a cell, any variables you create exist in the kernel's memory. They persist until:

1. You restart the kernel
2. You redefine them in a new cell
3. You explicitly delete them

### Example: State Persistence

```
Cell 1 (execute):
x = 42

Cell 2 (execute):
print(x)  # Output: 42
```

**Why does this work?** Because Cell 1 created `x` in the kernel's memory. Cell 2 can access it.

```
Cell 1 (deleted but after execution):
x = 42

Cell 3 (execute):
print(x)  # Output: 42 ✓ Still works!
```

**The trap:** Even though you deleted Cell 1, the kernel still remembers that `x = 42` because the deletion happened only in the notebook interface, not in the kernel's memory. This is a common source of confusion.

### Visualization: Kernel State Flow

```
Run Cell 1: y = 10          →  Kernel Memory: {y: 10}
Run Cell 2: y = y + 5       →  Kernel Memory: {y: 15}
Run Cell 3: print(y)        →  Output: 15  ✓
Delete Cell 2 from notebook →  Kernel Memory: {y: 15}  (unchanged!)
Run Cell 3 again            →  Output: 15  ✓
```

Then:

```
Restart Kernel              →  Kernel Memory: {} (empty)
Run Cell 3: print(y)        →  Error: NameError: name 'y' is not defined
```

---

## Running Cells Intentionally

### The "Execution Order" Principle

A professional notebook follows a simple rule:

**Every cell should produce the same output regardless of when it's executed, as long as all previous cells have been run first.**

This means:
- Variables created in Cell 5 should only be used in Cell 6+
- Imports should happen early (Cell 1 or 2)
- Assume the kernel was just restarted when you run a cell

### How to Run Cells Intentionally

#### Method 1: Run a Single Cell
- **Keyboard:** `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac)
- **Menu:** Click the ▶ button on the cell
- **Effect:** Executes the current cell, stays in that cell

#### Method 2: Run and Down
- **Keyboard:** `Shift+Enter` (Windows/Linux/Mac)
- **Menu:** Cell → Run and Move Down
- **Effect:** Executes current cell, moves to next cell

#### Method 3: Run All Cells
- **Menu:** Cell → Run All Cells
- **Effect:** Executes from Cell 1 to Cell N in order
- **Use when:** Testing if your notebook is reproducible

#### Method 4: Run All Above / Run All Below
- **Menu:** Cell → Run All Above / Run All Below
- **Use when:** Testing dependencies on a specific cell

### Example: Intentional Execution

Good notebook structure (top to bottom):

```python
# Cell 1: Imports
import pandas as pd
import numpy as np

# Cell 2: Configuration
DATA_PATH = "data.csv"
BATCH_SIZE = 32

# Cell 3: Load data
df = pd.read_csv(DATA_PATH)

# Cell 4: Process data
df['new_col'] = df['existing_col'] * 2

# Cell 5: Analysis
print(df.head())
```

Run these cells in order: **Cell 1 → Cell 2 → Cell 3 → Cell 4 → Cell 5**

If you run Cell 5 first:
```
NameError: name 'df' is not defined
```

This is because `df` was never created (Cell 3 didn't run).

---

## Interrupting Execution

### Why Interrupt?

Sometimes a cell is running too long:
- Infinite loop
- Slow algorithm
- Network timeout
- You realize you made a mistake mid-execution

Interrupting stops the cell **without restarting the kernel**, so your other variables are preserved.

### How to Interrupt a Cell

#### Method 1: Keyboard
- **Windows/Linux:** `Ctrl+C` (in terminal) or click the ⏹ button in the notebook
- **Mac:** `Cmd+C` or click the ⏹ button

#### Method 2: Notebook Button
- Look for the **⏹ (Stop)** button in the notebook toolbar when a cell is executing
- Click it to interrupt

#### Method 3: Kernel Menu
- **Menu:** Kernel → Interrupt Kernel (useful if button doesn't work)

### Important: Interrupt vs Restart

| Action | What Happens | When to Use |
|--------|--------------|-----------|
| **Interrupt** | Stops current cell execution | Cell is running too long, you want to stop it but keep other variables |
| **Restart** | Clears all kernel memory, stops all code | You need a fresh slate, want to test reproducibility |

### Example: Interrupt in Action

```python
# Cell 1
import time
counter = 0

# Cell 2
for i in range(1000000):
    counter += 1
    time.sleep(0.1)  # Each iteration takes 0.1 seconds
    print(f"Processing... {counter}")
```

When you run Cell 2:
- It starts printing "Processing... 1, 2, 3, ..."
- After 5 iterations, you press Ctrl+C (or click Stop button)
- The loop stops immediately ⏹
- The kernel is still running, and `counter` still exists in memory
- You can run other cells that use `counter`

---

## Restarting the Kernel

### What Restart Does

Restarting the kernel:
1. **Stops** any currently running code
2. **Clears** all variables, imports, and function definitions from memory
3. **Resets** the kernel to a blank state
4. **Restarts** a fresh Python interpreter

After restart, your notebook cells remain in the file, but the kernel has no memory of them.

### How to Restart the Kernel

#### Method 1: Notebook Menu
- **Menu:** Kernel → Restart Kernel (or Restart & Clear Output / Restart & Run All)

#### Method 2: Keyboard
- No direct keyboard shortcut; use the menu

#### Method 3: Cell Execution Error
- Sometimes VS Code or Jupyter restarts the kernel automatically if it crashes

### Restart Options

**Restart Kernel:**
- Clears memory but keeps notebook visible
- Use when you need a fresh state but want to see your code

**Restart Kernel & Clear Output:**
- Clears memory and removes all cell outputs
- Use when you want a completely clean notebook

**Restart Kernel & Run All:**
- Clears memory, then automatically executes all cells in order
- This is the **reproducibility test**: Does your notebook work from scratch?
- Essential before sharing notebooks

### Example: Restart Workflow

```python
# Cell 1: Run (creates my_var = 100)
my_var = 100
print(my_var)  # Output: 100

# Cell 2: Run (prints my_var, uses value from Cell 1)
print(my_var)  # Output: 100

# Now restart the kernel
# Kernel is reset, my_var no longer exists in memory

# Cell 2: Run again (error!)
print(my_var)  # NameError: name 'my_var' is not defined
```

To fix this, you must run Cell 1 again first:

```python
# Cell 1: Run
my_var = 100
print(my_var)  # Output: 100

# Cell 2: Run (now works)
print(my_var)  # Output: 100
```

---

## Best Practices for Kernel Management

### 1. Run Cells in Order

**✓ Good:**
```
Run Cell 1 → Run Cell 2 → Run Cell 3 → Run Cell 4
```

**✗ Bad:**
```
Run Cell 3 → Run Cell 1 → Run Cell 4 → Run Cell 2
```

Always execute from top to bottom unless you have a specific reason not to.

### 2. Use "Run All Cells" Regularly

Before sharing a notebook, run:
- **Cell → Run All Cells**

This ensures your notebook is reproducible from a fresh kernel state.

### 3. Organize Cells Logically

```python
# === SETUP ===
# Cell 1: Imports
import pandas as pd
import numpy as np

# Cell 2: Configuration
DATA_PATH = "data.csv"
SEED = 42

# === DATA ===
# Cell 3: Load data
df = pd.read_csv(DATA_PATH)

# === PROCESSING ===
# Cell 4: Clean data
df = df.dropna()

# === ANALYSIS ===
# Cell 5: Analyze results
print(df.describe())
```

### 4. Avoid Relying on Hidden State

**✗ Bad:**
```python
# Cell 5: This works if Cell 1-4 ran, but fails if run in isolation
result = df.groupby('category').sum()
```

**✓ Good:**
```python
# Cell 5: This works because we created df here
df = pd.read_csv("data.csv")  # Load afresh
result = df.groupby('category').sum()
```

### 5. Use Clear Variable Names and Comments

**✗ Bad:**
```python
x = 42
y = x + 10
z = y * 2
```

**✓ Good:**
```python
# Define batch size for processing
batch_size = 42

# Calculate delay based on batch size
delay_ms = batch_size + 10

# Final timeout in milliseconds
timeout_ms = delay_ms * 2
```

### 6. Interrupt Instead of Restarting (When Possible)

If a cell is just slow, interrupt it (Ctrl+C). This preserves your kernel state and variables.

Only restart when you need a clean slate or suspect kernel corruption.

### 7. Test Before Submitting

**Checklist:**
- [ ] Run all cells in order (Cell → Run All Cells)
- [ ] Verify no errors appear
- [ ] Verify outputs look correct
- [ ] Restart kernel (Kernel → Restart Kernel)
- [ ] Run all cells again
- [ ] Verify same outputs appear
- [ ] Restart one more time and check Cell 1-5 specifically (not the whole notebook)

---

## Common Mistakes and How to Fix Them

### Mistake 1: "My notebook works, but my friend's doesn't"

**Cause:** You have hidden variables in kernel memory that your friend doesn't.

**Example:**
```python
# Cell 1: You run this early
my_secret_var = 10

# Cell 5: You run this
result = my_secret_var + 5  # Works for you!
print(result)  # Output: 15
```

Your friend opens your notebook, sees Cell 5, and runs it:
```python
# Cell 5 (friend runs only this cell)
result = my_secret_var + 5
# NameError: name 'my_secret_var' is not defined
```

**Fix:**
- Always run cells in order
- Test with "Run All Cells" before sharing
- Avoid splitting logic across distant cells

### Mistake 2: "Deleting a cell doesn't delete its effects"

**Cause:** Deleting a cell from the notebook doesn't remove its variable from kernel memory.

**Example:**
```python
# Cell 2: You define a function
def calculate(x):
    return x * 2

# Later: You delete Cell 2 from your notebook

# Cell 5: You can still run this!
result = calculate(10)  # Works because function still in kernel memory
```

**Fix:**
- Restart kernel after deleting cells (clears all memory)
- Or use "Run All Cells" to ensure only your current cells define variables

### Mistake 3: "Rerunning a cell produces different output"

**Cause:** Cell depends on external state (file changed, random seed not set, network timeout).

**Example:**
```python
# Cell 1: Load data from a file
df = pd.read_csv("data.csv")

# Cell 2: First run
print(len(df))  # Output: 100 rows

# (Someone modifies data.csv)

# Cell 2: Second run
print(len(df))  # Output: 200 rows  (different!)
```

**Fix:**
- Set random seed if using random numbers
- Load data from a stable location
- Document data dependencies
- Mock external data in tests

### Mistake 4: "I added a cell but the output doesn't update"

**Cause:** You modified a cell but didn't rerun it; the old output is still displayed.

**Example:**
```python
# Cell 1: Initial code (you already ran this)
x = 10

# Later: You edit Cell 1 to say x = 20
# But you don't rerun it
print(x)  # Still shows output: 10 (old output!)
```

**Fix:**
- After editing a cell, press Ctrl+Enter to rerun it
- The output will update to reflect your changes

### Mistake 5: "Variables have weird values"

**Cause:** You accidentally overrote a variable earlier and forgot.

**Example:**
```python
# Cell 1
user_id = 42

# Cell 3
user_id = 99  # Oops, overwrote it!

# Cell 5
print(user_id)  # Output: 99 (expected 42, got 99!)
```

**Fix:**
- Use distinct variable names
- Add comments explaining what each variable is for
- Use "Restart & Run All" to test from scratch
- Check Kernel → Restart & Run All to ensure expected values

---

## Scenario Analysis: The Undefined Variable Problem

### The Real-World Scenario

You've been working on a notebook for days. It runs perfectly on your machine. You upload it to GitHub and ask a colleague to review it. They download your notebook, open it, and try to run all cells.

**Result:** NameError on Cell 7: `name 'my_data' is not defined`

But Cell 7 works fine when you run it! Why?

### Root Cause Analysis

**Hypothesis 1: Hidden Kernel State**

You ran cells in this order:
- Cell 3 (defines `my_data`)
- Cell 7 (uses `my_data`) ✓ Works
- Cell 5 (overwrites `my_data`)
- Cell 2 (imports libraries)

Your kernel memory has `my_data` from Cell 3, so Cell 7 works.

Your colleague ran cells in order (Cell 1 → 2 → 3 → ... → 7), but Cell 3 was skipped due to an error, so `my_data` was never defined. Cell 7 fails.

**Hypothesis 2: Faulty Cell Deletion**

You delete the cell that defines `my_data` (to clean up), but your colleague gets an old version of your notebook where that cell still exists. They run it differently than you expected.

**Hypothesis 3: Race Condition or Import Error**

Cell 3 depends on an import in Cell 1. Your colleague opens the notebook and runs only Cell 3 (without Cell 1 running first), so the import is missing.

### The Gold Standard Test: "Restart & Run All"

Before submitting any notebook:

1. Press **Kernel → Restart Kernel & Run All**
2. Watch every cell execute in order
3. Verify no errors occur
4. Verify outputs are correct
5. If any cell fails, fix it

If "Restart & Run All" works, your notebook is reproducible and will work for others.

### The Fix for the Undefined Variable Problem

**Step 1: Identify the dependency chain**

```python
# Cell 1: Imports (MUST run first)
import pandas as pd

# Cell 3: Creates my_data (MUST run before Cell 7)
my_data = pd.DataFrame({'x': [1, 2, 3]})

# Cell 7: Uses my_data (depends on Cell 3)
print(my_data['x'].sum())
```

**Step 2: Test with "Restart & Run All"**

Run: Kernel → Restart Kernel & Run All

Expected flow:
- Cell 1 runs: Imports pandas ✓
- Cell 3 runs: Creates my_data ✓
- Cell 7 runs: Prints 6 ✓

**Step 3: Ensure no cell can run in isolation**

Every cell should assume:
- All previous cells have been run
- All variables have been defined
- All imports are available

**Step 4: Add comments to clarify dependencies**

```python
# Cell 7: Calculate sum (requires Cell 1 imports & Cell 3 data)
print(my_data['x'].sum())
```

---

## Troubleshooting Guide

### Problem: "Cell is taking too long to run"

**Solution:**
1. Press Ctrl+C to interrupt
2. Check your code for infinite loops
3. Consider breaking the problem into smaller steps
4. Use print statements to track progress

### Problem: "I see old outputs even though I edited the cell"

**Solution:**
1. Edit your cell
2. Press Ctrl+Enter to rerun it
3. The output will update

### Problem: "Two cells use the same variable and I'm not sure which one defined it"

**Solution:**
1. Use Ctrl+F to search for the variable definition
2. Check Kernel → Restart Kernel & Run All to see which cell actually defines it
3. Rename variables to be more specific

### Problem: "My notebook crashes when I run all cells but works when I run them one by one"

**Solution:**
1. Check for race conditions (e.g., writing to the same file in two cells)
2. Check for timing issues (e.g., waiting for an external service)
3. Restart kernel and try again
4. Check if you're modifying data in a cell and then using it in a later cell in a way that depends on order

### Problem: "I restarted the kernel but my notebook still has errors"

**Solution:**
1. Check for syntax errors (red squiggly lines)
2. Verify all imports are available (pip install needed packages)
3. Check that file paths are correct
4. Try running cells one by one to find where the error originates
5. Use print statements to debug

### Problem: "I want to see the current state of all variables"

**Solution:**
- VS Code Jupyter: Look for the **Variables** icon in the Run panel
- Jupyter Lab/Notebook: Use `%whos` command in a cell to list all variables
- Or check Kernel → Show All Defined Variables (feature varies by IDE)

---

## Summary: Five Core Principles

1. **Run cells in order** (top to bottom)
2. **Use "Run All Cells" before sharing** (test reproducibility)
3. **Interrupt slow cells** (don't restart unnecessarily)
4. **Restart when you suspect hidden state** (clears everything)
5. **Never rely on cell execution order** (assume cells run from scratch)

---

## Checklist Before Submission

- [ ] All cells run without errors
- [ ] Cells run in order (Cell 1 → Cell 2 → Cell 3 → ...)
- [ ] "Run All Cells" works from a fresh kernel restart
- [ ] No undefined variable errors
- [ ] No hidden dependencies between distant cells
- [ ] Comments explain cell purpose and dependencies
- [ ] Variables have clear, descriptive names
- [ ] No cells rely on external state (files, network, random seed)
- [ ] Notebook is reproducible (same outputs each time)

---

**Key Takeaway:**

A professional notebook is execution-disciplined. It doesn't rely on hidden kernel state, it runs the same way every time, and it works for anyone—not just on your machine.

Master kernel management, and you've solved one of the hardest debugging problems in data science: "It works on my machine but not yours!"
