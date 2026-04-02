"""
================================================================================
MILESTONE 16: LOADING CSV DATA INTO PANDAS DATAFRAMES
================================================================================

Understanding CSV Loading:
A comprehensive guide to safely loading CSV files into Pandas DataFrames,
verifying correct interpretation of rows and columns, and diagnosing
structural issues before analysis.

Milestones covered:
1. Introduction to CSV Loading
2. Basic CSV Loading with pd.read_csv()
3. Handling Headers and Column Names
4. Understanding Row Indices
5. Preview and Inspection Methods
6. Dealing with Missing Values in CSV
7. Specifying Data Types During Loading
8. Handling Encoding Issues
9. The Scenario: Diagnosing Misaligned Data
10. Common CSV Loading Issues and Solutions
11. Best Practices for Safe CSV Loading

================================================================================
MILESTONE 1: INTRODUCTION TO CSV LOADING
================================================================================
"""

import numpy as np
import pandas as pd
import os

print("="*80)
print("MILESTONE 1: INTRODUCTION TO CSV LOADING")
print("="*80)

print("\n[What is CSV?]")
print("CSV = Comma-Separated Values")
print("A plain text format for storing tabular data:")
print("  - Each line = one row")
print("  - Each comma separates values (columns)")
print("  - First line (usually) = headers")
print("")
print("Example CSV content:")
print("  Name,Age,Salary")
print("  Alice,25,50000")
print("  Bob,30,60000")
print("  Charlie,35,75000")

print("\n[Why CSV?]")
print("- Simple, human-readable format")
print("- Universal (works everywhere: Excel, databases, etc.)")
print("- Lightweight (small file size)")
print("- Easy to create/edit")
print("- Industry standard for data exchange")

print("\n[Loading CSV into Pandas]")
print("Pandas pd.read_csv() is the standard way to load CSV files")
print("It returns a DataFrame with proper structure")

print("\n[Checking Pandas Version]")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")

"""
================================================================================
MILESTONE 2: BASIC CSV LOADING WITH pd.read_csv()
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 2: BASIC CSV LOADING WITH pd.read_csv()")
print("="*80)

# Create sample CSV files for demonstration
print("\n[Creating sample CSV files]")

# File 1: Simple employee data
csv1_content = """EmployeeID,Name,Department,Salary,HireDate
1001,Alice,Engineering,75000,2020-01-15
1002,Bob,Sales,60000,2019-06-20
1003,Charlie,Engineering,80000,2021-03-10
1004,Diana,HR,55000,2020-11-05
1005,Eve,Sales,62000,2021-08-12"""

csv1_file = 'employees.csv'
with open(csv1_file, 'w') as f:
    f.write(csv1_content)

print(f"Created: {csv1_file}")
print(f"Content:\n{csv1_content}\n")

# File 2: Sales data with mixed types
csv2_content = """Date,Product,Quantity,Price,Total
2024-01-01,Laptop,5,1200,6000
2024-01-02,Phone,12,800,9600
2024-01-03,Tablet,8,400,3200
2024-01-04,Monitor,15,350,5250
2024-01-05,Keyboard,25,100,2500"""

csv2_file = 'sales.csv'
with open(csv2_file, 'w') as f:
    f.write(csv2_content)

print(f"Created: {csv2_file}")
print(f"Content:\n{csv2_content}\n")

print("\n[Loading CSV - Basic Usage]")
print("df = pd.read_csv('employees.csv')")
df_emp = pd.read_csv(csv1_file)

print(f"\nLoaded DataFrame:")
print(df_emp)

print(f"\nDataFrame type: {type(df_emp)}")
print(f"Shape: {df_emp.shape}")
print(f"Columns: {df_emp.columns.tolist()}")

print("\n[Loading second CSV file]")
df_sales = pd.read_csv(csv2_file)
print(df_sales)

print("\n[How pd.read_csv() works]")
print("1. Reads first line as column headers (default)")
print("2. Reads remaining lines as data rows")
print("3. Determines data types automatically")
print("4. Creates integer index starting from 0")
print("5. Returns a fully-formed DataFrame")

"""
================================================================================
MILESTONE 3: HANDLING HEADERS AND COLUMN NAMES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 3: HANDLING HEADERS AND COLUMN NAMES")
print("="*80)

print("\n[Default header behavior]")
print("By default, first row is treated as column names (headers)")
df_default = pd.read_csv(csv1_file)
print(f"Column names: {df_default.columns.tolist()}")
print(f"First row of data: {df_default.iloc[0].to_dict()}")

print("\n[What if file has NO header?]")
# Create CSV without header
csv_no_header = """1001,Alice,Engineering,75000,2020-01-15
1002,Bob,Sales,60000,2019-06-20
1003,Charlie,Engineering,80000,2021-03-10"""

csv_no_header_file = 'no_header.csv'
with open(csv_no_header_file, 'w') as f:
    f.write(csv_no_header)

print(f"File content (no headers):\n{csv_no_header}\n")

# Default (treats first row as header - WRONG!)
print("Default behavior (WRONG for this file):")
df_wrong = pd.read_csv(csv_no_header_file)
print(df_wrong)
print(f"Column names: {df_wrong.columns.tolist()}")
print("Notice: First row treated as header, wrong!")

# Correct (tell Pandas there's no header)
print("\nCorrected (header=None):")
df_correct = pd.read_csv(csv_no_header_file, header=None)
print(df_correct)
print(f"Column names: {df_correct.columns.tolist()}")
print("Columns renamed to 0, 1, 2, ...")

# Assign meaningful names
print("\nAssigning column names after loading:")
df_correct.columns = ['EmployeeID', 'Name', 'Department', 'Salary', 'HireDate']
print(df_correct)

print("\n[What if header is not in first row?]")
csv_delayed_header = """Some metadata about this file
Created on 2024-01-01
EmployeeID,Name,Department,Salary,HireDate
1001,Alice,Engineering,75000,2020-01-15
1002,Bob,Sales,60000,2019-06-20"""

csv_delayed_file = 'delayed_header.csv'
with open(csv_delayed_file, 'w') as f:
    f.write(csv_delayed_header)

print(f"File content (header in row 3):\n{csv_delayed_header}\n")

# Wrong way
print("Wrong way (uses row 1 as header):")
try:
    df_wrong2 = pd.read_csv(csv_delayed_file)
    print(df_wrong2.head())
except pd.errors.ParserError as e:
    print(f"❌ Error: {str(e)[:100]}...")
    print("This happens because metadata doesn't parse as CSV data")

# Correct way - skip first 2 rows
print("\nCorrect way (skip 2 rows, use row 3 as header):")
df_correct2 = pd.read_csv(csv_delayed_file, skiprows=2)
print(df_correct2)

print("\n[Renaming columns after loading]")
df_rename = pd.read_csv(csv1_file)
print(f"Original columns: {df_rename.columns.tolist()}")

df_rename.columns = ['ID', 'Employee', 'Dept', 'Pay', 'Hired']
print(f"Renamed columns: {df_rename.columns.tolist()}")
print(df_rename.head(2))

"""
================================================================================
MILESTONE 4: UNDERSTANDING ROW INDICES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 4: UNDERSTANDING ROW INDICES")
print("="*80)

print("\n[Default row index]")
df_idx = pd.read_csv(csv1_file)
print(f"Row index: {df_idx.index.tolist()}")
print(f"Index type: {type(df_idx.index)}")
print(f"Index name: {df_idx.index.name}")

print("\n[Using a CSV column as index]")
print("If CSV has an ID column that should be the index:")

# Without setting index
df_no_idx = pd.read_csv(csv1_file)
print(f"Without index_col:")
print(df_no_idx)
print(f"Index: {df_no_idx.index.tolist()}")

# With index_col parameter
print(f"\nWith index_col='EmployeeID':")
df_with_idx = pd.read_csv(csv1_file, index_col='EmployeeID')
print(df_with_idx)
print(f"Index: {df_with_idx.index.tolist()}")
print("EmployeeID is now the row index, not a column")

print("\n[Accessing rows by index]")
print("df.loc[1001]:")
print(df_with_idx.loc[1001])

print("\n[Why use custom index?]")
print("- Makes data more intuitive (look up by ID, not position)")
print("- Enables efficient lookups")
print("- More readable code")
print("- Aligns with domain understanding (employee by ID)")

"""
================================================================================
MILESTONE 5: PREVIEW AND INSPECTION METHODS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 5: PREVIEW AND INSPECTION METHODS")
print("="*80)

df = pd.read_csv(csv1_file)

print(f"Sample DataFrame:")
print(df)

print("\n[Method 1: head() - first rows]")
print(f"df.head() (first 5 rows):")
print(df.head())

print(f"\ndf.head(2) (first 2 rows):")
print(df.head(2))

print("\n[Method 2: tail() - last rows]")
print(f"df.tail(2) (last 2 rows):")
print(df.tail(2))

print("\n[Method 3: info() - structure overview]")
print(f"df.info():")
df.info()

print("\n[Method 4: describe() - statistics]")
print(f"df.describe():")
print(df.describe())

print("\n[Method 5: shape - dimensions]")
print(f"df.shape: {df.shape} (5 rows, 5 columns)")

print("\n[Method 6: columns - column names]")
print(f"df.columns: {df.columns.tolist()}")

print("\n[Method 7: index - row index]")
print(f"df.index: {df.index.tolist()}")

print("\n[Method 8: dtypes - data types]")
print(f"df.dtypes:")
print(df.dtypes)

print("\n[Quick verification checklist]")
print("After loading any CSV:")
print("  ☐ df.shape - correct number of rows and columns?")
print("  ☐ df.head() - headers recognized? Data looks right?")
print("  ☐ df.columns - are column names what you expect?")
print("  ☐ df.dtypes - data types appropriate?")
print("  ☐ df.index - row index is what you expect?")
print("  ☐ df.info() - non-null counts show missing data?")

"""
================================================================================
MILESTONE 6: DEALING WITH MISSING VALUES IN CSV
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 6: DEALING WITH MISSING VALUES IN CSV")
print("="*80)

print("\n[Creating CSV with missing values]")
csv_missing = """Name,Score,Grade
Alice,85,B
Bob,,C
Charlie,92,A
,88,B
Eve,95,"""

csv_missing_file = 'missing.csv'
with open(csv_missing_file, 'w') as f:
    f.write(csv_missing)

print(f"File content (missing values):\n{csv_missing}\n")

print("[Loading CSV with missing values]")
df_missing = pd.read_csv(csv_missing_file)
print(df_missing)

print("\n[Identifying missing values]")
print("df.isna() (True where missing):")
print(df_missing.isna())

print("\ndf.isna().sum() (count missing per column):")
print(df_missing.isna().sum())

print("\ndf.isnull() (same as isna()):")
print(df_missing.isnull())

print("\n[How missing values appear in CSV]")
print("Empty between commas: name,, height → Score is NaN")
print("No value before quote: ,88, → Name is NaN")
print("End of line with comma: ...,  → Grade is NaN")

print("\n[Handling missing values]")
print("Option 1: Drop rows with missing:")
df_dropped = df_missing.dropna()
print(f"After dropna():\n{df_dropped}")

print("\nOption 2: Fill with default value:")
df_filled = df_missing.fillna('Unknown')
print(f"After fillna('Unknown'):\n{df_filled}")

print("\n[Specifying what values mean missing]")
csv_missing_text = """Name,Score,Status
Alice,85,Present
Bob,NA,Absent
Charlie,92,Present
Diana,77,N/A"""

csv_missing_text_file = 'missing_text.csv'
with open(csv_missing_text_file, 'w') as f:
    f.write(csv_missing_text)

# Default - treats as string
print("Default (treats 'NA' as string):")
df_text = pd.read_csv(csv_missing_text_file)
print(df_text)
print(f"Score dtype: {df_text['Score'].dtype}")

# Specify NA values
print("\nWith na_values=['NA', 'N/A'] (treats as NaN):")
df_na = pd.read_csv(csv_missing_text_file, na_values=['NA', 'N/A'])
print(df_na)
print(f"Score dtype: {df_na['Score'].dtype}")

"""
================================================================================
MILESTONE 7: SPECIFYING DATA TYPES DURING LOADING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 7: SPECIFYING DATA TYPES DURING LOADING")
print("="*80)

print("\n[Automatic dtype detection]")
df_auto = pd.read_csv(csv1_file)
print("Automatic dtypes:")
print(df_auto.dtypes)

print("\n[Problem: Numeric as string]")
csv_numeric_string = """ID,Amount,Quantity
001,1000.50,10
002,2000.75,20
003,1500.00,15"""

csv_num_file = 'numeric.csv'
with open(csv_num_file, 'w') as f:
    f.write(csv_numeric_string)

df_auto_num = pd.read_csv(csv_num_file)
print("Without dtype specification:")
print(df_auto_num.dtypes)
print("ID is 'object' (string) even though it looks numeric!")

print("\n[Solution: Specify dtype]")
df_typed = pd.read_csv(csv_num_file, dtype={'ID': 'int64', 'Amount': 'float64'})
print("With dtype specification:")
print(df_typed.dtypes)
print("ID is now int64, Amount is float64")

print("\n[Specifying multiple dtypes]")
dtype_dict = {
    'EmployeeID': 'int64',
    'Salary': 'float64',
    'Name': 'string',
    'Department': 'category'
}
df_multi_type = pd.read_csv(csv1_file, dtype=dtype_dict)
print("Multiple dtype specifications:")
print(df_multi_type.dtypes)

print("\n[Why specify dtype?]")
print("- Prevents misinterpretation")
print("- Saves memory (int32 smaller than object)")
print("- Enables correct operations")
print("- Catches data anomalies (if can't convert, error)")

"""
================================================================================
MILESTONE 8: HANDLING ENCODING ISSUES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 8: HANDLING ENCODING ISSUES")
print("="*80)

print("\n[What is encoding?]")
print("Encoding = how text is stored as bytes in files")
print("Common encodings: UTF-8 (default), Latin-1, ASCII, CP1252")
print("Different regions/systems use different encodings")

print("\n[Default encoding (UTF-8)]")
print("Pandas defaults to UTF-8, which handles most cases")

print("\n[When encoding issues occur]")
print("- Files created in different systems (Windows vs Mac vs Linux)")
print("- Files with special characters")
print("- Old systems using legacy encodings")
print("- Excel files exported to CSV with Windows encoding")

print("\n[Example: Latin-1 encoded file]")
# Create a simple example showing encoding parameter
csv_simple = """Name,City
Alice,São Paulo
Bob,Montréal
Charlie,Zürich"""

csv_encoding_file = 'encoding_test.csv'
# Write with UTF-8 (default)
with open(csv_encoding_file, 'w', encoding='utf-8') as f:
    f.write(csv_simple)

print(f"File content:\n{csv_simple}\n")

print("Loading with default encoding (UTF-8):")
df_utf8 = pd.read_csv(csv_encoding_file)
print(df_utf8)

print("\n[Specifying encoding]")
print("If you encounter encoding errors:")
print("  df = pd.read_csv('file.csv', encoding='latin-1')")
print("  df = pd.read_csv('file.csv', encoding='cp1252')")
print("  df = pd.read_csv('file.csv', encoding='iso-8859-1')")

print("\n[Error handling]")
print("df = pd.read_csv('file.csv', encoding='utf-8', on_bad_lines='warn')")
print("This warns about bad lines instead of failing")

"""
================================================================================
MILESTONE 9: THE SCENARIO - DIAGNOSING MISALIGNED DATA
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 9: THE SCENARIO - DIAGNOSING MISALIGNED DATA")
print("="*80)

print("\n[SCENARIO: Data appears misaligned, columns not expected]")
print("""
You load a CSV file but notice:
- First row appears to be data, not headers
- Column names are 0, 1, 2, 3, ... (not meaningful)
- Data doesn't align with what you expected
- Some columns are missing or extra

What steps would you take to diagnose?
""")

# Create a problematic CSV
csv_problem = """Some Header Info
This file contains employee data
Employee Records
EmployeeID,Name,Salary
1001,Alice,75000
1002,Bob,60000"""

csv_problem_file = 'problem.csv'
with open(csv_problem_file, 'w') as f:
    f.write(csv_problem)

print("Problematic CSV file:")
print(csv_problem)

print("\n[STEP 1: Load with default settings]")
df_problem = pd.read_csv(csv_problem_file)
print("df = pd.read_csv('problem.csv')")
print(df_problem)
print("❌ Problem: Metadata treated as data, wrong columns!")

print("\n[STEP 2: Inspect the structure]")
print(f"Shape: {df_problem.shape}")
print(f"Columns: {df_problem.columns.tolist()}")
print(f"First row: {df_problem.iloc[0].to_dict()}")
print("Identify: First column 'Some Header Info' - this is metadata!")

print("\n[STEP 3: Look at the original file]")
print("Open the CSV file in a text editor to see structure")
print("Count how many lines are metadata vs data")
print("Identify where actual headers are")

print("\n[STEP 4: Determine parameters needed]")
print("In this case: skiprows=3, uses row 4 as header")

print("\n[STEP 5: Load with corrected parameters]")
df_fixed = pd.read_csv(csv_problem_file, skiprows=3)
print("df = pd.read_csv('problem.csv', skiprows=3)")
print(df_fixed)
print("✓ Fixed! Headers recognized, data aligned correctly")

print("\n[STEP 6: Verify after fix]")
print(f"Shape: {df_fixed.shape}")
print(f"Columns: {df_fixed.columns.tolist()}")
print(f"dtypes:\n{df_fixed.dtypes}")
print("✓ All looks correct now")

print("\n[DIAGNOSTIC WORKFLOW]")
print("""
When data appears misaligned:

1. INSPECT DEFAULT LOAD
   - df.head()
   - df.columns
   - df.dtypes
   - Look for anomalies

2. IDENTIFY PROBLEM
   - Are headers recognized?
   - Is data in wrong rows?
   - Are there NaN values indicating misalignment?

3. EXAMINE FILE DIRECTLY
   - Open in text editor
   - Look for metadata, comments, unusual first rows
   - Count lines before actual headers

4. DETERMINE SOLUTION
   - skiprows=N to skip metadata
   - header=N if headers not in row 1
   - na_values=[] if certain values mean missing
   - encoding if special characters corrupted

5. RELOAD WITH PARAMETERS
   - df = pd.read_csv(file, skiprows=3, header=0)

6. VERIFY RESULT
   - df.head()
   - df.info()
   - df.dtypes
   - Do columns make sense now?
""")

"""
================================================================================
MILESTONE 10: COMMON CSV LOADING ISSUES AND SOLUTIONS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 10: COMMON CSV LOADING ISSUES AND SOLUTIONS")
print("="*80)

print("\n[Issue 1: Delimiter is not a comma]")
print("Some CSV files use semicolons, tabs, or pipes")

csv_semicolon = "Name;Age;Salary\nAlice;25;50000\nBob;30;60000"
csv_semi_file = 'semicolon.csv'
with open(csv_semi_file, 'w') as f:
    f.write(csv_semicolon)

print(f"File with semicolon delimiter:\n{csv_semicolon}\n")

print("Default (wrong - treats as single column):")
df_wrong_delim = pd.read_csv(csv_semi_file)
print(df_wrong_delim)

print("\nCorrected (sep=';'):")
df_right_delim = pd.read_csv(csv_semi_file, sep=';')
print(df_right_delim)

print("\n[Issue 2: Rows with extra commas inside quoted fields]")
csv_quoted = """ID,Name,Description,Price
1,"Smith, John","Product, type A",100
2,"Jones, Bob","Item, type B",200"""

csv_quoted_file = 'quoted.csv'
with open(csv_quoted_file, 'w') as f:
    f.write(csv_quoted)

print(f"File with quoted fields:\n{csv_quoted}\n")

print("Pandas handles this correctly by default:")
df_quoted = pd.read_csv(csv_quoted_file)
print(df_quoted)
print("Notice: Commas inside quotes are preserved")

print("\n[Issue 3: Blank rows creating NaN rows]")
csv_blank = """ID,Name,Score
1,Alice,85

2,Bob,90"""

csv_blank_file = 'blank_rows.csv'
with open(csv_blank_file, 'w') as f:
    f.write(csv_blank)

print(f"File with blank row:\n{csv_blank}\n")

print("Default (creates NaN row):")
df_blank = pd.read_csv(csv_blank_file)
print(df_blank)

print("\nWith skip_blank_lines=True:")
df_no_blank = pd.read_csv(csv_blank_file, skip_blank_lines=True)
print(df_no_blank)

print("\n[Issue 4: Column names have spaces]")
csv_spaces = """Student ID, First Name , Age"""

csv_space_file = 'spaces.csv'
with open(csv_space_file, 'w') as f:
    f.write(csv_spaces)

print(f"File with spaces in headers:\n{csv_spaces}\n")

df_spaces = pd.read_csv(csv_space_file)
print("Column names with spaces:")
print(df_spaces.columns.tolist())
print("❌ Problem: Can't access df['First Name'] - has spaces!")

print("\nSolution 1: Strip spaces from column names")
df_spaces.columns = df_spaces.columns.str.strip()
print(f"Stripped: {df_spaces.columns.tolist()}")

print("\nSolution 2: Rename columns")
df_spaces.columns = ['StudentID', 'FirstName', 'Age']
print(f"Renamed: {df_spaces.columns.tolist()}")

"""
================================================================================
MILESTONE 11: BEST PRACTICES FOR SAFE CSV LOADING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 11: BEST PRACTICES FOR SAFE CSV LOADING")
print("="*80)

print("\n[Best Practice 1: Always inspect immediately after loading]")
print("DON'T: df = pd.read_csv(file); df.some_analysis()")
print("DO:")
print("  df = pd.read_csv(file)")
print("  print(df.head())")
print("  print(df.info())")
print("  print(df.shape)")

print("\n[Best Practice 2: Specify dtypes to catch issues]")
print("DON'T: df = pd.read_csv(file)  # Hope dtypes are right")
print("DO:")
print("  df = pd.read_csv(file, dtype={'col1': 'int64', 'col2': 'float64'})")

print("\n[Best Practice 3: Handle encoding explicitly for international data]")
print("DON'T: df = pd.read_csv(file)  # Assume UTF-8")
print("DO:")
print("  df = pd.read_csv(file, encoding='utf-8')")

print("\n[Best Practice 4: Use index_col if appropriate]")
print("If a column is an ID that should be the index:")
print("  df = pd.read_csv(file, index_col='ID')")

print("\n[Best Practice 5: Specify missing value representation]")
print("DON'T: Let Pandas guess (might miss 'NA', 'N/A', etc.)")
print("DO:")
print("  df = pd.read_csv(file, na_values=['NA', 'N/A', '-'])")

print("\n[Best Practice 6: Keep original, work on copy]")
print("df_original = pd.read_csv(file)")
print("df = df_original.copy()  # Work on copy")
print("# Now you can always reference df_original if needed")

print("\n[Best Practice 7: Document loading parameters]")
print("# Good practice: add a comment")
print("""
# Load sales data from Q1 report
# Note: File has metadata in first 3 rows, uses semicolon delimiter
df = pd.read_csv('q1_sales.csv', skiprows=3, sep=';')
""")

print("\n[Best Practice 8: Verify row count and headers match file]")
print("After loading, check:")
print("  - df.shape[0]: Is this reasonable?")
print("  - df.shape[1]: Expected number of columns?")
print("  - df.columns: Do they look right?")

print("\n[Best Practice 9: Check for NaN immediately]")
print("After loading:")
print("  print(df.isna().sum())")
print("  print(df.isnull().any())")
print("Understand where missing data is before proceeding")

print("\n[Best Practice 10: Test on sample before production]")
print("For large files:")
print("  df = pd.read_csv(file, nrows=100)  # Load first 100")
print("  # Verify structure is correct")
print("  df = pd.read_csv(file)  # Load full file when ready")

print("\n" + "="*80)
print("MILESTONE 16 SUMMARY")
print("="*80)
print("""
Safe CSV loading is foundational for all data work.
Key concepts learned:

1. Basic Loading:
   - pd.read_csv(filename) returns a DataFrame
   - First row is header by default
   - Automatic index from 0 onwards

2. Parameter Control:
   - header=N: Which row is the header
   - skiprows=N: Skip first N rows
   - index_col='ColumnName': Use column as index
   - dtype={'col': 'type'}: Specify data types
   - sep=';': Use different delimiter
   - na_values=['NA', '-']: Define missing values
   - encoding='utf-8': Specify encoding

3. Inspection Methods:
   - df.head(): First rows (visual check)
   - df.info(): Structure and types
   - df.describe(): Statistics
   - df.shape: (rows, columns)
   - df.columns: Column names
   - df.dtypes: Data types

4. The Critical Workflow:
   Load → Inspect → Diagnose → Fix parameters → Reload → Verify
   
5. Common Issues:
   - Headers in wrong row → use skiprows or header
   - Metadata at top → use skiprows
   - Non-numeric columns as numbers → check data
   - Missing values → use na_values or fillna
   - Delimiter wrong → use sep
   - Encoding issues → use encoding

6. The Scenario:
   If data appears misaligned:
   - Inspect with head(), info()
   - Look at original file in text editor
   - Identify metadata, encoding, delimiter
   - Apply correct parameters
   - Reload and verify

7. Best Practices:
   - Always inspect immediately after loading
   - Specify dtypes for validation
   - Handle encoding explicitly
   - Use index_col if appropriate
   - Specify na_values for missing data
   - Keep original, work on copy
   - Document your parameters
   - Test before full load
   
Safe loading prevents hours of debugging later. Never skip this step!
""")

print("="*80)
print("END OF MILESTONE 16")
print("="*80)

# Clean up temporary CSV files
for file in [csv1_file, csv2_file, csv_no_header_file, csv_delayed_file, 
             csv_missing_file, csv_missing_text_file, csv_num_file, 
             csv_encoding_file, csv_problem_file, csv_semi_file, 
             csv_quoted_file, csv_blank_file, csv_space_file]:
    if os.path.exists(file):
        os.remove(file)

print("\nCleaned up temporary CSV files")
