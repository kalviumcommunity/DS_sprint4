# Reports

## Analysis Summaries and Data Export

This folder contains analysis summaries, predictions, and data exports.

## What Goes Here

- HTML reports (.html)
- CSV data exports (.csv)
- Excel workbooks (.xlsx)
- PDF summaries (.pdf)

## Report Types

### HTML Reports

**Interactive, self-contained, shareable**

Can include:
- Tables with summary metrics
- Embedded images
- Interactive elements (with plotly, etc.)
- Professional styling

**Example:** sales_analysis_2024.html

### CSV Reports

**Data tables for external use**

Raw data export format, easy to:
- Send to stakeholders
- Import into Excel
- Use in other tools
- Version control (small size)

**Example:** forecast_q1_2024.csv

### Excel Reports

**Formatted workbooks with multiple sheets**

Good for:
- Stakeholder presentations
- Multiple metrics on different sheets
- Charts and formatting
- Note-taking and annotations

**Example:** model_evaluation_summary.xlsx

### PDF Reports

**Formal printed documents**

Use for:
- Official reports
- Printing to paper
- Archive-style documents
- Professional presentations

**Example:** customer_insights_brief.pdf

## Naming Convention

**Format:** `[topic]_[date/version].[format]`

**Good:**
```
sales_analysis_2024_jan.html       ← Topic, month, format
forecast_2024_02.csv               ← Topic, date, format
model_metrics_v2.xlsx              ← Topic, version, format
```

## Common Reports

### Executive Summary
```html
- Key metrics (3-5 most important)
- Key findings (3-5 bullet points)
- Recommendations
- Next steps
```

### Technical Report
```
- Methodology
- Data sources
- Processing steps
- Statistical tests
- Results and interpretation
- Limitations
- Appendix with detailed tables
```

### Forecast Report
```
- Recent trends
- Model used
- Predictions (with confidence intervals)
- Assumptions
- Risk factors
```

## Creating Reports

### Simple HTML Report
```python
html = """
<html>
<head>
    <title>Sales Analysis</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        table { border-collapse: collapse; }
        th { background-color: #4CAF50; color: white; }
        td { border: 1px solid #ddd; padding: 8px; }
    </style>
</head>
<body>
    <h1>Sales Analysis 2024</h1>
    <p>Generated: 2024-01-16</p>
    
    <h2>Summary Metrics</h2>
    <table>
        <tr><th>Metric</th><th>Value</th></tr>
        <tr><td>Total Sales</td><td>$48.2M</td></tr>
        <tr><td>Avg Order</td><td>$194</td></tr>
    </table>
</body>
</html>
"""

with open('sales_analysis_2024.html', 'w') as f:
    f.write(html)
```

### CSV Data Export
```python
import pandas as pd

# Prepare data
forecast_df = pd.DataFrame({
    'date': pd.date_range('2024-02-01', periods=30),
    'predicted': predictions,
    'confidence_low': predictions * 0.95,
    'confidence_high': predictions * 1.05
})

# Save CSV
forecast_df.to_csv('forecast_2024_02.csv', index=False)
```

## Organizing Multiple Reports

Create subfolders for better organization:

```
reports/
├── monthly/
│   ├── sales_analysis_2024_jan.html
│   ├── sales_analysis_2024_feb.html
│   └── sales_analysis_2024_mar.html
├── models/
│   ├── model_evaluation_jan.xlsx
│   └── model_evaluation_feb.xlsx
└── forecasts/
    ├── forecast_2024_q1.csv
    └── forecast_2024_q2.csv
```

## Best Practices

✓ Include data source in report  
✓ Timestamp when report generated  
✓ Document any assumptions  
✓ Keep reports < 10 MB  
✓ Use clear, descriptive names  
✓ Archive old reports (keep 1-2 recent)  
✓ Link to underlying data/code  

## Sharing Reports

**Email stakeholders:**
```html
<!-- Attach HTML file or PDF -->
They can open in any browser/reader
```

**Publish on intranet:**
```
Save as HTML
Post to shared folder or website
```

**Archive:**
```
Keep one copy of each month
Delete very old reports (regenerable)
```

## Report Templates

Use consistent templates for recurring reports. Reduces time and ensures quality.

**Monthly Sales Template:**
1. Executive summary
2. Key metrics (sales, orders, avg value)
3. Trends chart
4. Top products
5. Regional breakdown
6. Next month forecast

**Model Evaluation Template:**
1. Model name and version
2. Training data summary
3. Performance metrics
4. Confusion matrix / ROC curve
5. Feature importance
6. Recommendations

---

**Pro Tip:** Automate report generation with scripts. Saves time and ensures consistency.
