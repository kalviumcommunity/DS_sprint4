# Output Artifacts

## Models, Visualizations, and Reports

This folder contains generated output artifacts from analysis and modeling. These files are **disposable** - they can be regenerated from processed data at any time.

### Key Principles

✓ **Regenerable** - Recreate from processed data anytime  
✓ **Organized by purpose** - Models/visualizations/reports in separate folders  
✓ **Timestamped** - Know when created  
✓ **Not backed up obsessively** - Can reproduce, so not mission-critical  
✓ **Separate from data** - Never mix outputs with input data  

### Folder Structure

```
outputs/
├── models/            ← Trained machine learning models
├── visualizations/    ← Plots, charts, images
└── reports/          ← Analysis summaries, HTML, Excel
```

---

## models/

### What Goes Here

Serialized trained machine learning models and associated metadata:

```
models/
├── customer_segmentation_kmeans.pkl      ← Trained K-Means model
├── customer_segmentation_kmeans_meta.txt ← Model metadata
├── purchase_prediction_xgboost.pkl      ← XGBoost model
├── purchase_prediction_xgboost_meta.txt ← Model metadata
└── model_evaluation_metrics.csv          ← Performance scores
```

### Model Files (.pkl format)

**Format**: Pickle (standard Python serialization)

**Created by**: `scripts/train_models.py`

**Metadata Example** (customer_segmentation_kmeans_meta.txt):

```
MODEL METADATA
==============

Model Name: customer_segmentation_kmeans
Algorithm: K-Means Clustering
Training Date: 2024-01-16 13:45 UTC
Training Data: data/processed/customer_features.csv (40,000 rows)

HYPERPARAMETERS:
- n_clusters: 4
- max_iter: 300
- random_state: 42
- init: 'k-means++'

PERFORMANCE:
- Silhouette Score: 0.58
- Inertia: 45,230
- Convergence: Achieved in 12 iterations

FEATURES USED: (8 features)
1. total_orders - Customer purchase count
2. avg_order_value - Average transaction size
3. days_since_signup - Account age
4. lifetime_value - Total spent (USD)
5. region_encoded - Geographic region
6. purchase_frequency - Orders per month
7. avg_days_between_orders - Purchase interval
8. recency_days - Days since last purchase

CLUSTER ASSIGNMENT:
- Cluster 0: Premium (4,500 customers, high LTV)
- Cluster 1: Active (12,000 customers, frequent purchases)
- Cluster 2: Casual (18,500 customers, occasional)
- Cluster 3: At-Risk (5,000 customers, inactive)

PRODUCTION STATUS:
- Status: Active ✓
- Model ID: SKU_KMEANS_20240116
- Version: 1.0
- Last Updated: 2024-01-16
- Next Review: 2024-02-16

REPRODUCIBILITY:
- Training Script: scripts/train_models.py (line 185)
- Random Seed: 42 (reproducible) ✓
- Run Duration: 45 seconds
- Can rebuild: Yes ✓

NOTES:
- Model used for customer targeting campaign
- Retrains monthly with new data
- Requires features 1-8 in exact order
```

### Using Models in Production

```python
import pickle

# Load trained model
with open('outputs/models/customer_segmentation_kmeans.pkl', 'rb') as f:
    model = pickle.load(f)

# Predict on new data
new_customers = pd.read_csv('data/processed/new_customers.csv')
clusters = model.predict(new_customers[FEATURE_COLUMNS])

# Apply results
new_customers['segment'] = clusters
```

### Model Lifecycle

```
Day 1: Train model
├─ Save to models/ folder
├─ Create metadata file
└─ Document performance

Week 1-3: Monitor in production
├─ Check predictions quality
├─ Track any issues
└─ Collect feedback

Month 1: Review performance
├─ Compare to baseline
├─ Decide: keep, retrain, or replace
└─ Document any changes

Quarterly: Archive old model
├─ Keep for historical reference
├─ But replace with new version
└─ Free up disk space
```

---

## visualizations/

### What Goes Here

Plots, charts, and graphs for reporting and presentation:

```
visualizations/
├── sales_trend_2024.png             ← Line chart (monthly sales)
├── customer_segments.png            ← Scatter plot (segment visualization)
├── feature_importance.png           ← Bar chart (model features)
├── correlation_matrix.pdf           ← Heatmap
└── forecast_comparison.pdf          ← Multiple subplots
```

### Creating High-Quality Visualizations

**Resolution:** Save at 300 DPI for publication quality

```python
import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Add plot
ax.plot(dates, sales, marker='o', linewidth=2)
ax.set_title('Sales Trend 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Sales ($)')
ax.grid(True, alpha=0.3)

# Save at high resolution
plt.savefig('outputs/visualizations/sales_trend_2024.png', 
            dpi=300,                    # High resolution
            bbox_inches='tight',        # Remove white space
            facecolor='white')
plt.close()

print("✓ Saved: outputs/visualizations/sales_trend_2024.png")
```

### File Format Guidelines

| Format | Use Case | Quality | Size |
|--------|----------|---------|------|
| **PNG** | Web, slides | Good @ 300 DPI | Medium |
| **PDF** | Printed reports | Excellent | Medium |
| **SVG** | Scalable graphics | Vector (infinite) | Small |
| **JPG** | Compact images | Okay (compressed) | Small |

**Recommendation:** PNG 300 DPI for most use cases

### Naming Conventions

**Good:**
```
sales_trend_monthly_2024.png        ← What, how, when
customer_segments_scatter.png       ← Content, chart type
feature_importance_random_forest.png ← Content, model
```

**Bad:**
```
plot1.png               ← Meaningless number
chart.png               ← Too generic
viz.png                 ← Too vague
analysis.png            ← Unclear what
```

### Organization by Analysis Type

For large projects, create subfolders:

```
visualizations/
├── exploratory_analysis/
│   ├── distributions.png
│   ├── correlations.png
│   └── missing_values.png
│
├── model_results/
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
│
└── reports/
    ├── sales_dashboard.pdf
    └── forecast_summary.pdf
```

### Annotate Important Visualizations

Add metadata to saved files:

```python
# Save with metadata using PIL
from PIL import Image
import datetime

# Create and save plot normally
plt.savefig('temp_plot.png', dpi=300, bbox_inches='tight')

# Add metadata
img = Image.open('temp_plot.png')
img.save('outputs/visualizations/sales_trend_2024.png',
         pnginfo={'createdDate': str(datetime.datetime.now())})
```

---

## reports/

### What Goes Here

Analysis summaries, executive reports, and data tables:

```
reports/
├── sales_analysis_2024.html        ← Interactive HTML report
├── forecast_q1_2024.csv            ← Predictions
├── model_evaluation_summary.xlsx    ← Excel with metrics
└── customer_insights_brief.pdf      ← PDF summary
```

### Report Types

#### HTML Reports

**Interactive, self-contained, shareable**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sales Analysis 2024</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #4CAF50; color: white; }
    </style>
</head>
<body>
    <h1>Sales Analysis 2024</h1>
    <p>Report generated: 2024-01-16</p>
    <p>Data source: data/processed/sales_cleaned.csv</p>
    
    <h2>Key Metrics</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Total Sales</td>
            <td>$48.2M</td>
        </tr>
        <tr>
            <td>Number of Orders</td>
            <td>248,500</td>
        </tr>
    </table>
    
    <h2>Visualizations</h2>
    <img src="sales_trend_2024.png" alt="Sales Trend">
</body>
</html>
```

**Generate from Python:**

```python
import pandas as pd

# Create simple HTML table
df_summary = pd.DataFrame({
    'Metric': ['Total Sales', 'Avg Order Value', 'Total Customers'],
    'Value': ['$48.2M', '$194', '50,000']
})

html = """
<html>
<head><title>Sales Report</title></head>
<body>
<h1>Sales Analysis 2024</h1>
""" + df_summary.to_html() + """
</body>
</html>
"""

with open('outputs/reports/sales_analysis_2024.html', 'w') as f:
    f.write(html)
```

#### CSV Reports (Data Export)

**Predictions and metrics in tabular form**

```
outputs/reports/forecast_q1_2024.csv
```

Table structure:
```
date,predicted_sales,confidence_lower,confidence_upper
2024-02-01,185000,172000,198000
2024-02-02,188000,174000,202000
2024-02-03,182000,170000,195000
...
```

#### Excel Reports

**Stakeholder-friendly summaries**

```python
import pandas as pd

# Create multiple sheets
with pd.ExcelWriter('outputs/reports/model_evaluation_summary.xlsx') as writer:
    
    # Sheet 1: Summary metrics
    df_metrics = pd.DataFrame({
        'Model': ['K-Means', 'XGBoost', 'Random Forest'],
        'Accuracy': [0.85, 0.92, 0.88],
        'F1-Score': [0.82, 0.90, 0.86],
        'Training Time': ['45s', '120s', '85s']
    })
    df_metrics.to_excel(writer, sheet_name='Summary', index=False)
    
    # Sheet 2: Detailed metrics
    df_detailed = pd.DataFrame({...})
    df_detailed.to_excel(writer, sheet_name='Detailed', index=False)
```

#### PDF Reports

**Professional formatted summaries**

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas('outputs/reports/customer_insights_brief.pdf', 
                  pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 18)
c.drawString(50, 750, "Customer Insights Report")

# Date
c.setFont("Helvetica", 10)
c.drawString(50, 730, f"Generated: 2024-01-16")

# Content
c.setFont("Helvetica", 12)
c.drawString(50, 700, "Key Findings:")
c.drawString(70, 680, "• 4,500 premium customers generate 55% of revenue")
c.drawString(70, 660, "• 5,000 at-risk customers need engagement")
c.drawString(70, 640, "• Seasonal peak in Q4")

c.save()
```

### Report Naming Convention

**Format:** `[topic]_[date|version].[format]`

**Good:**
```
sales_analysis_2024_q4.html           ← Topic, timeframe, format
forecast_2024_02_v2.csv               ← Topic, date, version
model_performance_2024_01_16.xlsx    ← Content, date
```

**Bad:**
```
report.html                ← Too vague
analysis.xlsx              ← Unclear content
data_2024.csv              ← Vague
report_final_v3.pdf       ← Which is final?
```

---

## Output Artifacts Lifecycle

```
Day 1: Generate output
├─ Run analysis script
├─ Save to outputs/ folder
└─ Organize by type (models/viz/reports)

Week 1: Use in presentation/reports
├─ Share visualizations
├─ Distribute reports
└─ Deploy models

Month 1: Archive results
├─ Keep one copy for reference
├─ Document key metrics
└─ Clean up temporary files

Note: All can be regenerated anytime
      so don't treat as precious
```

---

## Common Questions

**Q: Should I commit outputs to git?**  
A: Only small reports (< 1 MB). Regenrate large outputs. Use git-lfs for models if needed.

**Q: How long to keep outputs?**  
A: Keep current month + 1-2 previous. Delete ancient outputs (regenerable anyway).

**Q: Can I manually edit outputs?**  
A: Avoid if possible. Instead, modify script and regenerate. Keeps audit trail clean.

**Q: How do I version outputs?**  
A: Use date or version number in filename (forecast_2024_02.csv, not forecast_latest.csv).

**Q: What if someone needs a past output?**  
A: Regenerate from git history. Check out old processing script and run it.

---

## Quality Checklist

Before sharing outputs:

- [ ] File has meaningful, descriptive name
- [ ] Visualization appears correctly (size, fonts, colors)
- [ ] Report includes data source documentation
- [ ] Model includes metadata (training date, performance)
- [ ] All outputs dated or versioned
- [ ] Can regenerate from processed data ✓
- [ ] Filename indicates content clearly
- [ ] No hardcoded paths or personal info

---

**Remember:** Output artifacts are intermediate products. The real value is in understanding the data and insights, not the files themselves.
