# Milestone 3: Launching Jupyter Notebook and Understanding the Home Interface

## Overview

This milestone focuses on **workspace awareness** — understanding how Jupyter Notebook works from a file system perspective. We'll learn to:
1. Launch Jupyter from the correct project directory
2. Navigate the Jupyter Home interface
3. Create and save notebooks in the right location
4. Understand why working directory matters in data science projects

**Important**: This is NOT about data analysis. This is about setting up your workspace correctly so that future milestones work smoothly.

---

## Part A: Understanding the Jupyter Home Interface

### What is the Jupyter Home Interface?

When you launch Jupyter Notebook, it opens a web browser showing a file browser interface. This interface allows you to:
- Navigate folders within your "working directory"
- Create new notebooks
- Open existing notebooks
- Manage files and folders
- See your current location in the file tree

### Key Components of the Home Interface

```
┌─────────────────────────────────────────────────────────┐
│ Jupyter                              [Jupyter Logo]      │
├─────────────────────────────────────────────────────────┤
│ Files    Clusters                                        │
├─────────────────────────────────────────────────────────┤
│ Breadcrumb: /c:/sprint-4-ds-lifecycle                   │
├─────────────────────────────────────────────────────────┤
│ [ New ]  [ Upload ]  [ Refresh ]  [ New Folder ]        │
├─────────────────────────────────────────────────────────┤
│ 📁 notebooks/                                           │
│ 📁 data/                                                │
│ 📄 data-science-lifecycle.md                            │
│ 📄 jupyter-test-execution.ipynb                         │
│ 📄 SETUP_VERIFICATION.md                                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Understanding Each Component

**1. Breadcrumb Navigation**
- Shows your current location in the filesystem
- Path: `/c:/sprint-4-ds-lifecycle` means you're in that folder
- Click on any part to navigate up the folder tree
- Example: `/c:/sprint-4-ds-lifecycle/notebooks/` → click breadcrumb to go back

**2. Files & Folders List**
- 📁 = Folder (clickable, takes you inside)
- 📄 = File (depends on type)
  - `.ipynb` = Jupyter Notebook (clickable, opens in editor)
  - `.md`, `.txt` = Text files
  - `.py` = Python script files

**3. Action Buttons**
- **New**: Create new notebook or text file
- **Upload**: Add files from your computer
- **Refresh**: Reload file listing
- **New Folder**: Create a new directory

**4. Notebook File (`.ipynb`)**
- Contains notebook, metadata, and execution history
- Created in whatever folder you're currently viewing
- Example: Creating notebook in `/data/` creates file in that folder

---

## Part B: Launching Jupyter from the Correct Directory

### Why Working Directory Matters

```
Working Directory = Where Jupyter looks for files by default

If launched from:     Jupyter can access:
────────────────────────────────────────────────────────
C:\                  Files in C:\ and all subdirectories
C:\sprint-4-ds...    Files in sprint-4-ds... and subdirectories
C:\Users\Name\...    Only files in home directory path
```

### Correct Way to Launch Jupyter

**Step 1: Open PowerShell**

**Step 2: Navigate to your project folder**
```powershell
cd c:\sprint-4-ds-lifecycle
```

**Step 3: Verify you're in the right place**
```powershell
# Show current directory
pwd

# List files to confirm
dir
```

**Step 4: Launch Jupyter Notebook**
```powershell
jupyter notebook
```

**What happens:**
1. Jupyter server starts in the terminal
2. Browser opens automatically (localhost:8888)
3. Home interface shows files in `/c:/sprint-4-ds-lifecycle`
4. You can now create notebooks here or in subdirectories

### Incorrect Ways (Avoid These)

❌ **Launching from wrong directory:**
```powershell
cd C:\Users\YourName
jupyter notebook   # Can only see files in home folder, not project!
```

❌ **Launching without changing directory:**
```powershell
# Already in C:\random\path
jupyter notebook   # Jupyter working directory is C:\random\path
```

❌ **Launching without knowing where you are:**
```powershell
jupyter notebook   # Where is my project? Can't find my data!
```

---

## Part C: Creating & Saving Notebooks in the Correct Location

### File Organization Pattern for DS Projects

```
sprint-4-ds-lifecycle/          ← Launch Jupyter here
├── data/                       ← Store datasets here
│   └── crop_data.csv
├── notebooks/                  ← Create notebooks here (or here)
│   ├── 01-data-exploration.ipynb
│   └── 02-analysis.ipynb
├── scripts/                    ← Store Python scripts here
│   └── data_cleaning.py
└── outputs/                    ← Save results here
    ├── visualizations.png
    └── model_results.csv
```

### Creating a Notebook in the Right Place

**Scenario: Create a notebook in the `notebooks/` folder**

1. Launch Jupyter from project root:
   ```powershell
   cd c:\sprint-4-ds-lifecycle
   jupyter notebook
   ```

2. In Jupyter Home interface, navigate to `notebooks/` folder
   - Click on the 📁 `notebooks/` folder in the file list

3. You're now inside `notebooks/` (check breadcrumb: `/c:.../notebooks`)

4. Click **New** → **Python 3** to create notebook

5. Jupyter opens the notebook editor in a new tab

6. The notebook is automatically saved as `Untitled.ipynb` in the `notebooks/` folder

7. Rename it by right-clicking in file browser or using File menu

---

## Part D: Diagnosing File Path Issues (Scenario-Based Reasoning)

### The Problem: "File Not Found"

**Situation:**
```python
import pandas as pd
df = pd.read_csv("crop_data.csv")  # Error! File not found
```

You get: `FileNotFoundError: [Errno 2] No such file or directory: 'crop_data.csv'`

### Root Causes & Diagnosis Using Workspace Awareness

**Diagnosis Method 1: Check Current Working Directory**

In your notebook, add a cell:
```python
import os
print(os.getcwd())  # Shows current working directory
```

**If output is:**
- `/c:/sprint-4-ds-lifecycle` → You're in project root, but file is in `/data/` subdirectory
- `/home/username` → Wrong! Jupyter launched from home directory

**Diagnosis Method 2: Check File Location**

In your notebook:
```python
import os
print(os.listdir('.'))    # List files in current folder
print(os.listdir('./data/'))  # List files in data/ folder
```

**Diagnosis Method 3: Verify Launch Directory**

Look at terminal window where you launched Jupyter. First line should show:
```
The Jupyter Notebook is running at: http://localhost:8888/?token=...
```

The working directory is shown in terminal output and reflected by breadcrumb in browser.

### Solution Using Relative Paths

Once you understand your working directory, fix the path:

```python
# Wrong: Assumes file in current directory
df = pd.read_csv("crop_data.csv")

# Correct: Navigate to data/ folder first
df = pd.read_csv("data/crop_data.csv")  # Relative path from project root

# Even better: Use os.path.join()
import os
data_path = os.path.join("data", "crop_data.csv")
df = pd.read_csv(data_path)
```

### Why Workspace Awareness Matters in DS Projects

1. **Reproducibility**: If file path is hardcoded to one computer's location, code breaks on other machines
2. **Collaboration**: Team members have different home directories; relative paths work for everyone
3. **Debugging**: Knowing working directory helps diagnose "file not found" errors quickly
4. **Project Structure**: Intentional folder organization prevents accidentally overwriting files or losing data

---

## Part E: What This PR Demonstrates

Files included in this PR:

| File | Purpose |
|------|---------|
| JUPYTER_HOME_INTERFACE_GUIDE.md | This document - Complete reference |
| project-notebook-sample.ipynb | Sample notebook with file path examples |
| JUPYTER_LAUNCH_CHECKLIST.txt | Quick reference steps |
| MILESTONE-3-VIDEO-GUIDE.md | Script and timing for video |
| notebooks/ folder | Correct location for notebooks |

**Evidence of Correct Practice:**
- ✅ Notebooks in `notebooks/` folder, not scattered at root
- ✅ Sample notebook demonstrates file path best practices
- ✅ Documentation explains folder structure reasoning
- ✅ Video walkthrough shows correct launch and navigation

---

## Summary: Key Takeaways

### ✅ DO:
- Launch Jupyter from project root directory
- Create notebooks in organized subfolders (`notebooks/`)
- Use relative paths (`data/file.csv` not `C:/Users/...`)
- Check working directory when debugging file paths
- Keep data files separate from notebooks

### ❌ DON'T:
- Launch Jupyter from random directory
- Save notebooks to home folder or random locations
- Use hardcoded absolute paths
- Assume Jupyter finds files automatically
- Mix notebooks, data, and scripts in one folder

---

**Status**: Workspace best practices documented ✅  
**Next Step**: Watch video guide, then record your own walkthrough ⏳
