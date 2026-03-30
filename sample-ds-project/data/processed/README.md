# Processed Data

**Purpose:** Cleaned, transformed, analysis-ready data

## About Processed Data

This folder contains data that has been cleaned, transformed, and is ready for analysis. These files are generated from `data/raw/` through cleaning and transformation scripts.

## What Goes Here

- Cleaned datasets (duplicates removed, missing values handled)
- Merged/joined datasets
- Feature-engineered data
- Normalized/standardized data
- Train/test splits
- Aggregated datasets

## What Does NOT Go Here

- ❌ Raw, unmodified data (belongs in `../raw/`)
- ❌ Temporary intermediate files
- ❌ Large generated datasets (move to `../outputs/`)
- ❌ Personal experiments (use separate folder)

## Naming Convention

Include what was done in the filename:

**Good:**
- `customer_data_cleaned_duplicates_removed.csv`
- `sales_data_merged_with_demographics.csv`
- `features_engineered_v2.csv`
- `train_set_80pct.csv`
- `test_set_20pct.csv`

**Bad:**
- `data.csv` (what data?)
- `processed.csv` (what was done?)
- `final.csv` (is this final?)
- `data_v2.csv` (unclear what version changed)

## Documentation

Consider creating a processing log for each file:

**Example: `customer_data_cleaned_duplicates_removed_notes.txt`**

```
Processing steps for customer_data_cleaned_duplicates_removed.csv

Source: ../raw/customer_database_export_2024-01-15.csv
Date Created: 2024-01-16

Processing Steps:
1. Loaded original file
2. Removed duplicate rows: 25,000 → 24,995 rows (5 duplicates)
3. Verified required columns present:
   - customer_id ✓
   - name ✓
   - email ✓
   - created_date ✓
4. Checked data types
5. Saved to processed/

Final Stats:
- Records: 24,995
- Columns: 4
- Missing values: 0
- Date created: 2024-01-16 14:30 UTC
```

## Workflow

```
Raw Data (../raw/) 
    ↓
[scripts/data_cleaning.py]
    ↓
Processed Data (this folder)
    ↓
[notebooks/analysis.ipynb]
    ↓
[outputs/]
```

## Versioning

Document why versions exist if you create multiple:

**Acceptable:**
- `customer_features_v1.csv` – First pass
- `customer_features_v2.csv` – Added more features
- `customer_features_LATEST.csv` – Current version (use in scripts)

**Better:** Use git branches instead of file versions

## Example Structure

```
processed/
├── customer_data_cleaned.csv
├── customer_data_cleaned_notes.txt
├── customer_features_engineered.csv
├── train_set_80pct.csv
└── test_set_20pct.csv
```

---

**Trust this data:** It's been through cleaning steps and documented. Use this for your analysis.
