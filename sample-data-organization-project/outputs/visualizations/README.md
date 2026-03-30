# Visualizations

## Plots, Charts, and Images

This folder contains data visualizations created from analysis and modeling.

## What Goes Here

- PNG images (.png)
- PDF charts (.pdf)
- SVG graphics (.svg)
- Any exploratory plots

## Naming Convention

Use descriptive names indicating content and type:

**Good:**
```
sales_trend_monthly.png           ← What + chart type
customer_segments_scatter.png     ← What + chart type
feature_importance_bars.png       ← What + chart type
```

**Bad:**
```
plot.png
chart.png
viz1.png
```

## Example Files

**sales_trend_2024.png**
- Type: Line chart
- Shows: Monthly sales throughout 2024
- Created: 2024-01-16
- Resolution: 300 DPI (print quality)

**customer_segments.png**
- Type: Scatter plot
- Shows: Customer clustering results (2D projection)
- Colors: Different colors for each segment
- Created: 2024-01-16

**feature_importance.png**
- Type: Horizontal bar chart
- Shows: Top 10 most important features for predictions
- Source: XGBoost model
- Created: 2024-01-16

## Creating Quality Visualizations

**Key guidelines:**

1. **Resolution**: Save at 300 DPI
   ```python
   plt.savefig('sales_trend.png', dpi=300, bbox_inches='tight')
   ```

2. **Size**: Use appropriate figure size
   ```python
   fig, ax = plt.subplots(figsize=(10, 6))  # Width x Height
   ```

3. **Labels**: Clear titles and axis labels
   ```python
   ax.set_title('Sales Trend 2024', fontsize=14, fontweight='bold')
   ax.set_xlabel('Month')
   ax.set_ylabel('Sales ($)')
   ```

4. **Format**: PNG for most uses
   - PNG: Best for web and general use
   - PDF: For formal reports
   - SVG: For scalable graphics

## Organization Options

For larger projects, optionally organize by analysis type:

```
visualizations/
├── exploratory_analysis/
│   ├── distributions.png
│   ├── correlations_heatmap.png
│   └── missing_values_pattern.png
├── model_diagnostics/
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
└── reporting/
    ├── sales_dashboard.png
    └── forecast_comparison.png
```

## Tips for Better Visualizations

✓ Use consistent color palette  
✓ Include data source in title or caption  
✓ Label axes clearly with units  
✓ Avoid 3D charts (hard to read)  
✓ Use gridlines for reference  
✓ Keep legends at side, not overlaying  
✓ High contrast colors (readability)  
✓ Meaningful titles (not "Figure 1")  

## Sharing Visualizations

```bash
# Email or share individual PNG files
# They're self-contained and look good

# For formal reports, use PDF
# PDF preserves formatting across systems

# Include PNG in presentations
# GitHub, notebooks, and slides render PNGs well
```

## Common Issues

**Files look blurry:**
→ Increase DPI to 300 or higher

**Text too small:**
→ Increase figure size: figsize=(12, 8)

**Colors don't print well:**
→ Test print preview first

**Can't share large files:**
→ PNG usually < 1 MB per image
