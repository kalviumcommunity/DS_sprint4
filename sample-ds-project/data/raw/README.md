# Raw Data

**Purpose:** Store original, immutable source data

**Key Rule:** NEVER modify files in this folder

## About Raw Data

This folder contains the original datasets exactly as received from their sources. These files should never be modified or overwritten.

## Why Immutability Matters

1. **Reproducibility:** Can always re-run analysis from the original source
2. **Audit Trail:** Know the exact source data used
3. **Data Integrity:** Original data is preserved as backup
4. **Debugging:** If processed data is wrong, raw data is unchanged

## What Goes Here

- CSV/Excel downloads
- Database exports
- API responses (saved)
- External data sources
- Vendor-provided datasets

## What Does NOT Go Here

- ❌ Cleaned versions
- ❌ Data after any transformation
- ❌ Intermediate processing steps
- ❌ Feature-engineered data
- ❌ Train/test splits

## Workflow

```
Raw Data (this folder) → Processing Script → Processed Data (../processed/)
```

## Example

```
raw/
├── customer_database_export_2024-01-15.csv
├── sales_transaction_api_2024-01-01-to-01-31.csv
└── competitor_pricing_web_scrape_2024-01-15.csv
```

## Documentation

Create a `README.md` in this folder (optional but recommended) that documents:

```markdown
# Raw Data Sources

## customer_database_export_2024-01-15.csv
- **Source:** Export from Salesforce
- **Date:** 2024-01-15
- **Records:** 25,000
- **Columns:** customer_id, name, email, created_date, segment
- **Notes:** Updated weekly; this is January 15 snapshot

## sales_transaction_api_2024-01-01-to-01-31.csv
- **Source:** Internal API /transactions endpoint
- **Date Range:** 2024-01-01 to 2024-01-31
- **Records:** 50,000
- **Columns:** transaction_id, customer_id, amount, date, region
- **Notes:** Excludes failed transactions
```

---

**Remember:** This is your single source of truth. Protect these files!
