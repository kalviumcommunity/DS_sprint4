# Processed Data

## Cleaned, Transformed, Analysis-Ready Data

This folder contains data that has been cleaned and transformed from raw sources. Every file here is derived from raw data and is reproducible.

### Key Principles

✓ **Derived from raw data** - Created through documented transformations  
✓ **Recreatable** - Run processing script to regenerate  
✓ **Documented** - Metadata file accompanying each file  
✓ **Multiple versions OK** - Different approaches can have v1, v2, etc.  
✓ **Always traceable** - Can point to exact raw files used  

### Files in This Folder

#### sales_cleaned.csv

**Source:** `data/raw/sales_transactions_raw.csv`  
**Processing:** `scripts/clean_sales_data.py`  
**Created:** 2024-01-16 10:30 UTC  
**Records:** 248,500 (2 duplicates removed, rest unchanged)  
**Size:** 48 MB  

**What Changed:**
```
Processing Steps:
✓ 1. Loaded 250,000 raw records
✓ 2. Detected 2 duplicate rows
✓ 3. Removed duplicates
✓ 4. Result: 248,500 clean records

Quality Metrics:
- Nulls: None (no missing values)
- Date range: 2024-01-01 to 2024-01-31 ✓
- Negative amounts: 0 ✓
- Status values: completed, cancelled, pending ✓
```

**When to use:** Starting point for all analysis  
**See also:** `sales_cleaned_metadata.txt` for full processing details

#### customer_features.csv

**Source:** `data/raw/customer_profiles_raw.csv` (merged with sales_cleaned.csv)  
**Processing:** `scripts/engineer_features.py`  
**Created:** 2024-01-16 11:15 UTC  
**Records:** 50,000  
**Size:** 15 MB  

**New Columns Added:**
- `total_orders` - Count of purchases
- `avg_order_value` - Average transaction amount
- `days_since_signup` - Days since account created
- `customer_segment` - Tier based on LTV
- `region_code` - Standardized country codes

**Quality Metrics:**
- Duplicates handled: 2 duplicate customers merged
- Missing values: Countries filled with 'UNKNOWN' (2.5%)
- Validation: All 50,000 records linked to customers ✓

**When to use:** Feature engineering for ML models  
**See also:** `customer_features_metadata.txt`

#### train_set_80pct.csv

**Source:** `customer_features.csv`  
**Processing:** `scripts/train_models.py`  
**Created:** 2024-01-16 12:00 UTC  
**Records:** 40,000 (80% of 50,000)  
**Size:** 12 MB  

**Purpose:** ML model training set  
**Random Seed:** 42 (reproducible)  
**Includes:** All features from customer_features.csv  

#### test_set_20pct.csv

**Source:** `customer_features.csv`  
**Processing:** `scripts/train_models.py`  
**Created:** 2024-01-16 12:00 UTC  
**Records:** 10,000 (20% of 50,000)  
**Size:** 3 MB  

**Purpose:** ML model evaluation set  
**Random Seed:** 42 (reproducible)  
**Includes:** All features from customer_features.csv  

### Metadata Files

Every processed data file has an accompanying `*_metadata.txt` file:

```
PROCESSING METADATA
====================

File Name: sales_cleaned.csv
Created: 2024-01-16 10:30 UTC
Created By: clean_sales_data.py (line 42)

SOURCE DATA:
- Source File: data/raw/sales_transactions_raw.csv
- Source Records: 250,000

PROCESSING STEPS:
1. Load CSV with validation
   ✓ Encoding: utf-8
   ✓ Delimeter: comma
   ✓ Date parsing enabled

2. Detect duplicates
   ✓ Method: Exact row duplicates
   ✓ Found: 2 duplicates (0.008%)

3. Remove duplicates
   ✓ Rows before: 250,000
   ✓ Rows after: 248,500
   ✓ Data removed: 2 records

4. Validation checks
   ✓ Date range: 2024-01-01 to 2024-01-31
   ✓ Negative amounts: 0 ✗
   ✓ Null values: 0 ✗

FINAL RESULT:
- Output File: sales_cleaned.csv
- Final Records: 248,500
- Data Loss: 2 records (0.008%)

REPRODUCIBILITY:
- Run: python scripts/clean_sales_data.py
- Input: data/raw/sales_transactions_raw.csv
- Output: data/processed/sales_cleaned.csv
- Can regenerate: Yes ✓

QA/VALIDATION:
- Approved for use: Yes ✓
```

**Always review metadata before using data!**

### Naming Convention

**Format:** `[entity]_[transformation]_[version].csv`

**Examples in this folder:**
```
sales_cleaned.csv               ← Simple transformation
customer_features.csv           ← Feature engineering
sales_merged_customers.csv      ← Source combination
train_set_80pct.csv             ← Train/test split
test_set_20pct.csv              ← Train/test split
```

### Data Versioning

When creating multiple approaches, version explicitly:

```
data/processed/
├── features_v1_initial.csv          ← First attempt
├── features_v1_initial_metadata.txt

├── features_v2_temporal_added.csv   ← Added time features
├── features_v2_temporal_added_metadata.txt

└── features_LATEST.csv              ← Current in use
```

Each version is:
- ✓ Separate file
- ✓ Independently documented
- ✓ Fully reproducible
- ✓ Stored with metadata

### How to Use Processed Data

✓ **DO - Reproducible Workflow:**
```python
# 1. Load processed data (already clean)
df_clean = pd.read_csv('data/processed/sales_cleaned.csv')
print(f"Loaded {len(df_clean)} records")

# 2. Check metadata to understand transformations
with open('data/processed/sales_cleaned_metadata.txt') as f:
    print(f.read())

# 3. Use for analysis
analysis = df_clean.groupby('region')['amount'].mean()
print(analysis)
```

✓ **DO - Feature Engineering with New Columns:**
```python
# Create new processed version without modifying original
df = pd.read_csv('data/processed/sales_cleaned.csv')
df_new = df.copy()
df_new['day_of_week'] = pd.to_datetime(df_new['date']).dt.day_name()
df_new.to_csv('data/processed/sales_with_day_of_week.csv')
```

✗ **DON'T - Modify in Place:**
```python
# Never overwrite original processed file
df = pd.read_csv('data/processed/sales_cleaned.csv')
df.drop_duplicates(inplace=True)  # ❌ WRONG!
df.to_csv('data/processed/sales_cleaned.csv')  # ❌ Overwrites!
```

### Creating New Processed Data

When processing raw data:

1. **Read from raw/**
   ```python
   df = pd.read_csv('data/raw/sales_transactions_raw.csv')
   ```

2. **Create working copy**
   ```python
   df_processed = df.copy()
   ```

3. **Apply transformations**
   ```python
   df_processed = df_processed.drop_duplicates()
   df_processed = df_processed.fillna(0)
   ```

4. **Save to processed/**
   ```python
   df_processed.to_csv('data/processed/sales_cleaned.csv', index=False)
   ```

5. **Create metadata file**
   ```python
   metadata = """
   PROCESSING METADATA
   File: sales_cleaned.csv
   Source: data/raw/sales_transactions_raw.csv
   Processing: remove duplicates, fill nulls
   Records: {input} → {output}
   Date: 2024-01-16 10:30 UTC
   """.format(input=len(df), output=len(df_processed))
   
   with open('data/processed/sales_cleaned_metadata.txt', 'w') as f:
       f.write(metadata)
   ```

### Processing Layers (for Complex Projects)

For large projects, organize processed data by transformation stage:

```
data/processed/
├── 01_cleaned/
│   ├── sales_duplicates_removed.csv
│   ├── customers_nulls_filled.csv
│   └── products_types_fixed.csv
│
├── 02_transformed/
│   ├── sales_normalized.csv
│   ├── customers_aggregated.csv
│   └── products_categorized.csv
│
├── 03_engineered/
│   ├── features_temporal.csv
│   ├── features_statistical.csv
│   └── features_combined.csv
│
└── 04_ready_for_ml/
    ├── train_set.csv
    └── test_set.csv
```

### Quality Assurance Checklist

Before using processed data, verify:

- [ ] Metadata file exists and is recent
- [ ] Source raw file documented
- [ ] Processing steps clearly recorded
- [ ] Null values handled (documented how)
- [ ] Duplicates dealt with (if applicable)
- [ ] Record counts changed documented
- [ ] Data validated (ranges, types, formats)
- [ ] File size reasonable
- [ ] Can point to exact code that created it

### Common Questions

**Q: Why keep processed files if I can regenerate?**  
A: Speed! Processing can take 10 minutes. Keep for reference while iterating.

**Q: Should I commit processed data to git?**  
A: Only if < 100 MB. For larger files, use git-lfs or external storage.

**Q: What if raw data updates?**  
A: Reprocess! Delete processed/ files and run scripts again.

**Q: Can I delete old processed files?**  
A: Yes, after confirming nobody needs them. Reprocess if needed.

**Q: How long to keep versions?**  
A: Keep current + 1-2 old. Delete ancient versions.

---

**Key Principle:** Processed data is fast-replaying raw data through documented transformations.
