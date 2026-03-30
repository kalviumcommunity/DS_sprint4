# Models

## Trained Machine Learning Models

This folder contains serialized trained models ready for prediction or further evaluation.

## What Goes Here

- Trained ML models (.pkl, .h5, .joblib)
- Model metadata and configuration
- Feature importance data
- Model evaluation metrics

## Example Files

**customer_segmentation_kmeans.pkl**
- Type: K-Means clustering model
- Trained on: 40,000 customer records
- Date: 2024-01-16
- Purpose: Segment customers into 4 groups

**purchase_prediction_xgboost.pkl**
- Type: XGBoost classifier
- Trained on: 40,000 records (train set)
- Tested on: 10,000 records (test set)
- Accuracy: 92%
- Purpose: Predict if customer will purchase

## How to Use

```python
import pickle
import pandas as pd

# Load model
with open('customer_segmentation_kmeans.pkl', 'rb') as f:
    model = pickle.load(f)

# Prepare new data (same features as training)
new_data = pd.read_csv('../data/processed/new_customers.csv')
features = ['total_orders', 'avg_order_value', 'days_since_signup', 
            'lifetime_value', 'region_encoded', 'purchase_frequency', 
            'avg_days_between_orders', 'recency_days']

# Make predictions
predictions = model.predict(new_data[features])

# Use results
new_data['segment'] = predictions
```

## Model Metadata Files

For each model, create a metadata file:

**customer_segmentation_kmeans_meta.txt**
- Algorithm and hyperparameters
- Training data and date
- Performance metrics
- Features used (exact order!)
- Production status
- Last update date

Read metadata before using model to understand:
- What data was used for training
- How well it performs
- If it's still current/maintained

## Best Practices

✓ Save models with clear names  
✓ Create metadata file for each model  
✓ Document features required (order matters)  
✓ Track model version/date  
✓ Never modify models in place  
✓ Archive old models (keep in git history)  

## Sharing Models

If sharing with team:
```bash
# Include both model and metadata
- customer_segmentation_kmeans.pkl
- customer_segmentation_kmeans_meta.txt
```

Team can load and use immediately with full context from metadata.
