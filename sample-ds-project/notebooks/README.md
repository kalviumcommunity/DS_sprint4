# Notebooks

**Purpose:** Jupyter notebooks for exploratory analysis and prototyping

## About Notebooks

This folder contains Jupyter notebooks for interactive exploration, visualization, and prototyping. Notebooks are great for:
- Exploring data visually
- Testing hypotheses
- Iterating on analysis
- Documenting findings
- Creating visualizations

## Naming Convention

Use **numbered prefix** for sequence:

```
notebooks/
├── 01_exploratory_analysis.ipynb
├── 02_feature_engineering.ipynb
├── 03_model_training.ipynb
└── 04_model_evaluation.ipynb
```

**Why numbers?**
- Clear progression of work
- Easy to sort chronologically
- Shows logical flow
- Prevents confusion about which is "current"

## What Goes Here

- **Exploratory Data Analysis (EDA):** Understanding data structure, distributions, patterns
- **Visualization experiments:** Testing different plots and charts
- **Feature engineering:** Creating and testing new features
- **Model prototyping:** Testing different models
- **Results analysis:** Interpreting model outputs

## What Does NOT Go Here

- ❌ Multiple versions of same analysis (`04_v1.ipynb`, `04_final.ipynb`)
- ❌ One-off test notebooks (keep locally or on separate branch)
- ❌ Reusable functions (extract to `../scripts/`)
- ❌ Production code (use `../scripts/`)

## Workflow Template

Each notebook typically follows this structure:

1. **Import and Setup**
   - Import libraries
   - Load configuration
   - Set display options

2. **Load Data**
   - Read from `data/processed/`
   - Display first few rows
   - Check shape and types

3. **Analysis**
   - Exploratory questions
   - Calculations and transformations
   - Visualizations

4. **Results**
   - Key findings
   - Save outputs to `outputs/`
   - Document next steps

5. **Cleanup**
   - Clear unnecessary cells
   - Document assumptions
   - Note for next analyst

## Code Reuse

**Don't:**
```python
# Copy-pasting functions across notebooks
def remove_outliers(data):
    ...  # Repeated in every notebook
```

**Do:**
```python
# Extract to scripts/, import in notebooks
from scripts.data_cleaning import remove_outliers

df_clean = remove_outliers(df)
```

## Best Practices

1. **Use meaningful titles:** "01_customer_segmentation_analysis"
2. **Document assumptions:** "Assuming transactions > $1000 are data errors"
3. **Save outputs:** Use consistent paths: `../outputs/visualizations/`
4. **Include markdown:** Explain what you're doing and why
5. **Version control:** Commit notebooks to git

## Example Notebook Structure

```
01_exploratory_analysis.ipynb

Cell 1 (Markdown): Title and Overview
Cell 2 (Code): Imports and Setup
Cell 3 (Code): Load Data
Cell 4 (Markdown): Data Quality Section
Cell 5 (Code): Check for missing values
Cell 6 (Markdown): Distribution Analysis
Cell 7 (Code): Create histograms
Cell 8 (Markdown): Key Findings
Cell 9 (Code): Save summary to outputs/
```

## Common Mistakes

❌ Storing multiple versions: `01_analysis.ipynb`, `01_analysis_v2.ipynb`
❌ All code in notebooks (functions should be in `scripts/`)
❌ Not using numbered prefixes
❌ Unclear titles
❌ No markdown documentation
❌ Outputs saved to `data/` instead of `outputs/`

---

**These are your working files.** Use them freely for exploration and iteration. Extract reusable code to `scripts/` and keep them focused on discovery.
