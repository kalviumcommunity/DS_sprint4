# Scripts

## Data Processing and Analysis Code

This folder contains Python scripts for processing raw data and generating outputs.

## Available Scripts

### clean_sales_data.py

**Purpose:** Clean and prepare sales transaction data

**Input:** data/raw/sales_transactions_raw.csv  
**Output:** data/processed/sales_cleaned.csv  
**Output:** data/processed/sales_cleaned_metadata.txt  

**What it does:**
1. Load raw sales data
2. Detect and remove duplicate rows
3. Validate data types
4. Save cleaned data to processed/
5. Create metadata file documenting changes

**Usage:**
```bash
python scripts/clean_sales_data.py
```

**Run time:** ~5 seconds

---

### engineer_features.py

**Purpose:** Create analysis-ready customer features

**Input:** data/processed/sales_cleaned.csv  
**Input:** data/raw/customer_profiles_raw.csv  
**Output:** data/processed/customer_features.csv  
**Output:** data/processed/customer_features_metadata.txt  

**What it does:**
1. Load processed sales and raw customer data
2. Merge sales with customer info
3. Calculate aggregate features:
   - total_orders
   - avg_order_value
   - days_since_signup
   - customer_segment (LTV-based)
4. Save feature matrix
5. Create metadata file

**Usage:**
```bash
python scripts/engineer_features.py
```

**Run time:** ~15 seconds

---

### train_models.py

**Purpose:** Train ML models and generate outputs

**Input:** data/processed/customer_features.csv  
**Output:** outputs/models/customer_segmentation_kmeans.pkl  
**Output:** outputs/models/purchase_prediction_xgboost.pkl  
**Output:** outputs/visualizations/feature_importance.png  
**Output:** outputs/reports/model_evaluation_summary.xlsx  

**What it does:**
1. Load feature matrix
2. Split into train (80%) / test (20%)
3. Train K-Means clustering model
4. Train XGBoost prediction model
5. Evaluate models
6. Save models and metadata
7. Generate visualizations
8. Create evaluation report

**Usage:**
```bash
python scripts/train_models.py
```

**Run time:** ~90 seconds

---

## Running the Complete Pipeline

**Step 1: Clean raw data**
```bash
python scripts/clean_sales_data.py
```
Output: data/processed/sales_cleaned.csv

**Step 2: Engineer features**
```bash
python scripts/engineer_features.py
```
Output: data/processed/customer_features.csv

**Step 3: Train models**
```bash
python scripts/train_models.py
```
Output: models + visualizations + reports

**Verify outputs:**
```bash
ls -lh data/processed/
ls -lh outputs/models/
ls -lh outputs/visualizations/
```

---

## Pipeline Architecture

```
RAW DATA
├─ data/raw/sales_transactions_raw.csv
├─ data/raw/customer_profiles_raw.csv
└─ data/raw/product_catalog_raw.csv
    ↓
[clean_sales_data.py]
    ↓
PROCESSED DATA
├─ data/processed/sales_cleaned.csv
└─ data/processed/sales_cleaned_metadata.txt
    ↓
[engineer_features.py]
    ↓
FEATURES
├─ data/processed/customer_features.csv
└─ data/processed/customer_features_metadata.txt
    ↓
[train_models.py]
    ↓
OUTPUTS
├─ outputs/models/
├─ outputs/visualizations/
└─ outputs/reports/
```

---

## Reproducibility

**Can someone else reproduce this?**

✓ YES, because:
- All data sources documented in data/raw/DATA_SOURCES.md
- Processing steps in metadata files
- Code in these scripts
- Scripts are deterministic (random_state=42)

**To reproduce:**
```bash
# Clone repo
git clone [repo]
cd [project]

# Run pipeline
python scripts/clean_sales_data.py
python scripts/engineer_features.py
python scripts/train_models.py

# Results should match original exactly (except models - slight randomness expected)
```

---

## Modifying Scripts

When improving scripts:

1. **Update the script file**
2. **Increment version in metadata**
3. **Regenerate outputs**
4. **Commit to git**

```bash
# After editing script
git add scripts/train_models.py
git commit -m "Improved model training (added cross-validation)"

# Regenerate all outputs
python scripts/train_models.py

# Commit updated outputs (if small)
git add outputs/
git commit -m "Regenerated outputs with improved model training"
```

---

## Dependency Management

**Required packages:**
- pandas >= 1.3.0
- scikit-learn >= 0.24.0
- xgboost >= 1.5.0
- matplotlib >= 3.3.0
- numpy >= 1.20.0

**Install:**
```bash
pip install -r requirements.txt
```

**Create requirements file:**
```bash
pip freeze > requirements.txt
```

---

## Troubleshooting

### Script fails: "File not found"
- Verify you're in project root directory
- Check file paths in script match your structure
- Run from: cd /path/to/project

### Script fails: "Module not found"
- Install dependencies: pip install -r requirements.txt
- Verify Python version: python --version

### Outputs don't match expected size
- Check input data file sizes
- Verify processing logic (no filters were applied)
- Check for errors in script logs

### Models don't load in predictions
- Verify you're using same Python version (v3.8+ required)
- Check feature order matches training

---

## Adding New Scripts

When creating new scripts:

1. **Descriptive filename**
   - ✓ process_weather_data.py
   - ✗ data_script.py

2. **Input/Output documented**
   ```python
   """
   Process weather data
   
   Input: data/raw/weather_2024.csv
   Output: data/processed/weather_daily.csv
   """
   ```

3. **Metadata file created**
   - Track processing steps
   - Document changes
   - Enable reproducibility

4. **Added to pipeline documentation**
   - Update this README
   - Explain when/where runs
   - Document dependencies

---

## Best Practices

✓ Keep scripts modular (one-purpose per script)  
✓ Use random_state=42 for reproducibility  
✓ Log progress to console  
✓ Create metadata files automatically  
✓ Never modify raw data within scripts  
✓ Test script with sample data first  
✓ Document all inputs/outputs clearly  
✓ Include error handling  

---

**Questions about these scripts?** Email data-team@company.com
