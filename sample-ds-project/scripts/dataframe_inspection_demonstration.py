"""
================================================================================
MILESTONE 17: INSPECTING DATAFRAMES USING head(), info(), AND describe()
================================================================================

Understanding DataFrame Inspection:
A comprehensive guide to using head(), info(), and describe() to understand
dataset structure, data types, and summary statistics before any analysis.

Milestones covered:
1. Introduction to DataFrame Inspection
2. Using head() for Data Preview
3. Variations of head() and tail()
4. Using info() for Structure Inspection
5. Understanding Data Types (dtypes)
6. Using describe() for Statistical Summary
7. Comparing Inspection Methods
8. The Scenario: Detecting Misloaded Data Types
9. Complete Inspection Workflow
10. Common Inspection Patterns
11. Best Practices for Data Inspection

================================================================================
MILESTONE 1: INTRODUCTION TO DATAFRAME INSPECTION
================================================================================
"""

import numpy as np
import pandas as pd
import os

print("="*80)
print("MILESTONE 1: INTRODUCTION TO DATAFRAME INSPECTION")
print("="*80)

print("\n[What is DataFrame inspection?]")
print("Inspection = Understanding your data BEFORE analysis")
print("Three key inspection methods:")
print("  1. head() -> Preview: What does the data look like?")
print("  2. info() → Structure: What columns, types, and nulls?")
print("  3. describe() → Statistics: What are typical values?")

print("\n[Why inspect first?]")
print("- Catch loading errors early (wrong data types, missing values)")
print("- Understand data structure before analysis")
print("- Identify data quality issues")
print("- Prevent wasted time on cleaning later")
print("- Build confidence in your data")

print("\n[When to inspect]")
print("ALWAYS, immediately after:")
print("  - Loading a CSV file")
print("  - Receiving a new dataset")
print("  - Creating a DataFrame from scratch")
print("  - After any data transformation")

print("\n[The inspection workflow]")
print("Step 1: Load data → df = pd.read_csv('file.csv')")
print("Step 2: Preview → df.head()")
print("Step 3: Structure → df.info()")
print("Step 4: Summary → df.describe()")
print("Step 5: Decide → Can I trust this data?")

print("\n[Creating sample datasets for demonstration]")

# Create CSV file
csv_content = """StudentID,Name,Age,GPA,Major,Enrolled,ExamScore
1001,Alice,20,3.8,Computer Science,True,95
1002,Bob,21,3.2,Mathematics,True,87
1003,Charlie,20,3.9,Physics,False,92
1004,Diana,22,3.5,Chemistry,True,88
1005,Eve,19,3.7,Biology,True,91
1006,Frank,21,2.9,Engineering,False,79
1007,Grace,20,3.6,Computer Science,True,94
1008,Henry,23,3.4,Mathematics,True,85"""

csv_file = 'students.csv'
with open(csv_file, 'w') as f:
    f.write(csv_content)

print(f"Created: {csv_file}")
print(f"Sample content:\n{csv_content[:150]}...\n")

# Load the DataFrame
df = pd.read_csv(csv_file)
print("DataFrame loaded successfully")

"""
================================================================================
MILESTONE 2: USING head() FOR DATA PREVIEW
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 2: USING head() FOR DATA PREVIEW")
print("="*80)

print("\n[What is head()?]")
print("head() = Display first N rows of a DataFrame (default: 5)")
print("Purpose: Quick visual check of data content")

print("\n[Basic head() - Default (5 rows)]")
print("df.head()")
print(df.head())

print("\n[Specifying number of rows]")
print("df.head(3) - Show first 3 rows:")
print(df.head(3))

print("\n[head(1) - Single row inspection]")
print("df.head(1) - Often used to see structure without clutter:")
print(df.head(1))

print("\n[head(0) - Just column names]")
print("df.head(0) - Shows structure without any data:")
print(df.head(0))

print("\n[What to look for in head()]")
print("✓ Are column names meaningful?")
print("✓ Do values look reasonable?")
print("✓ Are there weird characters or formatting?")
print("✓ Do data types appear correct?")
print("✓ Are there NaN or 'null' values visible?")

print("\n[Common patterns in head()]")
print("Pattern 1: First few rows look different")
print("  → Metadata? Headers misaligned? Data loading issue?")

print("\nPattern 2: Values are unexpected format")
print("  → Numeric as string? Dates formatted oddly?")

print("\nPattern 3: See NaN immediately")
print("  → Missing data present from start")

print("\n[head() output interpretation]")
df_preview = df.head(2)
print(f"DataFrame type: {type(df_preview)}")
print(f"Still a DataFrame: {isinstance(df_preview, pd.DataFrame)}")
print(f"Shape: {df_preview.shape}")

"""
================================================================================
MILESTONE 3: VARIATIONS OF head() AND tail()
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 3: VARIATIONS OF head() AND tail()")
print("="*80)

print("\n[tail() - Last rows]")
print("df.tail() - Show last 5 rows (default):")
print(df.tail())

print("\n[tail() with specific count]")
print("df.tail(2) - Last 2 rows:")
print(df.tail(2))

print("\n[Why use tail()?]")
print("- Check for unusual patterns at end")
print("- See if data ends abruptly")
print("- Compare last rows to first rows for consistency")

print("\n[Combining head() and tail()]")
print("Strategy 1: Check bookends")
print("  df.head(1)  # How does data start?")
print("  df.tail(1)  # How does data end?")

print("\nStrategy 2: Get middle sense around")
print("  df.head(3)  # First few")
print("  df.tail(3)  # Last few")
print("  To understand overall pattern")

print("\n[Negative indexing with head()]")
print("df.head(-2) - All rows EXCEPT last 2:")
result = df.head(-2)
print(f"Original rows: {len(df)}, After head(-2): {len(result)}")

print("\ndf.tail(-2) - All rows EXCEPT first 2:")
result = df.tail(-2)
print(f"Original rows: {len(df)}, After tail(-2): {len(result)}")

print("\n[iloc and loc for specific row inspection]")
print("df.iloc[0] - Get first row as Series:")
print(df.iloc[0])

print("\ndf.loc[0] - Get row with index 0:")
print(df.loc[0])

print("\n[Quick sample() for random rows]")
print("df.sample(2) - Random sample of 2 rows:")
print(df.sample(2, random_state=42))
print("(random_state for reproducibility)")

"""
================================================================================
MILESTONE 4: USING info() FOR STRUCTURE INSPECTION
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 4: USING info() FOR STRUCTURE INSPECTION")
print("="*80)

print("\n[What is info()?]")
print("info() = Display DataFrame structure and metadata")
print("Shows: columns, data types, non-null counts, memory usage")

print("\n[Viewing info() output]")
print("df.info()")
df.info()

print("\n[Components of info() output]")
print("1. RangeIndex: (0 to 7) = 8 rows")
print("2. Data columns (total 7 columns)")
print("3. For each column:")
print("   - Column name")
print("   - Count of non-null values")
print("   - Data type (int64, float64, object, bool)")
print("4. Memory usage")

print("\n[Interpreting data types]")
print("int64    = Integer (no decimals)")
print("float64  = Floating point (decimals)")
print("object   = Mixed types or strings")
print("bool     = True/False")
print("datetime64 = Date and time")
print("category = Categorical data")

print("\n[Reading non-null counts]")
print("If Column has 8 non-nulls in 8 rows → No missing data")
print("If Column has 7 non-nulls in 8 rows → 1 missing value")

print("\n[Identifying missing values in info()]")
# Create DataFrame with missing values
csv_missing = """ID,Name,Score,Pass
101,Alice,95.5,True
102,Bob,,False
103,Charlie,88.0,True
104,,92.0,
105,Eve,91.5,True"""

csv_missing_file = 'scores.csv'
with open(csv_missing_file, 'w') as f:
    f.write(csv_missing)

df_missing = pd.read_csv(csv_missing_file)
print("\nDataFrame WITH missing values:")
df_missing.info()

print("\n[info() tells you about data quality]")
print("Missing values = Non-null count < total rows")
print("In this example:")
print("  Score: 4 non-null (1 missing)")
print("  Pass: 4 non-null (1 missing)")
print("  Name: 4 non-null (1 missing)")

print("\n[The CRITICAL scenario: Detecting wrong data type]")
print("Original CSV columns list might show:")
print("Column 1: StudentID (int64) ✓")
print("Column 2: Name (object) ✓")
print("Column 3: Age (int64) ✓")
print("Column 4: GPA (float64) ✓")
print("Column 5: Major (object) ✓")
print("Column 6: Enrolled (bool) ✓")
print("Column 7: ExamScore (int64) ✓")

print("\nBUT if data loaded wrong:")
print("Column 3: Age (object) ❌ Should be int64!")
print("This means age values are strings, not numbers")
print("Would fail: df['Age'].sum() or df['Age'] > 20")

print("\n[Why info() catches this immediately]")
print("1. You look at expected types")
print("2. You see if actual types match")
print("3. If object instead of int64 → data quality issue")
print("4. Fix at load time instead of discovering in analysis")

"""
================================================================================
MILESTONE 5: UNDERSTANDING DATA TYPES (dtypes)
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 5: UNDERSTANDING DATA TYPES (dtypes)")
print("="*80)

print("\n[Accessing dtypes directly]")
print("df.dtypes - Show all column data types:")
print(df.dtypes)

print("\n[Single column dtype]")
print("df['Age'].dtype:", df['Age'].dtype)
print("df['Name'].dtype:", df['Name'].dtype)
print("df['Enrolled'].dtype:", df['Enrolled'].dtype)

print("\n[Why data types matter]")
print("int64 Column: Can do math (sum, mean, comparison)")
print("object Column: Cannot do math (must convert first)")

print("\n[Example: Wrong dtype prevents operations]")
df_age = df[['Age']].copy()
print("df['Age'].sum():", df_age['Age'].sum())  # Works, it's int64
print("✓ Works because Age is int64")

print("\nBut if Age was loaded as object (string):")
print("df['Age'].sum() would FAIL")
print("Because you can't sum strings")

print("\n[Data type categories]")
print("Numeric:")
print("  int8, int16, int32, int64 (integers)")
print("  float32, float64 (decimals)")
print("  Uint8, uint16, uint32, uint64 (unsigned integers)")

print("\nNon-numeric:")
print("  object (strings, mixed types)")
print("  bool (True/False)")
print("  datetime64 (dates and times)")
print("  category (categorical data)")
print("  string (text - newer pandas)")

print("\n[Why object is concerning]")
print("object type = 'Unknown, might be anything'")
print("Could contain: strings, numbers, mixed, corrupted data")
print("If numeric column is object → likely loading error")

"""
================================================================================
MILESTONE 6: USING describe() FOR STATISTICAL SUMMARY
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 6: USING DESCRIBE() FOR STATISTICAL SUMMARY")
print("="*80)

print("\n[What is describe()?]")
print("describe() = Statistical summary of numeric columns")
print("Shows: count, mean, std, min, 25%, 50%, 75%, max")

print("\n[Basic describe()]")
print("df.describe()")
print(df.describe())

print("\n[Interpreting describe() output]")
print("count    = Number of non-null values")
print("mean     = Average value")
print("std      = Standard deviation (spread)")
print("min      = Minimum value")
print("25%      = 1st quartile (25th percentile)")
print("50%      = Median (middle value)")
print("75%      = 3rd quartile (75th percentile)")
print("max      = Maximum value")

print("\n[What each statistic tells you]")
print("count < total rows → Missing values present")
print("mean vs 50% similar → Symmetric distribution")
print("mean > 50% → Right-skewed (large values pull mean up)")
print("mean < 50% → Left-skewed (small values pull mean down)")
print("max - min = range → Overall spread")

print("\n[Example interpretation]")
stats = df.describe()
print(f"GPA: mean={stats.loc['mean', 'GPA']:.2f}, std={stats.loc['std', 'GPA']:.2f}")
print(f"    range: {stats.loc['min', 'GPA']:.1f} to {stats.loc['max', 'GPA']:.1f}")
print("Insight: GPA values clustered around 3.5, with some variation")

print("\n[describe() includes or excludes non-numeric]")
print("df.describe() - Only numeric columns")
print("df.describe(include='all') - All columns including object")

print("\nWith include='all':")
print(df.describe(include='all'))

print("\n[Specific column describe()]")
print("df['Age'].describe():")
print(df['Age'].describe())

print("\n[Percentiles with describe()]")
print("df.describe(percentiles=[0.25, 0.5, 0.75, 0.95])")
print("Shows percentiles of your choosing")

print("\n[What describe() reveals about data quality]")
print("Large std = High variability")
print("mean ≈ median = Likely normal distribution")
print("max >> mean = Possible outliers")
print("count << rows = Many missing values")

"""
================================================================================
MILESTONE 7: COMPARING INSPECTION METHODS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 7: COMPARING INSPECTION METHODS")
print("="*80)

print("\n[When to use each method]")
print("head():")
print("  When: Need to see actual data rows")
print("  Shows: First N rows of data")
print("  Good for: Spot-checking content, finding errors")

print("\ninfo():")
print("  When: Need to understand structure")
print("  Shows: Columns, dtypes, nulls, memory")
print("  Good for: Finding wrong data types, missing values")

print("\ndescribe():")
print("  When: Need numeric summary statistics")
print("  Shows: Mean, std, min, max, quartiles")
print("  Good for: Understanding data ranges, distributions")

print("\n[Inspection workflow in order]")
print("1. head() first → See what data looks like")
print("   'Does this look like real data?'")
print("\n2. info() second → Understand structure")
print("   'Are data types correct?'")
print("\n3. describe() third → Get statistics")
print("   'What are typical values?'")

print("\n[Example: Full inspection sequence]")
print("Step 1: df.head()")
print(df.head())

print("\nStep 2: df.info()")
df.info()

print("\nStep 3: df.describe()")
print(df.describe())

"""
================================================================================
MILESTONE 8: THE SCENARIO - DETECTING MISLOADED DATA TYPES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 8: THE SCENARIO - DETECTING MISLOADED DATA TYPES")
print("="*80)

print("\n[SCENARIO: Numeric column loaded as string]")
print("""
You begin analysis and later discover that a numeric column was
actually loaded as a string (object type).

How could using info() earlier have helped prevent this issue?
What would you look for during inspection?
""")

# Create problematic CSV
csv_problem = """StudentID,Name,Age,Score
1001,Alice,20,95
1002,Bob,twenty-one,87
1003,Charlie,20,92"""

csv_problem_file = 'problem_ages.csv'
with open(csv_problem_file, 'w') as f:
    f.write(csv_problem)

print("Problematic CSV file (Age has mixed format):")
print(csv_problem)

df_problem = pd.read_csv(csv_problem_file)
print("\nAfter loading:")
print(df_problem)

print("\n[Step 1: Quick inspection with head()]")
print("df.head():")
print(df_problem.head())
print("Observation: Age 'twenty-one' looks wrong!")

print("\n[Step 2: Check data types with info()]")
print("df.info():")
df_problem.info()
print("ALERT: Age is 'object', not 'int64'!")
print("This is the RED FLAG you should see")

print("\n[Step 3: Why this matters]")
print("If you immediately proceed to analysis:")
print("df['Age'].mean() → Would FAIL")
print("df['Age'] > 20 → Would FAIL")
print("df['Age'].sum() → Would FAIL")

print("\n[The prevention strategy]")
print("1. After loading, ALWAYS run df.info()")
print("2. Check each column's expected dtype")
print("3. Ask: 'Is this column numeric?'")
print("4. If dtype != expected → STOP and investigate")
print("5. Fix at load time with dtype parameter")

print("\n[How to fix at load time]")
print("df = pd.read_csv('file.csv', dtype={'Age': 'int64'})")
print("This will raise an error if Age contains non-numeric values")
print("Error at load time prevents silent data corruption")

print("\n[The info() inspection checklist]")
print("For each column, ask:")
print("  ✓ Is the dtype what I expect?")
print("  ✓ Is count == number of rows? (all non-null?)")
print("  ✓ Are there NaN values I didn't know about?")
print("  ✓ Is 'object' actually numeric by mistake?")

print("\n[Real-world example of the scenario]")
print("Without early inspection:")
print("  Load data → Begin analysis → df['Age'].mean()")
print("  TypeError: unsupported operand type(s) for +: 'int' and 'str'")
print("  Now you must find and fix the problem")

print("\nWith early inspection:")
print("  Load data → df.info()")
print("  See Age is 'object' → Open file → Find 'twenty-one'")
print("  Fix with dtype parameter → Reload")
print("  Analysis proceeds without error")

print("\n[Why early inspection saves time]")
print("Time spent on inspection: 30 seconds")
print("Time saved in debugging: Hours")

"""
================================================================================
MILESTONE 9: COMPLETE INSPECTION WORKFLOW
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 9: COMPLETE INSPECTION WORKFLOW")
print("="*80)

print("\n[The Standard 3-Step Inspection Workflow]")
print("""
After EVERY data load, follow this workflow:

STEP 1: Quick Visual Check (head)
├─ Use: df.head()
├─ Ask: Does data look reasonable?
├─ Look for: Weird values, formatting issues, obvious errors
└─ Time: 15 seconds

STEP 2: Structure Verification (info)
├─ Use: df.info()
├─ Ask: Are column types correct?
├─ Look for: object types that should be numeric, NaN patterns
└─ Time: 15 seconds

STEP 3: Summary Statistics (describe)
├─ Use: df.describe()
├─ Ask: Do values make sense?
├─ Look for: Unexpected ranges, outliers
└─ Time: 10 seconds
""")

print("\n[Example: Complete workflow on our student data]")
print("\n--- STEP 1: head() ---")
print(df.head(2))
print("✓ Looks like reasonable student data")

print("\n--- STEP 2: info() ---")
df.info()
print("✓ All columns have correct types")
print("✓ No missing values (all non-null counts = 8)")

print("\n--- STEP 3: describe() ---")
print(df.describe())
print("✓ Age ranges 19-23 (reasonable for students)")
print("✓ GPA ranges 2.9-3.9 (realistic GPA range)")
print("✓ ExamScore ranges 79-95 (reasonable test scores)")

print("\n[Conclusion after workflow]")
print("Data quality: ✓ Trustworthy")
print("Data types: ✓ Correct")
print("Missing data: ✓ None present")
print("Value ranges: ✓ Reasonable")
print("Status: ✓ Ready for analysis")

"""
================================================================================
MILESTONE 10: COMMON INSPECTION PATTERNS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 10: COMMON INSPECTION PATTERNS")
print("="*80)

print("\n[Pattern 1: Finding missing data]")
print("df.info() shows: Column 'Score' has 7 non-null, not 8")
print("This means 1 missing value")
print("Next step: df['Score'].isna().sum() → confirms")

print("\n[Pattern 2: Detecting numeric loaded as string]")
print("df.info() shows: Column 'Age' dtype = 'object', not 'int64'")
print("Likely problem: Non-numeric value in Age column")
print("Next step: Check unique values, find the culprit")

print("\n[Pattern 3: Unexpected column]")
print("df.head() shows: Column 'Unnamed: 7'")
print("Likely problem: Extra blank column in CSV")
print("Next step: Check CSV file directly")

print("\n[Pattern 4: Values in wrong type]")
print("df.info() shows: Column 'Date' dtype = 'object'")
print("Should be: datetime64")
print("Next step: Use pd.to_datetime() or reload with parse_dates")

print("\n[Pattern 5: Unexpected NaN distribution]")
print("df.info() shows: Column 'Email' has only 3 non-null in 100 rows")
print("Likely problem: Data entry issue or wrong column")
print("Next step: Verify if this is expected")

print("\n[Pattern 6: Outliers in describe()]")
print("df.describe() shows: max = 999, but mean = 50")
print("Likely problem: Outliers or data entry errors")
print("Next step: Investigate unusual values")

"""
================================================================================
MILESTONE 11: BEST PRACTICES FOR DATA INSPECTION
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 11: BEST PRACTICES FOR DATA INSPECTION")
print("="*80)

print("\n[Best Practice 1: ALWAYS inspect immediately after loading]")
print("DON'T: df = pd.read_csv(file); df.groupby(...)")
print("DO:")
print("  df = pd.read_csv(file)")
print("  df.head()")
print("  df.info()")
print("  df.describe()")
print("  # NOW proceed with analysis")

print("\n[Best Practice 2: Make it a reflex]")
print("Develop muscle memory for inspection")
print("As soon as data loads, run these 3 methods")
print("It takes 1 minute and prevents hours of debugging")

print("\n[Best Practice 3: Document your expectations]")
print("Before loading, write:")
print("  # Expected: 1000 rows, 15 columns")
print("  # Types: StudentID (int), Name (str), Score (float)")
print("  df = pd.read_csv(file)")
print("  df.info()  # Verify matches expectations")

print("\n[Best Practice 4: Check specific columns when suspicious]")
print("If info() shows unexpected type:")
print("  df['ColumnName'].unique()  # See actual values")
print("  df['ColumnName'].value_counts()  # Count occurrences")
print("  df['ColumnName'].isna().sum()  # Count NaN")

print("\n[Best Practice 5: Use verbose info()]")
print("df.info(verbose=True)  # Detailed output")
print("df.info(memory_usage='deep')  # Exact memory usage")

print("\n[Best Practice 6: Create inspection summary]")
print("Never trust a single view. Create your inspection report:")
inspection_report = f"""
INSPECTION REPORT: {csv_file}
├─ Rows: {df.shape[0]}
├─ Columns: {df.shape[1]}
├─ Column Names: {df.columns.tolist()}
├─ Dtypes Check
│  └─ All numeric: {df.select_dtypes(include='number').shape[1]} columns
├─ Missing Data: {df.isna().sum().sum()} total missing values
├─ Memory Usage: ~{df.memory_usage(deep=True).sum() / 1024:.1f} KB
└─ Status: Ready for analysis ✓
"""
print(inspection_report)

print("\n[Best Practice 7: Comparative analysis]")
print("Compare head() with tail() for consistency")
print("Compare describe() across runs to spot changes")
print("Compare info() before/after transformations")

print("\n[Best Practice 8: Automate inspection]")
print("Create a function for quick inspection:")
print("""
def inspect_dataframe(df):
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Missing: {df.isna().sum().sum()}")
    df.info()
    print(df.describe())

inspect_dataframe(df)  # Single call for full inspection
""")

print("\n[Best Practice 9: Question everything]")
print("Never assume data is correct. Always verify:")
print("  Is every column I expect present?")
print("  Are there unexpected columns?")
print("  Are data types correct?")
print("  Are value ranges reasonable?")
print("  Are there more NaN values than expected?")

print("\n[Best Practice 10: Document findings]")
print("After inspection, document:")
print("  Data quality assessment: Good/Needs work")
print("  Issues found: [list any oddities]")
print("  Actions taken: [how you fixed issues]")
print("  Ready for analysis: Yes/No")

print("\n" + "="*80)
print("MILESTONE 17 SUMMARY")
print("="*80)
print("""
Three essential DataFrame inspection methods learned:

1. head() - Visual Preview
   ├─ See first N rows of actual data
   ├─ Quick spot-check for obvious errors
   └─ Default: first 5 rows

2. info() - Structure Inspection
   ├─ See columns, data types, nulls
   ├─ Catch wrong data types (CRITICAL)
   ├─ Identify missing values
   └─ Most important for data quality

3. describe() - Statistical Summary
   ├─ See mean, std, min, max, quartiles
   ├─ Understand data ranges
   └─ Identify outliers

The Standard Inspection Workflow:
1. df.head() → 15 seconds
2. df.info() → 15 seconds (THE CRITICAL STEP)
3. df.describe() → 10 seconds
Total: ~40 seconds to verify data quality

The CRITICAL Scenario:
When a numeric column loads as 'object' (string) instead of int/float:
- head() shows the values
- info() shows dtype = object (RED FLAG)
- Without inspection, analysis fails later (wasted time)
- With inspection, you catch it immediately (few seconds to fix)

Why This Matters:
- 30 seconds of inspection = Hours of debugging prevented
- Early detection of data quality issues
- Confidence before analysis begins
- Professional approach to data work

The Rule:
NEVER skip inspection. If you're tempted to, that's exactly when
you need it most. Make it automatic. Inspect everything. Always.
""")

print("="*80)
print("END OF MILESTONE 17")
print("="*80)

# Clean up temporary CSV files
for file in [csv_file, csv_missing_file, csv_problem_file]:
    if os.path.exists(file):
        os.remove(file)

print("\nCleaned up temporary CSV files")
