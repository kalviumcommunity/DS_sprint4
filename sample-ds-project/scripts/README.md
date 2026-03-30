# Scripts

**Purpose:** Reusable, production-ready Python code

## About Scripts

This folder contains standalone Python scripts that contain reusable functions extracted from notebooks. Scripts should be:
- Well-documented with docstrings
- Tested and reliable
- Reusable across notebooks
- Easy to maintain
- Follow Python best practices

## What Goes Here

- **data_cleaning.py:** Functions for loading, validating, cleaning data
- **feature_engineering.py:** Functions for creating features
- **model_training.py:** Functions for training models
- **utils.py:** Helper functions used across scripts
- **config_loader.py:** Functions for loading configuration

## What Does NOT Go Here

- ❌ Jupyter notebooks (use `../notebooks/`)
- ❌ One-off analysis (keep in notebooks first)
- ❌ Temporary test code
- ❌ Notebook-specific code (e.g., `%matplotlib`)

## Workflow: From Notebook to Script

**Step 1: Write in Notebook**
```python
# In a notebook cell
def remove_duplicates(df):
    return df.drop_duplicates()

df_clean = remove_duplicates(df_raw)
```

**Step 2: Extract to Script**
```python
# In scripts/data_cleaning.py
def remove_duplicates(df):
    """Remove duplicate rows from dataframe."""
    return df.drop_duplicates()
```

**Step 3: Import in Notebook**
```python
# Back in notebook
from scripts.data_cleaning import remove_duplicates

df_clean = remove_duplicates(df_raw)
```

## Code Organization

### Example: data_cleaning.py

```python
"""
Data cleaning utilities for customer dataset.

Functions:
    load_and_validate(): Load and validate data
    remove_duplicates(): Remove duplicate rows
    handle_missing_values(): Fill missing values
    remove_outliers(): Detect and remove outliers
"""

import pandas as pd
import numpy as np

def load_and_validate(file_path, required_columns=None):
    """
    Load CSV file and validate required columns exist.
    
    Args:
        file_path (str): Path to CSV file
        required_columns (list): Column names that must exist
        
    Returns:
        pd.DataFrame: Loaded and validated data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If required columns missing
        
    Example:
        >>> df = load_and_validate('data/raw/sales.csv', 
        ...     required_columns=['date', 'amount'])
    """
    df = pd.read_csv(file_path)
    
    if required_columns:
        missing = set(required_columns) - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")
    
    return df

def remove_duplicates(df):
    """Remove duplicate rows and return count."""
    initial_rows = len(df)
    df_clean = df.drop_duplicates()
    removed = initial_rows - len(df_clean)
    print(f"Removed {removed} duplicate rows")
    return df_clean
```

## Best Practices

### 1. Use Docstrings

```python
# ❌ No documentation
def clean_data(d):
    return d.drop_duplicates()

# ✓ Well documented
def clean_data(df):
    """Remove duplicate rows from dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.DataFrame: Dataframe with duplicates removed
    """
    return df.drop_duplicates()
```

### 2. Reusable Functions

```python
# ❌ Hardcoded paths (not reusable)
def clean_sales_data():
    df = pd.read_csv('data/raw/sales.csv')
    df = df.drop_duplicates()
    df.to_csv('data/processed/sales.csv')

# ✓ Parameters (reusable)
def clean_data(input_path, output_path=None):
    """Clean data and optionally save."""
    df = pd.read_csv(input_path)
    df = df.drop_duplicates()
    if output_path:
        df.to_csv(output_path)
    return df
```

### 3. Error Handling

```python
# ✓ Handle edge cases
def load_data(file_path):
    """Load data with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file at {file_path}")
    
    try:
        return pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        print(f"Warning: {file_path} is empty")
        return pd.DataFrame()
```

### 4. Imports Organization

```python
# Standard library imports first
import os
import json
from datetime import datetime

# Third-party imports second
import pandas as pd
import numpy as np

# Local imports last
from scripts.utils import load_config
```

## Example File Structure

```
scripts/
├── __init__.py                  # Makes scripts a package
├── data_cleaning.py             # Data loading and cleaning
├── feature_engineering.py       # Feature creation
├── model_training.py           # Model training utilities
├── utils.py                    # Helper functions
└── config_loader.py            # Configuration handling
```

## Using Scripts in Notebooks

**Import and Use:**
```python
# At top of notebook
from scripts.data_cleaning import load_and_validate, remove_duplicates
from scripts.feature_engineering import engineer_features
from scripts.utils import load_config

# In notebook cell
config = load_config('configs/parameters.yaml')
df = load_and_validate('data/raw/sales.csv')
df_clean = remove_duplicates(df)
df_features = engineer_features(df_clean, config)
```

## Naming Conventions

**File names:**
- Use descriptive names: `data_cleaning.py` (not `utils_v2.py`)
- Use lowercase with underscores: `feature_engineering.py` (not `FeatureEngineering.py`)
- One purpose per file when practical

**Function names:**
- Use descriptive names: `remove_duplicates()` (not `clean()`)
- Use lowercase with underscores: `load_and_validate()` (not `loadAndValidate()`)

## Testing (Optional)

Consider creating test functions:

```python
# In scripts/data_cleaning.py
from scripts.data_cleaning import remove_duplicates

def test_remove_duplicates():
    """Test remove_duplicates function."""
    df = pd.DataFrame({'a': [1, 1, 2], 'b': [3, 3, 4]})
    result = remove_duplicates(df)
    assert len(result) == 2
    print("✓ Test passed")

if __name__ == '__main__':
    test_remove_duplicates()
```

---

**Extract once, use many times.** Code in scripts should be reusable and reliable. Notebooks should stay focused on exploration and analysis.
