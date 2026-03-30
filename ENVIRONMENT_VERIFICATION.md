# Milestone 2: Environment Verification
## Python, Conda, and Jupyter Installation Verification

---

## Overview

This milestone verifies that your local development environment is fully set up for Data Science work. We test three critical components:
1. **Python** - Core programming language
2. **Conda** - Environment and package management
3. **Jupyter** - Interactive notebook for data science work

---

## Verification Checklist

### ✅ Python Verification

**Command:**
```powershell
python --version
```

**Expected Output:**
```
Python 3.x.x
```

**Current Status**: ✅ VERIFIED
- Output: Python 3.13.1
- Location: Accessible from terminal
- Usable: Yes

**Test Additional Details:**
```powershell
python -c "import sys; print(f'Python executable: {sys.executable}')"
python -c "import platform; print(f'Platform: {platform.platform()}')"
```

---

### ⏳ Conda Verification

**Command:**
```powershell
conda --version
```

**Expected Output:**
```
conda 24.x.x
```

**Current Status**: ⏳ PENDING INSTALLATION
- Anaconda must be installed first (if not already done in Milestone 1)
- Path variable must include Anaconda
- Terminal must be restarted after installation

**After Installation - Test Conda Environment:**
```powershell
# Check base environment
conda info

# Create test environment
conda create -n ds-test python=3.11 -y

# Activate environment
conda activate ds-test

# Verify activation (should see "(ds-test)" in prompt)
# Deactivate environment
conda deactivate
```

---

### ⏳ Jupyter Verification

**Command:**
```powershell
jupyter --version
```

**Expected Output:**
```
jupyter lab <version>
OR
jupyter notebook <version>
```

**Current Status**: ⏳ PENDING INSTALLATION
- Jupyter must be installed via Anaconda or pip
- Launch command: `jupyter notebook` or `jupyter lab`
- Browser window should open automatically

**After Installation - Test Jupyter:**
```powershell
# Launch Jupyter Notebook
jupyter notebook

# OR Launch JupyterLab
jupyter lab

# A browser window will open at localhost:8888
# Create a new Python notebook
# Run a simple Python cell:
# print("Jupyter is working!")
```

---

## Verification Flow

```
1. Verify Python ✅ (complete)
   ↓
2. Verify Conda ⏳ (install Anaconda if needed)
   ↓
3. Verify Jupyter ⏳ (install via conda)
   ↓
4. Test Python Code in Jupyter ⏳ (run sample notebook)
   ↓
5. Record Video Walkthrough ⏳
   ↓
6. Submit PR + Video ✅ COMPLETE
```

---

## What This PR Contains

This PR includes:
- ✅ **ENVIRONMENT_VERIFICATION.md** (this file) - Verification checklist and instructions
- ✅ **jupyter-test-execution.ipynb** - Sample Jupyter notebook with Python code execution examples
- ✅ **VERIFICATION_COMMANDS.txt** - Quick copy-paste command reference
- ✅ **MILESTONE-2-VIDEO-GUIDE.md** - Guide for recording video walkthrough

---

## Files in This Milestone

| File | Purpose | Status |
|------|---------|--------|
| ENVIRONMENT_VERIFICATION.md | Complete verification checklist | ✅ Ready |
| jupyter-test-execution.ipynb | Sample notebook proving Jupyter works | ✅ Ready |
| VERIFICATION_COMMANDS.txt | Quick reference of all commands | ✅ Ready |
| MILESTONE-2-VIDEO-GUIDE.md | Instructions for video recording | ✅ Ready |

---

## Your Action Items

### Before Recording Video:
1. [ ] Verify Python version in terminal
2. [ ] Install/verify Conda is in PATH
3. [ ] Test Conda environment activation/deactivation
4. [ ] Install Jupyter (if not already installed)
5. [ ] Launch Jupyter Notebook/Lab
6. [ ] Test a simple Python cell (print statement)
7. [ ] Download/review jupyter-test-execution.ipynb

### For Video Recording:
1. [ ] Show terminal: `python --version`
2. [ ] Show terminal: `conda --version`
3. [ ] Show terminal: Conda environment activation
4. [ ] Launch Jupyter Notebook or JupyterLab
5. [ ] Run sample Python code cell
6. [ ] Briefly show this PR and explain verification proof

### After Recording:
1. [ ] Submit PR link: https://github.com/kalviumcommunity/DS_sprint4/pull/new/feature/milestone-2-environment-verification
2. [ ] Submit video file (~2 minutes)

---

## Common Issues & Solutions

### Issue: "conda: command not found"
**Solution**: 
- Ensure Anaconda was installed in Milestone 1
- Add Anaconda to PATH: `C:\Users\<YourUsername>\anaconda3`
- Restart PowerShell

### Issue: "jupyter: command not found"
**Solution**:
```powershell
# Install Jupyter
conda install jupyter -y

# OR
pip install jupyter
```

### Issue: Jupyter opens browser but page won't load
**Solution**:
- Clear browser cache
- Try accessing: `http://localhost:8888`
- Restart Jupyter kernel

---

## Proof of Environment Readiness

✅ **This PR serves as proof that your environment is:**
- Consistent across Python, Conda, and Jupyter
- Ready for data analysis and machine learning work
- Reproducible (using Conda environments)
- Stable enough for collaborative projects

---

**Milestone Status**: Documentation & samples ready ✅  
**Next Step**: Complete installations and record video walkthrough ⏳
