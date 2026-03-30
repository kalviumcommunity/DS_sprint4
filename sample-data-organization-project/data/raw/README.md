# Raw Data

## Sacred Rule: NEVER Modify These Files

This folder contains original, unmodified data exactly as received from source systems.

### Why Raw Data is Immutable

**If raw data is corrupted:**
- No way to reproduce original results
- No audit trail of what changed
- Colleagues can't verify your work
- Backup copy lost accidentally

**If raw data is protected:**
- Always reproducible ✓
- Full audit trail ✓
- Prevents accidental mistakes ✓
- Serves as backup ✓

### Files in This Folder

#### sales_transactions_raw.csv

**Source:** Shopify API export  
**Date Received:** 2024-01-15 14:00 UTC  
**Total Records:** 250,000  
**Size:** 50 MB  

**Columns:**
- `order_id` - Unique order identifier
- `customer_id` - Customer reference
- `amount` - Order total (USD)
- `date` - Purchase date
- `region` - Geographic region
- `status` - Order status (completed, cancelled, pending)

**Data Quality Notes:**
- Some cancelled orders included (status='cancelled')
- May contain duplicate rows (0.8%)
- No data cleaning applied
- Ready for processing pipeline

#### customer_profiles_raw.csv

**Source:** CRM Database export  
**Date Received:** 2024-01-14 10:30 UTC  
**Total Records:** 50,000  
**Size:** 12 MB  

**Columns:**
- `customer_id` - Unique customer ID
- `name` - Customer name
- `email` - Email address
- `signup_date` - Account creation date
- `country` - Country code
- `lifetime_value` - Total spent (USD)

**Data Quality Notes:**
- No email validation applied
- May have duplicate customers (estimated 2%)
- Missing country for some users (5%)
- All records unmodified from source

#### product_catalog_raw.csv

**Source:** Inventory Management System  
**Date Received:** 2024-01-15 09:00 UTC  
**Total Records:** 10,000  
**Size:** 5 MB  

**Columns:**
- `product_id` - Unique product identifier
- `name` - Product name
- `category` - Product category
- `price` - Retail price (USD)
- `discontinued` - Boolean (product active or discontinued)

**Data Quality Notes:**
- Includes discontinued products
- No formatting standardization
- Raw from system export
- Unmodified

### Data Source Documentation

See [DATA_SOURCES.md](DATA_SOURCES.md) for complete source information.

### How to Use Raw Data

✓ **DO:**
```python
# Read raw data (safe, no modifications)
df_raw = pd.read_csv('sales_transactions_raw.csv')
print(f"Loaded {len(df_raw)} records")
```

✓ **DO:**
```python
# Create a copy for processing
df_process = df_raw.copy()
df_process = df_process.drop_duplicates()
```

✗ **DON'T:**
```python
# Modify in place and save (CORRUPTS RAW DATA!)
df_raw.drop_duplicates(inplace=True)
df_raw.to_csv('sales_transactions_raw.csv')  # ❌ WRONG!
```

✗ **DON'T:**
```python
# Delete/rename raw files
os.remove('customer_profiles_raw.csv')  # ❌ WRONG!
os.rename('product_catalog_raw.csv', 'products.csv')  # ❌ WRONG!
```

### Protecting Raw Data

#### Method 1: Read-Only File Permissions

```bash
# Linux/Mac
chmod 444 *.csv

# Windows PowerShell
Get-Item '*.csv' | ForEach-Object { $_.Attributes = 'ReadOnly' }
```

After setting read-only, accidental modifications are blocked:
```python
# This will raise an error (good!)
df_raw.to_csv('sales_transactions_raw.csv')
# PermissionError: Cannot write to read-only file
```

#### Method 2: `.gitignore` (don't overwrite)

In project `.gitignore`:
```
# Keep raw data files but never overwrite them
data/raw/*_raw.csv

# Always use new names
data/processed/*.csv
```

#### Method 3: Script Guards

```python
"""
Script to process raw data
IMPORTANT: Never modify raw data directly
"""

import os
from pathlib import Path

# Verify we're not accidentally overwriting raw data
raw_folder = Path('data/raw')
output_folder = Path('data/processed')

def process_data(raw_file):
    """Process raw data create processed output."""
    
    # Guard: refuse if trying to write to raw/ folder
    if 'raw' in str(raw_file):
        raise ValueError("❌ STOP: Never save to raw folder!")
    
    # Guard: refuse if overwriting file without _processed suffix
    if '_processed' not in str(raw_file):
        raise ValueError("❌ Use _processed in filename!")
    
    # Safe to proceed
    print("✓ Processing safe - correct filename/folder")
```

### Access Control

**Who can modify?** Nobody. Raw data is read-only.

**Who can read?** Anyone on team (tracking in git history).

**Who manages?** Data owner (see [DATA_SOURCES.md](DATA_SOURCES.md)).

### Backup and Disaster Recovery

If raw data is corrupted or lost:

1. **From version control:**
   ```bash
   git checkout data/raw/sales_transactions_raw.csv
   ```

2. **From source:**
   - See [DATA_SOURCES.md](DATA_SOURCES.md) for re-export instructions
   - Contact data owner

### Verification Checklist

- [ ] All raw files unchanged from source date
- [ ] File sizes match documentation
- [ ] No processing applied (still in original format)
- [ ] Files marked as read-only (if possible)
- [ ] Backup exists in git history
- [ ] Data source documented

### Common Questions

**Q: What if data has an error?**  
A: Keep it! Errors are truthful records. Document in processing and clean in processed/ folder.

**Q: Can I delete old raw data?**  
A: Not unless explicitly approved. Raw data is backup against data loss.

**Q: What if raw data is huge (> 1 GB)?**  
A: Use git-lfs (Large File Storage) but same principles apply - immutable once stored.

**Q: How often update raw data?**  
A: Depends on source. See [DATA_SOURCES.md](DATA_SOURCES.md) for refresh frequency.

---

**Remember:** Raw data is your single source of truth. Protect it fiercely.
