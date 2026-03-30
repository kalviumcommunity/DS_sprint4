# Configurations

**Purpose:** Centralized parameter and configuration management

## About Configs

This folder contains configuration files that centralize parameters and settings:
- Model hyperparameters
- Data paths and source information
- Processing parameters
- Output paths
- Database connections

## What Goes Here

- YAML configuration files
- JSON configuration files
- Feature lists
- Parameter sets
- Connection strings

## Naming Convention

Use descriptive names:

```
configs/
├── data_config.yaml         # Data sources and paths
├── model_config.yaml        # Model hyperparameters
├── feature_config.yaml      # Feature definitions
├── paths_config.yaml        # File paths
└── parameters.yaml          # General parameters
```

## Example: data_config.yaml

```yaml
data:
  raw:
    path: ./data/raw/
    files:
      - sales_data.csv
      - customer_demographics.xlsx
  processed:
    path: ./data/processed/
    output:
      - sales_cleaned.csv
      - customer_features.csv

validation:
  required_columns:
    - order_id
    - customer_id
    - amount
  date_format: '%Y-%m-%d'
  encoding: 'utf-8'
```

## Example: model_config.yaml

```yaml
model:
  type: random_forest
  
hyperparameters:
  n_estimators: 100
  max_depth: 15
  random_state: 42
  
training:
  test_size: 0.2
  validation_split: 0.1
  
output:
  model_path: ./outputs/models/
  model_filename: model_rf.pkl
```

## Using Configs in Code

### Load YAML Config:

```python
import yaml

def load_config(config_path):
    """Load YAML configuration file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

# In notebook
config = load_config('configs/parameters.yaml')
raw_path = config['data']['raw']['path']
test_size = config['training']['test_size']
```

### Use in Model Training:

```python
# Extract parameters
model_params = config['model']['hyperparameters']

# Create model
model = RandomForestClassifier(**model_params)
model.fit(X_train, y_train)
```

## Benefits

1. **Centralization:** Change parameters in one place
2. **Consistency:** Same parameters across notebooks and scripts
3. **Documentation:** Parameters are documented and tracked
4. **Version Control:** Easy to see what parameters changed
5. **Reproducibility:** Can re-run analysis with exact same parameters

## Secrets and Sensitive Data

**Do NOT store in version control:**
- API keys
- Database passwords
- Personal information
- Cloud credentials

**Instead:**
- Store in `.env` file (add to `.gitignore`)
- Use environment variables
- Store in secure configuration management tool

**Example: .env file (not committed)**
```
DATABASE_USER=admin
DATABASE_PASSWORD=secret123
API_KEY=sk-1234567890
```

**Load from environment:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv('DATABASE_USER')
api_key = os.getenv('API_KEY')
```

---

**Use configs for flexibility and reproducibility.** Keep parameters outside code so analysis is easy to adapt and reproduce.
