# Data Sources

## Documentation of Raw Data Origins

This file documents where each raw data file came from and how to obtain updated versions.

## Data Inventory

### sales_transactions_raw.csv

**Filename:** sales_transactions_raw.csv  
**Date Received:** 2024-01-15 14:00 UTC  
**Total Records:** 250,000  
**Size:** 50 MB  

**Source Information:**
- **System:** Shopify Store API
- **Endpoint:** `/admin/api/2024-01/orders.json`
- **Access:** API credentials in 1Password (vault: Data Team)
- **Authentication:** Bearer token (expires annually)

**Export Process:**
```bash
# Manual export via Shopify
1. Login to Shopify admin panel
2. Reports > Orders export
3. Select date range: 2024-01-01 to 2024-01-31
4. Format: CSV
5. Download and save to data/raw/

# OR API export (via scripts)
python scripts/export_shopify_orders.py --output data/raw/sales_transactions_raw.csv
```

**Update Frequency:** Daily (or as needed)  
**Last Verified:** 2024-01-15  

**Data Quality Notes:**
- Some orders duplicate (estimated 0.8%)
- Includes cancelled orders (status='cancelled')
- No data validation or cleaning applied
- All fields exported as-is from Shopify
- Timezone: UTC

**Contact:** Data team lead (john@company.com)

---

### customer_profiles_raw.csv

**Filename:** customer_profiles_raw.csv  
**Date Received:** 2024-01-14 10:30 UTC  
**Total Records:** 50,000  
**Size:** 12 MB  

**Source Information:**
- **System:** HubSpot CRM
- **Report:** Custom contact export
- **Access:** HubSpot admin account (see 1Password)
- **Database:** Production CRM (safe to export)

**Export Process:**
```bash
# Via HubSpot interface
1. Login to HubSpot
2. Contacts > Export contacts
3. Select all fields
4. Format: CSV
5. Download and save to data/raw/

# OR via API
python scripts/export_hubspot_contacts.py --output data/raw/customer_profiles_raw.csv
```

**Update Frequency:** Weekly (sync on Mondays)  
**Last Verified:** 2024-01-14  

**Data Quality Notes:**
- May have 2-3% duplicate customers
- Some missing email addresses (5%)
- Country field missing for international customers
- Timezone: UTC

**Contact:** CRM admin (jane@company.com)

---

### product_catalog_raw.csv

**Filename:** product_catalog_raw.csv  
**Date Received:** 2024-01-15 09:00 UTC  
**Total Records:** 10,000 products  
**Size:** 5 MB  

**Source Information:**
- **System:** Shopify Product Database
- **Export Method:** Shopify admin > Products > Export all
- **Frequency:** Daily snapshot
- **Includes:** Active and discontinued products

**Export Process:**
```bash
# Manual export
1. Shopify admin > Products
2. Select all > Export
3. Format: CSV with all columns
4. Save to data/raw/

# OR API export
python scripts/export_shopify_products.py --output data/raw/product_catalog_raw.csv
```

**Update Frequency:** Daily  
**Last Verified:** 2024-01-15  

**Data Quality Notes:**
- Includes both active and discontinued products
- Pricing in USD
- No filtering or modification from system
- Best-sell ranking not included in export

**Contact:** Product team (products@company.com)

---

## How to Re-Export Data

### If raw data is lost or corrupted:

```bash
# Step 1: Verify current raw file
ls -lh data/raw/

# Step 2: Delete corrupted file (after backup)
rm data/raw/sales_transactions_raw.csv

# Step 3: Re-export from source
python scripts/export_shopify_orders.py \
    --start_date 2024-01-01 \
    --end_date 2024-01-31 \
    --output data/raw/sales_transactions_raw.csv

# Step 4: Verify new file
wc -l data/raw/sales_transactions_raw.csv
# Should show ~250,000 lines (excluding header)

# Step 5: Add to git (if tracking raw data)
git add data/raw/sales_transactions_raw.csv
git commit -m "Re-export raw sales data from Shopify"
```

## Data Access and Permissions

### Who has access to raw data?

| Role | System | Access | Restrictions |
|------|--------|--------|--------------|
| Data Team | All | Read/Write | Only for updates |
| Analytics Team | Sales/Products | Read | No modifications |
| Developers | Sales/Products | Read | For model training |
| Executives | None | Dashboard only | Via reports only |

### API Credentials

Stored in 1Password vault "Data Team":

- **Shopify API Key:** [in 1Password]
- **Shopify API Password:** [in 1Password]
- **HubSpot API Key:** [in 1Password]

**Never commit credentials to git!** Use environment variables:

```python
import os

SHOPIFY_KEY = os.environ.get('SHOPIFY_API_KEY')
SHOPIFY_PASS = os.environ.get('SHOPIFY_API_PASSWORD')
```

## Data Quality Verification

Before using raw data in analysis, verify:

```bash
# Check file exists and is recent
ls -l data/raw/sales_transactions_raw.csv

# Check total records
wc -l data/raw/sales_transactions_raw.csv
# Expected: ~250,000 (±5% ok)

# Check column headers
head -1 data/raw/sales_transactions_raw.csv

# Check for obvious corruption
tail -20 data/raw/sales_transactions_raw.csv
# (should have complete rows, not abrupt endings)

# Spot check data
python
>>> import pandas as pd
>>> df = pd.read_csv('data/raw/sales_transactions_raw.csv')
>>> df.head()
>>> df.info()
>>> df.describe()
```

## Troubleshooting Data Issues

### Issue: File doesn't match expected size

**Solution:**
1. Check export date in source system
2. Verify date range includes expected period
3. Check if data still included (not archived/deleted)
4. Re-export with correct date range

### Issue: Column count is different

**Solution:**
1. Verify which columns are included
2. Check if system added/removed columns
3. Request manual export with all columns
4. Compare to previous export

### Issue: Row count anomaly

**Solution:**
1. Check if include/exclude deleted records
2. Verify date range is correct
3. Check for filters applied in source system
4. Run count query in source database

### Issue: Cannot access source system

**Solution:**
1. Verify API credentials in 1Password
2. Check if API key expired (expires annually)
3. Verify network/VPN connection
4. Contact system owner for access restoration

## Archival and Retention

### How long to keep raw data?

**Policy:**
- Keep current + 3 months of daily exports
- Archive older (monthly snapshots)
- Delete very old (> 1 year)

**Example:**
```
data/raw/
├── sales_daily/
│   ├── sales_2024_01_15.csv (current)
│   ├── sales_2024_01_14.csv (recent)
│   └── sales_2024_01_01.csv (old)
└── sales_archive/
    ├── sales_2023_12.csv    (monthly snapshot)
    └── sales_2023_11.csv
```

### Retention schedule:
- **Current month:** Keep all daily exports
- **Last 2 months:** Keep daily exports
- **Older:** Keep 1 monthly snapshot only
- **> 1 year:** Consider deletion (check with legal)

---

## Contact Information

### Data Owners

| Data Source | Owner | Email | Phone |
|-------------|-------|-------|-------|
| Shopify Sales | John Smith | john@company.com | (555) 123-4567 |
| HubSpot CRM | Jane Doe | jane@company.com | (555) 234-5678 |
| Product Catalog | Rick Johnson | prod@company.com | (555) 345-6789 |

### For Questions

**Data access issues:** Contact your data owner  
**Export problems:** Email data-team@company.com  
**API issues:** File ticket in company Jira  

---

## Compliance Notes

⚠️ **Data Privacy:** All data contains customer information (PII)
- Secure storage (encrypted drives)
- Limited access (need-to-know basis)
- Don't share externally
- GDPR compliant (retention policy)

⚠️ **Data Security:**
- Store credentials in 1Password only
- Never commit passwords
- Use VPN for remote access
- Report breaches immediately

---

This file is the single source of truth for data provenance. When others ask "Where did this data come from?", they should find the answer here.
