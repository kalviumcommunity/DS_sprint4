# Environment Setup Guide & Verification

## Part A: Installation Instructions

### Step 1: Install Python (if not already installed)
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Verify: `python --version`

### Step 2: Install Anaconda
1. Download Anaconda from https://www.anaconda.com/download
2. Choose the Python 3.x version (latest stable)
3. Run the installer
4. **IMPORTANT**: Check "Add Anaconda to PATH" during installation
5. Restart PowerShell/Terminal
6. Verify: `conda --version`

### Step 3: Verify Complete Setup
Run these commands in PowerShell to confirm everything works:

```powershell
# Check Python
python --version
python -c "import sys; print('Python Location:', sys.executable)"

# Check Conda
conda --version
conda info

# Check pip
pip --version

# Check basic packages
python -c "import numpy; print('NumPy installed')"
python -c "import pandas; print('Pandas installed')"
```

---

## Part B: Installation Verification Status

### ✅ Completed
- **Python 3.13.1** - Installed and verified

### ⏳ In Progress / Next Steps
- **Anaconda/Conda** - Download from https://www.anaconda.com/download
- **Virtual Environment Creation** - Will use `conda create` to set up project env
- **Data Science Libraries** - Will install pandas, numpy, scikit-learn, jupyter

---

## Part C: Why This Setup Matters for DS Sprint 4

### Environment Consistency
- **Problem**: Code works on your machine but fails for teammates
- **Solution**: Using Conda allows creating reproducible environments with `environment.yml`
- **Benefit**: Everyone on the team gets the same Python version, same package versions

### Collaborative Best Practice
```bash
# Export environment for teammates
conda env export > environment.yml

# Teammates can recreate your setup
conda env create -f environment.yml
```

### Expected Output After Full Setup
```
Python 3.x.x
conda 24.x.x (or latest)
pip 24.x.x
All libraries install without errors
Jupyter Lab/Notebook ready to use
```

---

## Scenario-Based Reasoning: Diagnosing Environment Issues

**Scenario**: Your code runs fine locally but breaks on a teammate's machine.

### Diagnostic Steps Using This Setup:

1. **Check Python Versions**
   ```powershell
   python --version  # Your version
   ```
   Compare with teammate's output

2. **Check Package Versions**
   ```powershell
   pip list
   conda list
   ```
   Export and compare environments

3. **Use Conda for Consistency**
   ```powershell
   conda env export > environment.yml
   # Share with teammate - they run:
   conda env create -f environment.yml
   ```

4. **Prevent Issues Early**
   - Document Python version requirements in README
   - Commit `environment.yml` or `requirements.txt` to repo
   - Test code on different Python versions during development

### Why Early Setup Validation Matters:
- ✅ Identifies compatibility issues before data analysis starts
- ✅ Saves debugging time later when working with large datasets
- ✅ Ensures reproducibility (others can verify your findings)
- ✅ Makes onboarding new team members faster

---

## Files in This PR
- `SETUP_VERIFICATION.md` - This document
- `environment-setup-checklist.txt` - Quick reference checklist

**Status**: Ready for DS Sprint 4 ✅
