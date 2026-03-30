# Sample Data Science Project

A demonstration of clean, professional project structure for data science work.

## 📁 Project Structure

```
sample-ds-project/
├── README.md                    ← Project overview (this file)
├── .gitignore                   ← Git configuration
├── requirements.txt             ← Python dependencies
│
├── data/                        ← All project data
│   ├── raw/                     ← Original, immutable source data
│   └── processed/               ← Cleaned, analysis-ready data
│
├── notebooks/                   ← Jupyter notebooks for exploration
│   ├── 01_exploratory_analysis.ipynb
│   └── 02_feature_engineering.ipynb
│
├── scripts/                     ← Reusable Python code
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── utils.py
│
├── outputs/                     ← Generated files (models, plots, reports)
│   ├── models/                  ← Trained models
│   ├── visualizations/          ← Generated charts and plots
│   └── reports/                 ← Analysis reports
│
├── configs/                     ← Configuration files
│   └── parameters.yaml
│
└── docs/                        ← Documentation
    └── data_dictionary.md
```

## 🎯 Purpose

This project demonstrates:
- **Separation of Concerns:** Raw data, processed data, code, and outputs in separate locations
- **Consistency:** Predictable folder names and structure
- **Clarity:** Clear purpose for each folder
- **Scalability:** Easy to expand as project grows
- **Collaboration:** Easy for teammates to navigate

## 📊 Data Overview

### Raw Data (`data/raw/`)
- **Location:** `data/raw/`
- **Rule:** NEVER modify files here
- **Contents:** Original datasets as received from sources
- **Purpose:** Preserve original data for reproducibility

### Processed Data (`data/processed/`)
- **Location:** `data/processed/`
- **Contents:** Cleaned, transformed, analysis-ready data
- **Examples:**
  - Cleaned datasets (duplicates removed, missing values handled)
  - Feature-engineered data
  - Train/test splits
  - Merged datasets

## 💻 Code

### Jupyter Notebooks (`notebooks/`)
- **Purpose:** Exploratory analysis, prototyping, visualization
- **Naming:** Use numbered prefix for sequence (01_, 02_, etc.)
- **Workflow:** Experiments and interactive analysis

### Python Scripts (`scripts/`)
- **Purpose:** Reusable, production-ready code
- **Contents:**
  - Data cleaning functions
  - Feature engineering functions
  - Utility functions
- **Usage:** Import into notebooks for cleaner code

**Example Usage:**
```python
# In a notebook:
from scripts.data_cleaning import remove_duplicates
from scripts.utils import load_config

df_raw = pd.read_csv('data/raw/data.csv')
df_clean = remove_duplicates(df_raw)
df_clean.to_csv('data/processed/data_cleaned.csv')
```

## 📦 Outputs

### Models (`outputs/models/`)
- Serialized trained models (.pkl, .h5, .joblib)
- Model metadata and performance metrics

### Visualizations (`outputs/visualizations/`)
- Generated plots and charts
- EDA visualizations
- Model evaluation plots

### Reports (`outputs/reports/`)
- Analysis summaries
- HTML or PDF reports
- CSV exports for stakeholders

## ⚙️ Configuration

### configs/
- **Purpose:** Centralized parameter management
- **Contents:** YAML/JSON configuration files
- **Usage:** Import in Python scripts

**Example (configs/parameters.yaml):**
```yaml
data:
  raw_path: ./data/raw/
  processed_path: ./data/processed/
  
model:
  test_size: 0.2
  random_state: 42
  
output:
  models_path: ./outputs/models/
  viz_path: ./outputs/visualizations/
```

## 📖 Documentation

### docs/data_dictionary.md
- Description of each data column
- Data types and ranges
- Missing value information
- Data sources

## 🚀 Quick Start

1. **Set up environment:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Place raw data:**
   ```
   Copy your CSV/Excel files to: data/raw/
   ```

3. **Explore data:**
   ```bash
   jupyter notebook notebooks/01_exploratory_analysis.ipynb
   ```

4. **Extract reusable code:**
   ```
   Move repetitive functions to: scripts/
   ```

5. **Save outputs:**
   ```
   Models go to: outputs/models/
   Plots go to: outputs/visualizations/
   Reports go to: outputs/reports/
   ```

## 🔄 Workflow

```
Raw Data (data/raw/)
        ↓
    [Notebook] → Execute → [Script]
        ↓
Processed Data (data/processed/)
        ↓
    [Notebook] → Analysis → Plot + Model
        ↓
Outputs (outputs/)
```

## 📋 Naming Conventions

### Files
- **Notebooks:** `01_exploratory_analysis.ipynb` (numbered, descriptive)
- **Scripts:** `data_cleaning.py` (descriptive, singular purpose)
- **Data:** `customer_data_raw_2024.csv` (specific, indicates raw/processed)
- **Models:** `model_random_forest_tuned.pkl` (type and status)
- **Plots:** `feature_importance_comparison.png` (descriptive)

### Folders
- Use **lowercase with underscores**
- Use **singular** for data folders (`data/`, not `datas/`)
- Use **plural** for collections (`notebooks/`, `outputs/`)
- Avoid version numbers (use git instead)

## 📊 Key Principles

### 1. Immutability of Raw Data
```python
# ✓ RIGHT: Create new file, don't modify raw
df_raw = pd.read_csv('data/raw/sales.csv')
df_clean = df_raw.drop_duplicates()
df_clean.to_csv('data/processed/sales_cleaned.csv')

# ❌ WRONG: Modifying raw data
df = pd.read_csv('data/raw/sales.csv')
df.drop_duplicates(inplace=True)
df.to_csv('data/raw/sales.csv')  # Overwrote original!
```

### 2. Separation of Concerns
- Keep raw data separate from processed data
- Keep exploratory notebooks separate from scripts
- Keep code separate from outputs
- Keep generated files in `outputs/`

### 3. Consistency
- Same structure for every project
- Everyone knows where to find things
- Easy to onboard new team members

### 4. Documentation
- README explains the project
- `docs/data_dictionary.md` describes data
- Scripts have docstrings and comments
- Configuration files are self-explanatory

## 🎓 Why This Structure?

### For Your Analysis
- ✓ Know where everything is
- ✓ Easy to find data you created
- ✓ Can reproduce results
- ✓ Clean git history

### For Your Teammates
- ✓ Can quickly understand project
- ✓ Know where to find data
- ✓ Can contribute without confusion
- ✓ Can run analysis independently

### For Your Future Self
- ✓ 6 months later, still understand it
- ✓ Easy to extend project
- ✓ Can learn from previous analysis
- ✓ Professional appearance

## 🔍 Common Mistakes to Avoid

❌ Mixing raw and processed data
❌ Storing outputs in `data/` folder
❌ Multiple notebook versions (v1, v2, final, FINAL)
❌ Replicating code across notebooks instead of scripts
❌ No documentation explaining folder purposes
❌ Unclear folder names
❌ Storing data in `docs/` or root directory

## ✓ Next Steps

1. **Explore** each folder to understand its purpose
2. **Review** `docs/data_dictionary.md` for documentation practices
3. **Notice** the consistency and clarity of structure
4. **Adopt** this structure for your projects
5. **Share** with teammates to maintain consistency

---

**This is a demonstration of professional project structure. Refer to `PROJECT_STRUCTURE_GUIDE.md` for detailed guidance on implementation.**
