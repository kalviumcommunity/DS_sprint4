"""
================================================================================
MILESTONE 15: PANDAS DATAFRAMES - CREATING FROM DICTIONARIES AND FILES
================================================================================

Understanding Pandas DataFrames:
A comprehensive guide to creating Pandas DataFrames from Python dictionaries
and external files (CSV, etc.), understanding their structure, and inspecting
data immediately after loading to verify correctness.

Milestones covered:
1. Introduction to DataFrames
2. Creating DataFrames from Dictionary of Lists
3. Creating DataFrames from Dictionary of Series
4. Creating DataFrames from Records (List of Dicts)
5. Understanding DataFrame Structure
6. Inspecting DataFrame Rows and Columns
7. Creating Sample CSV File for Loading
8. Loading DataFrames from CSV Files
9. Inspecting After Loading (The Scenario)
10. Data Type Verification and Conversion
11. Best Practices for DataFrame Creation

================================================================================
MILESTONE 1: INTRODUCTION TO DATAFRAMES
================================================================================
"""

import numpy as np
import pandas as pd
import os

print("="*80)
print("MILESTONE 1: INTRODUCTION TO DATAFRAMES")
print("="*80)

print("\n[What is a Pandas DataFrame?]")
print("A DataFrame is a 2D labeled table combining:")
print("  1. ROWS: Individual records or observations")
print("  2. COLUMNS: Features or attributes (like Series)")
print("  3. ROW INDEX: Labels for each row (0, 1, 2, ... by default)")
print("  4. COLUMN NAMES: Labels for each column")
print("")
print("Structure:")
print("         Col1    Col2    Col3")
print("  Row0   val     val     val")
print("  Row1   val     val     val")
print("  Row2   val     val     val")
print("")
print("Think of it like:")
print("  - Excel spreadsheet")
print("  - SQL table with rows and columns")
print("  - 2D NumPy array with labeled rows and columns")

print("\n[DataFrame vs Series]")
print("Series: 1D (values + index)")
print("DataFrame: 2D (rows + columns + row index)")

print("\n[Checking Pandas Version]")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")

"""
================================================================================
MILESTONE 2: CREATING DATAFRAMES FROM DICTIONARY OF LISTS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 2: CREATING DATAFRAMES FROM DICTIONARY OF LISTS")
print("="*80)

print("\n[Creating DataFrame from dict of lists]")
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data_dict)
print(f"Dictionary:\n{data_dict}\n")
print(f"Created DataFrame:")
print(df)

print("\n[Understanding the structure]")
print(f"DataFrame type: {type(df)}")
print(f"DataFrame shape: {df.shape} (4 rows, 3 columns)")
print(f"Column names: {df.columns.tolist()}")
print(f"Row index: {df.index.tolist()}")

print("\n[Creating DataFrame with custom row index]")
data = {
    'Product': ['Laptop', 'Phone', 'Tablet'],
    'Price': [1000, 500, 300],
    'Stock': [50, 150, 200]
}
df_custom = pd.DataFrame(data, index=['A', 'B', 'C'])
print(f"DataFrame with custom index:")
print(df_custom)

print("\n[What happens with mismatched list lengths?]")
try:
    bad_data = {
        'A': [1, 2, 3],
        'B': [10, 20]  # Different length!
    }
    df_bad = pd.DataFrame(bad_data)
except ValueError as e:
    print(f"ERROR: {e}")
    print("All columns must have the same number of values!")

print("\n[DataFrame from dict of lists - key points]")
print("- Dictionary keys become column names")
print("- List values become column data")
print("- All lists must have same length")
print("- Row index is auto-generated (0, 1, 2, ...)")

"""
================================================================================
MILESTONE 3: CREATING DATAFRAMES FROM DICTIONARY OF SERIES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 3: CREATING DATAFRAMES FROM DICTIONARY OF SERIES")
print("="*80)

print("\n[Creating DataFrame from dict of Series]")
s1 = pd.Series([100, 200, 300, 400], index=['Q1', 'Q2', 'Q3', 'Q4'], name='Revenue')
s2 = pd.Series([50, 60, 55, 70], index=['Q1', 'Q2', 'Q3', 'Q4'], name='Profit')
s3 = pd.Series([30, 40, 35, 45], index=['Q1', 'Q2', 'Q3', 'Q4'], name='Expenses')

series_dict = {'Revenue': s1, 'Profit': s2, 'Expenses': s3}
df_from_series = pd.DataFrame(series_dict)

print(f"Series 1:\n{s1}\n")
print(f"Series 2:\n{s2}\n")
print(f"Dictionary of Series: {list(series_dict.keys())}\n")
print(f"Created DataFrame:")
print(df_from_series)

print("\n[Index alignment in dict of Series]")
print("If Series have different indices, DataFrame aligns by matching index")
s_a = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
s_b = pd.Series([10, 20, 30], index=['z', 'y', 'x'])  # Different order!
df_aligned = pd.DataFrame({'A': s_a, 'B': s_b})
print(f"Series A index: {s_a.index.tolist()}")
print(f"Series B index: {s_b.index.tolist()}")
print(f"DataFrame (aligned by index):")
print(df_aligned)

print("\n[Benefits of Series dict approach]")
print("- Can use custom indices")
print("- Series can have different names")
print("- Index alignment is automatic")
print("- Good for combining related 1D data")

"""
================================================================================
MILESTONE 4: CREATING DATAFRAMES FROM RECORDS (LIST OF DICTS)
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 4: CREATING DATAFRAMES FROM RECORDS (LIST OF DICTS)")
print("="*80)

print("\n[Creating DataFrame from list of dicts]")
records = [
    {'Name': 'Alice', 'Role': 'Engineer', 'Department': 'Tech'},
    {'Name': 'Bob', 'Role': 'Manager', 'Department': 'Sales'},
    {'Name': 'Charlie', 'Role': 'Designer', 'Department': 'Tech'},
    {'Name': 'Diana', 'Role': 'Analyst', 'Department': 'Finance'}
]

df_records = pd.DataFrame(records)
print(f"Records (list of dicts):")
for r in records:
    print(f"  {r}")
print(f"\nCreated DataFrame:")
print(df_records)

print("\n[This approach is very common for JSON/API data]")
print("API responses often return arrays of objects (dicts)")
print("List of dicts is a natural way to represent them")

print("\n[Missing keys create NaN]")
records_sparse = [
    {'ID': 1, 'Name': 'Alice', 'Email': 'alice@example.com'},
    {'ID': 2, 'Name': 'Bob'},  # Email missing
    {'ID': 3, 'Email': 'charlie@example.com'},  # Name missing
]
df_sparse = pd.DataFrame(records_sparse)
print(f"Records with missing keys:")
print(df_sparse)

print("\n[Handling missing values]")
print("Missing keys create NaN (Not a Number)")
print("This is good - you can see data is incomplete immediately")

"""
================================================================================
MILESTONE 5: UNDERSTANDING DATAFRAME STRUCTURE
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 5: UNDERSTANDING DATAFRAME STRUCTURE")
print("="*80)

df = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [1200, 800, 400, 350],
    'Quantity': [50, 150, 200, 100],
    'Discount': [0.1, 0.05, 0.0, 0.15]
})

print(f"Sample DataFrame:")
print(df)

print("\n[Core attributes]")
print(f"df.shape: {df.shape} (rows, columns)")
print(f"df.columns: {df.columns.tolist()}")
print(f"df.index: {df.index.tolist()}")
print(f"df.dtypes:\n{df.dtypes}")

print("\n[Accessing specific parts]")
print(f"df.values (2D NumPy array):\n{df.values}\n")
print(f"First column (df['Product']):\n{df['Product'].to_list()}\n")
print(f"First row (df.iloc[0]):\n{df.iloc[0].to_dict()}")

print("\n[Quick stats]")
print(f"df.size (total elements): {df.size}")
print(f"df.ndim (dimensions): {df.ndim}")
print(f"df.empty: {df.empty}")

"""
================================================================================
MILESTONE 6: INSPECTING DATAFRAME ROWS AND COLUMNS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 6: INSPECTING DATAFRAME ROWS AND COLUMNS")
print("="*80)

df = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Score': [85.5, 92.0, 78.5, 88.0, 95.5],
    'Grade': ['B', 'A', 'C', 'B', 'A']
})

print(f"Sample DataFrame:")
print(df)

print("\n[Head and tail - inspect first/last rows]")
print(f"df.head() (first 5 rows, default):")
print(df.head())
print(f"\ndf.head(2) (first 2 rows):")
print(df.head(2))
print(f"\ndf.tail(2) (last 2 rows):")
print(df.tail(2))

print("\n[Info - high-level inspection]")
print("df.info() shows:")
print("  - Column names")
print("  - Non-null count (missing data indicator)")
print("  - Data types")
print("  - Memory usage")
print("\nOutput:")
df.info()

print("\n[Describe - statistical summary]")
print("df.describe() shows statistics for numeric columns:")
print(df.describe())

print("\n[Checking column names]")
print(f"df.columns: {df.columns.tolist()}")
print(f"'Name' in df.columns: {'Name' in df.columns}")
print(f"'Age' in df.columns: {'Age' in df.columns}")

print("\n[Checking data types]")
print(f"df.dtypes:\n{df.dtypes}")
print(f"df['Score'].dtype: {df['Score'].dtype}")
print(f"df['Grade'].dtype: {df['Grade'].dtype}")

print("\n[Checking for missing data]")
df_missing = df.copy()
df_missing.loc[1, 'Score'] = np.nan  # Introduce missing value
print(f"DataFrame with missing value:")
print(df_missing)
print(f"\ndf.isna():\n{df_missing.isna()}")
print(f"Missing count per column:\n{df_missing.isna().sum()}")

"""
================================================================================
MILESTONE 7: CREATING SAMPLE CSV FILE FOR LOADING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 7: CREATING SAMPLE CSV FILE FOR LOADING")
print("="*80)

print("\n[Creating a sample CSV file]")
sample_csv_content = """StudentID,Name,Math,English,Science,Grade
1001,Alice,85,90,88,B+
1002,Bob,92,85,90,A
1003,Charlie,78,82,80,B
1004,Diana,88,94,92,A
1005,Eve,95,92,94,A+
1006,Frank,81,79,83,B
1007,Grace,90,88,91,A"""

csv_file_path = 'student_scores.csv'
with open(csv_file_path, 'w') as f:
    f.write(sample_csv_content)

print(f"Created CSV file: {csv_file_path}")
print(f"Contents:\n{sample_csv_content}")

print("\n[CSV file structure]")
print("First line (header): StudentID,Name,Math,English,Science,Grade")
print("Lines 2-8 (data rows): Student records")
print("Each field separated by comma")
print("First column is StudentID (will become row index if requested)")

"""
================================================================================
MILESTONE 8: LOADING DATAFRAMES FROM CSV FILES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 8: LOADING DATAFRAMES FROM CSV FILES")
print("="*80)

print("\n[Loading CSV into DataFrame]")
df_csv = pd.read_csv(csv_file_path)
print(f"Loaded DataFrame from {csv_file_path}:")
print(df_csv)

print("\n[Understanding what was loaded]")
print(f"Shape: {df_csv.shape} (6 rows of data, 6 columns)")
print(f"Columns: {df_csv.columns.tolist()}")
print(f"Index: {df_csv.index.tolist()} (default 0-indexed)")
print(f"Data types:\n{df_csv.dtypes}")

print("\n[Loading with custom index]")
df_indexed = pd.read_csv(csv_file_path, index_col='StudentID')
print(f"DataFrame with StudentID as index:")
print(df_indexed)

print("\n[Loading specific columns]")
df_subset = pd.read_csv(csv_file_path, usecols=['Name', 'Math', 'English'])
print(f"DataFrame with selected columns:")
print(df_subset)

print("\n[Specifying data types]")
dtype_spec = {'StudentID': 'int32', 'Math': 'float32', 'English': 'float32'}
df_typed = pd.read_csv(csv_file_path, dtype=dtype_spec)
print(f"DataFrame with specified dtypes:")
print(df_typed.dtypes)

print("\n[Handling first row as data instead of header]")
print("(Not recommended, but showing capability)")
df_no_header = pd.read_csv(csv_file_path, header=None)
print(f"Loading without treating first row as header:")
print(df_no_header.head(3))

"""
================================================================================
MILESTONE 9: INSPECTING AFTER LOADING (THE SCENARIO)
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 9: INSPECTING AFTER LOADING (THE SCENARIO)")
print("="*80)

print("\n[SCENARIO: Loaded CSV, noticed unexpected column names/types]")
print("""
You load a CSV file into a DataFrame and notice that the column names 
or data types are not what you expected.

STEPS TO TAKE:
""")

df_loaded = pd.read_csv(csv_file_path)

print("\nSTEP 1: Check shape and basic info")
print(f"df.shape: {df_loaded.shape}")
print("✓ Confirms number of rows and columns loaded")

print("\nSTEP 2: Display first few rows")
print(f"df.head():")
print(df_loaded.head(3))
print("✓ Shows actual data to verify header interpretation")

print("\nSTEP 3: Check column names")
print(f"df.columns: {df_loaded.columns.tolist()}")
print(f"df.columns.dtype: {df_loaded.columns.dtype}")
print("✓ Confirms which names were read as headers")

print("\nSTEP 4: Check data types")
print(f"df.dtypes:")
print(df_loaded.dtypes)
print("✓ Shows if columns were interpreted as string, int, float, etc.")
print("  Mismatches here are common: '123' might be string not int")

print("\nSTEP 5: Check for missing data")
print(f"df.isna().sum():")
print(df_loaded.isna().sum())
print("✓ Shows which columns have missing values (NaN)")

print("\nSTEP 6: Use df.info() for comprehensive view")
print("df.info():")
df_loaded.info()
print("✓ Combines shape, dtypes, non-null counts, memory usage")

print("\nSTEP 7: Use df.describe() for numeric data")
print("df.describe():")
print(df_loaded.describe())
print("✓ Shows min, max, mean for numeric columns")
print("  Helps spot outliers or unexpected ranges")

print("\n[WHAT IF YOU SPOT ISSUES?]")
print("\nIssue: Column names not as expected")
print("  Solution: Use df.rename(columns={'old': 'new'})")
print("")
print("Issue: Data type wrong (string instead of int)")
print("  Solution: Reload with dtype={'ColName': 'int64'}")
print("           Or convert: df['Col'] = df['Col'].astype('int64')")
print("")
print("Issue: Missing values where unexpected")
print("  Solution: Check df.isna() to locate")
print("           Investigate CSV file for issues")
print("")
print("Issue: Header not recognized (data starts in wrong row)")
print("  Solution: Use pd.read_csv(file, skiprows=N, header=M)")

print("\n[BEST PRACTICE: VERIFY IMMEDIATELY]")
print("Always inspect your DataFrame right after loading!")
print("Catching issues early prevents analysis errors later")

"""
================================================================================
MILESTONE 10: DATA TYPE VERIFICATION AND CONVERSION
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 10: DATA TYPE VERIFICATION AND CONVERSION")
print("="*80)

df_types = pd.read_csv(csv_file_path)

print(f"Original dtypes from CSV:")
print(df_types.dtypes)

print("\n[Common dtype issues]")
print("1. Numeric columns read as 'object' (string) due to formatting")
print("2. Categorical data read as 'object' instead of 'category'")
print("3. Dates read as strings instead of datetime")

print("\n[Converting data types]")
print("\nConvert single column:")
df_types['StudentID'] = df_types['StudentID'].astype('int64')
print(f"After astype: {df_types['StudentID'].dtype}")

print("\nConvert multiple columns at once:")
df_types = pd.read_csv(csv_file_path)
conversion_dict = {'Math': 'float64', 'English': 'float64', 'Science': 'float64'}
df_types = df_types.astype(conversion_dict)
print(f"After batch conversion:")
print(df_types.dtypes)

print("\n[Checking dtype of specific column]")
print(f"df['Math'].dtype: {df_types['Math'].dtype}")
print(f"df['Name'].dtype: {df_types['Name'].dtype}")

print("\n[Data type categories]")
print("Numeric: int64, int32, float64, float32")
print("String: object (or 'string' in newer Pandas)")
print("Boolean: bool")
print("Categorical: category (efficient for repeated values)")
print("Datetime: datetime64[ns]")
print("Time delta: timedelta64[ns]")

"""
================================================================================
MILESTONE 11: BEST PRACTICES FOR DATAFRAME CREATION
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 11: BEST PRACTICES FOR DATAFRAME CREATION")
print("="*80)

print("\n[Best Practice 1: Verify immediately after creation/loading]")
print("DON'T: Load data and start analysis right away")
print("DO: Always run df.info() and df.head() first")

print("\n[Best Practice 2: Use meaningful column names]")
# DON'T:
df_bad = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(f"❌ Bad: {df_bad.columns.tolist()}")

# DO:
df_good = pd.DataFrame({'StudentCount': [1, 2, 3], 'AverageScore': [4, 5, 6]})
print(f"✓ Good: {df_good.columns.tolist()}")

print("\n[Best Practice 3: Specify dtypes when loading]")
print("DON'T: df = pd.read_csv(file)")
print("DO: df = pd.read_csv(file, dtype={'col1': 'int64', 'col2': 'float64'})")

print("\n[Best Practice 4: Use index_col appropriately]")
print("If CSV has ID column that should be index:")
print("  df = pd.read_csv(file, index_col='ID')")
print("This makes access and operations clearer")

print("\n[Best Practice 5: Handle missing data awareness]")
print("Always check: df.isna().sum()")
print("Before assuming complete data")

print("\n[Best Practice 6: Use head() and tail() before full iteration]")
print("DON'T: Start operations on entire large DataFrame")
print("DO: Test on df.head(100) first")

print("\n[Best Practice 7: Keep original DataFrame]")
df_original = pd.read_csv(csv_file_path)
df_working = df_original.copy()  # Make copy for modifications
print("Create a copy for filtering/transformations")
print("Keep original for reference and debugging")

print("\n[Best Practice 8: Check column names for spaces/special chars]")
df_check = pd.DataFrame({'Name ': [1], ' Age': [2]})  # Spaces!
print(f"Columns with spaces: {df_check.columns.tolist()}")
print("This causes bugs: df['Name'] fails, need df['Name ']")
print("Use df.columns.str.strip() to remove spaces")

print("\n[Best Practice 9: Understand index]")
print("Default index: integers 0, 1, 2, ...")
print("Custom index: Use index_col in read_csv()")
print("MultiIndex: For hierarchical data")
print("Always check: print(df.index)")

print("\n[Best Practice 10: Document your DataFrame]")
print("Add a comment explaining what each DataFrame represents")
print("Example:")
print("# df_sales: Monthly sales data by region")
print("# Columns: Date, Region, Product, Amount")
print("# Index: Sequential integers starting at 0")
print("# Time period: Jan 2023 - Dec 2023")

print("\n" + "="*80)
print("MILESTONE 15 SUMMARY")
print("="*80)
print("""
Creating and inspecting Pandas DataFrames enables structured data work.
Key concepts learned:

1. DataFrame Structure:
   - Rows: Observations/records
   - Columns: Features/attributes
   - Row index: Labels for rows (0-based by default)
   - Column names: Labels for columns

2. Creating DataFrames:
   - From dict of lists: pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
   - From dict of Series: pd.DataFrame({'A': series1, 'B': series2})
   - From list of dicts: pd.DataFrame([{'col1': 1, 'col2': 4}, ...])
   - From CSV: pd.read_csv(filename)

3. Inspection Methods:
   - df.head() / df.tail(): Preview rows
   - df.info(): Structure and types
   - df.describe(): Statistics for numeric data
   - df.shape: (rows, columns)
   - df.columns: Column names
   - df.dtypes: Data types per column

4. The Critical Scenario:
   After loading a CSV, ALWAYS inspect:
   - df.shape (did all data load?)
   - df.columns (are headers correct?)
   - df.head() (does data look right?)
   - df.info() (correct data types?)
   - df.isna().sum() (missing data?)
   
5. Data Types:
   - Verify numeric columns are numeric (not string)
   - Check for unexpected object dtype
   - Convert as needed with astype()
   - Plan for datetime conversion if needed

6. Best Practices:
   - Always verify immediately after creation/loading
   - Use meaningful column names
   - Specify dtypes when loading
   - Make a copy if you'll modify
   - Check for spaces/special chars in column names
   - Document what your DataFrame represents

Understanding DataFrames thoroughly is essential for all Pandas work!
""")

print("="*80)
print("END OF MILESTONE 15")
print("="*80)

# Clean up temporary CSV file
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"\nCleaned up: {csv_file_path}")
