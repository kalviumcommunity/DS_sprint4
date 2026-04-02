"""
================================================================================
MILESTONE 18: UNDERSTANDING DATA SHAPES AND COLUMN DATA TYPES
================================================================================

Understanding DataFrame Structure:
A comprehensive guide to inspecting DataFrame shape and column data types
to correctly understand dataset size, structure, and type compatibility
before analysis.

Milestones covered:
1. Introduction to DataFrame Shape and Types
2. The Shape Property: Rows and Columns
3. Interpreting Shape (N, M) Notation
4. Understanding Column Data Types
5. Data Type Categories and Characteristics
6. Why Data Types Matter for Operations
7. Inspecting and Verifying Column Types
8. The Scenario: Type Mismatch Errors
9. Prevention Strategies
10. Common Data Type Issues
11. Best Practices for Structure Understanding

================================================================================
MILESTONE 1: INTRODUCTION TO DATAFRAME SHAPE AND TYPES
================================================================================
"""

import numpy as np
import pandas as pd
import os

print("="*80)
print("MILESTONE 1: INTRODUCTION TO DATAFRAME SHAPE AND TYPES")
print("="*80)

print("\n[What is DataFrame structure?]")
print("Structure = Shape + Data Types")
print("Shape = How many rows and columns")
print("Types = What kind of data is in each column")

print("\n[Why understanding structure is critical]")
print("- Know how much data you have")
print("- Understand what operations are possible")
print("- Prevent type errors before they happen")
print("- Allocate appropriate memory")
print("- Design analysis strategies")

print("\n[The two key concepts]")
print("1. SHAPE: df.shape attribute")
print("   Returns (number_of_rows, number_of_columns)")
print("   Example: (1000, 15) means 1000 rows, 15 columns")
print("")
print("2. DTYPES: df.dtypes or df.dtypes property")
print("   Shows data type of each column")
print("   Example: Age is int64, Name is object (string)")

print("\n[Creating sample data for demonstration]")

csv_content = """ProductID,ProductName,Category,Price,Quantity,InStock,LastRestockDate
101,Laptop,Electronics,1299.99,45,True,2024-01-15
102,Mouse,Electronics,29.99,150,True,2024-01-10
103,Desk,Furniture,349.50,12,False,2023-12-20
104,Chair,Furniture,199.99,28,True,2024-01-05
105,Monitor,Electronics,399.99,8,False,2023-12-10
106,Keyboard,Electronics,79.99,62,True,2024-01-12
107,Bookshelf,Furniture,299.99,5,True,2023-11-30
108,Lamp,Furniture,89.99,20,True,2024-01-08"""

csv_file = 'products.csv'
with open(csv_file, 'w') as f:
    f.write(csv_content)

print(f"Created: {csv_file}")
df = pd.read_csv(csv_file)
print(f"Sample content:\n{csv_content[:150]}...\n")
print("DataFrame loaded successfully")

"""
================================================================================
MILESTONE 2: THE SHAPE PROPERTY - ROWS AND COLUMNS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 2: THE SHAPE PROPERTY - ROWS AND COLUMNS")
print("="*80)

print("\n[What is df.shape?]")
print("df.shape is a tuple with two elements:")
print("  (number_of_rows, number_of_columns)")
print("")
print("It's ONE of the most important properties")

print("\n[Getting the shape]")
print(f"df.shape = {df.shape}")
print(f"Type: {type(df.shape)}")
print(f"Length of tuple: {len(df.shape)}")

print("\n[Unpacking the shape]")
rows, cols = df.shape
print(f"Rows: {rows}")
print(f"Columns: {cols}")

print("\n[Alternative ways to get shape components]")
print(f"df.shape[0] (rows): {df.shape[0]}")
print(f"df.shape[1] (columns): {df.shape[1]}")
print(f"len(df) (rows): {len(df)}")
print(f"len(df.columns) (columns): {len(df.columns)}")

print("\n[What rows represent]")
print("Rows = Individual records/observations")
print("Each row is one complete record")
print("Examples:")
print("  - Sales data: Each row is one sale")
print("  - Student data: Each row is one student")
print("  - Product data: Each row is one product")
print(f"In our data: {rows} products")

print("\n[What columns represent]")
print("Columns = Attributes/features/variables")
print("Each column is one attribute")
print("Examples:")
print("  - Sales data: Amount, Date, Region columns")
print("  - Student data: Name, Age, GPA columns")
print("  - Product data: Name, Price, Category columns")
print(f"In our data: {cols} attributes per product")

print("\n[Visualizing shape]")
print("Imagine a spreadsheet:")
print(f"  {cols} columns ------>")
print(f"  Column names: [ProductID, ProductName, Category, ...]")
print(f"  |")
print(f"  | {rows} rows")
print(f"  |")
print(f"  V")
print(f"  Each cell = one value")
print(f"  Total cells = {rows} * {cols} = {rows * cols}")

"""
================================================================================
MILESTONE 3: INTERPRETING SHAPE (N, M) NOTATION
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 3: INTERPRETING SHAPE (N, M) NOTATION")
print("="*80)

print("\n[The (N, M) format]")
print("DataFrame shape always returns (N, M) where:")
print("  N = number of rows")
print("  M = number of columns")
print("")
print("NOT (columns, rows) - always rows first!")

print("\n[Examples of shape interpretation]")
examples = [
    (100, 5),
    (50000, 20),
    (1, 10),
    (1000, 1),
    (0, 5),
    (5, 0),
]

for shape in examples:
    rows, cols = shape
    print(f"Shape {shape}: {rows} rows, {cols} columns")
    if rows == 0:
        print(f"  -> Empty DataFrame (no data rows)")
    elif cols == 0:
        print(f"  -> No columns (unusual)")
    else:
        print(f"  -> {rows * cols} total cells")

print("\n[What shape tells you about data size]")
print("Small shape (10, 5): Tiny dataset")
print("Medium shape (1000, 20): Typical working dataset")
print("Large shape (1000000, 50): Big data (memory concerns)")
print("Wide shape (100, 1000): More features than rows")
print("Tall shape (100000, 10): More rows than features")

print("\n[Shape vs len() vs info()]")
print(f"df.shape: {df.shape} (tuple)")
print(f"len(df): {len(df)} (int, number of rows only)")
print(f"df.shape[0]: {df.shape[0]} (rows from shape)")
print(f"df.shape[1]: {df.shape[1]} (columns from shape)")

print("\n[Important note: Column count]")
print("Shape[1] = number of columns currently in DataFrame")
print("This can change if you add/remove columns")
print("Original CSV might have more columns (some filtered)")

"""
================================================================================
MILESTONE 4: UNDERSTANDING COLUMN DATA TYPES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 4: UNDERSTANDING COLUMN DATA TYPES")
print("="*80)

print("\n[What are column data types?]")
print("Data type = The kind of data stored in each column")
print("Pandas assigns type to each column")
print("Type determines what operations are possible")

print("\n[Viewing all column data types]")
print("df.dtypes:")
print(df.dtypes)

print("\n[Viewing dtype of specific column]")
print("df['Price'].dtype:", df['Price'].dtype)
print("df['ProductName'].dtype:", df['ProductName'].dtype)
print("df['InStock'].dtype:", df['InStock'].dtype)

print("\n[Common pandas data types]")
print("Numeric types:")
print("  int64   - Integer (no decimals: 42, -10, 0)")
print("  int32   - 32-bit integer (smaller, older systems)")
print("  float64 - Floating point (decimals: 3.14, 99.99, -0.5)")
print("  float32 - 32-bit float (smaller)")
print("")
print("Text type:")
print("  object  - Usually strings (text, mixed types)")
print("  str     - Modern Pandas string type")
print("")
print("Logical type:")
print("  bool    - Boolean (True/False)")
print("")
print("Temporal type:")
print("  datetime64 - Dates and times")
print("")
print("Special type:")
print("  category - Categorical (fixed set of values)")

print("\n[Inspecting our product data types]")
for col, dtype in df.dtypes.items():
    print(f"{col:20} -> {dtype}")

print("\n[Type summary for our data]")
numeric_cols = df.select_dtypes(include='number').columns.tolist()
string_cols = df.select_dtypes(include='object').columns.tolist()
bool_cols = df.select_dtypes(include='bool').columns.tolist()

print(f"Numeric columns ({len(numeric_cols)}): {numeric_cols}")
print(f"String columns ({len(string_cols)}): {string_cols}")
print(f"Boolean columns ({len(bool_cols)}): {bool_cols}")

"""
================================================================================
MILESTONE 5: DATA TYPE CATEGORIES AND CHARACTERISTICS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 5: DATA TYPE CATEGORIES AND CHARACTERISTICS")
print("="*80)

print("\n[Numeric types]")
print("int64: Integers (whole numbers)")
print("  Examples: 1, -42, 0, 1000")
print("  Operations: +, -, *, /, >, <, ==")
print("  Memory: 8 bytes per value")

print("\nfloat64: Decimals")
print("  Examples: 3.14, -99.99, 0.5")
print("  Operations: +, -, *, /, >, <, ==")
print("  Memory: 8 bytes per value")

print("\nint vs float: Key difference")
print("  int64('5') + int64('3') = int64(8)")
print("  float64(5.5) + float64(3.2) = float64(8.7)")
print("  int64(5) + float64(3.5) = float64(8.5) [converts to float]")

print("\n[String types]")
print("object: Usually strings (text, but can be mixed)")
print("  Examples: 'Alice', 'Product Name', 'Category1'")
print("  Operations: +, len(), str methods")
print("  Memory: Variable, usually more than numeric")

print("\nstr: Modern Pandas string type")
print("  Examples: 'text', 'value'")
print("  Newer Pandas versions recommend this over object")
print("  Better for string-specific operations")

print("\n[Boolean type]")
print("bool: True or False only")
print("  Examples: True, False")
print("  Operations: &, |, ~, and, or")
print("  Memory: 1 byte per value")

print("\n[Date/Time type]")
print("datetime64: Dates and times")
print("  Examples: 2024-01-15, 2024-01-15 14:30:00")
print("  Operations: Date arithmetic (subtract to get days)")
print("  Memory: 8 bytes per value")

print("\n[Why type matters]")
print("Type determines valid operations")
print("int64 column: Can compute sum(), mean(), max()")
print("object column: Cannot compute mean() (error)")
print("bool column: Can use & (and), | (or)")
print("datetime64: Can compute time differences")

"""
================================================================================
MILESTONE 6: WHY DATA TYPES MATTER FOR OPERATIONS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 6: WHY DATA TYPES MATTER FOR OPERATIONS")
print("="*80)

print("\n[Operation 1: Numeric addition]")
numeric_col = df['Price'].values[:3]
print(f"df['Price'] (float64): {numeric_col}")
print(f"Sum of prices: {numeric_col.sum():.2f}")
print("SUCCESS: float64 supports addition")

print("\n[Operation 2: String concatenation]")
string_col = df['ProductName'].values[:2]
print(f"df['ProductName'] (object): {string_col}")
print(f"Concatenated: {' + '.join(string_col)}")
print("SUCCESS: object (string) supports concatenation")

print("\n[Operation 3: Boolean filtering]")
bool_col = df['InStock']
print(f"df['InStock'] (bool): {bool_col.values}")
in_stock_count = bool_col.sum()
print(f"Items in stock: {in_stock_count}")
print("SUCCESS: bool supports & (and) and | (or)")

print("\n[What goes WRONG: Type mismatch]")
print("If a numeric column is loaded as object (string):")
print("")

# Create problem data
problem_csv = """ID,Amount
1,100.50
2,200.75
3,three hundred
4,400.00"""

problem_file = 'problem_types.csv'
with open(problem_file, 'w') as f:
    f.write(problem_csv)

df_problem = pd.read_csv(problem_file)
print("CSV content with mixed values:")
print(problem_csv)
print("")
print("After loading:")
print(f"Amount dtype: {df_problem['Amount'].dtype}")
print(f"Amount values: {df_problem['Amount'].values}")
print("")

print("Attempting to sum:")
print("df['Amount'].sum() would FAIL with:")
print("TypeError: unsupported operand type(s) for +: 'float' and 'str'")
print("")

try:
    result = df_problem['Amount'].sum()
    print(f"Result: {result}")
except TypeError as e:
    print(f"ERROR (as expected): {str(e)[:70]}...")

print("")
print("Why? Because 'three hundred' is a string, not a number")

"""
================================================================================
MILESTONE 7: INSPECTING AND VERIFYING COLUMN TYPES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 7: INSPECTING AND VERIFYING COLUMN TYPES")
print("="*80)

print("\n[Method 1: df.dtypes (view all)]")
print(df.dtypes)

print("\n[Method 2: df.dtypes[column_name] (specific)]")
print(f"df.dtypes['Price']: {df.dtypes['Price']}")

print("\n[Method 3: df[column].dtype (alternative)]")
print(f"df['Price'].dtype: {df['Price'].dtype}")

print("\n[Method 4: df.info() (comprehensive view)]")
df.info()

print("\n[Method 5: select_dtypes() (filter by type)]")
print("Get all numeric columns:")
numeric_df = df.select_dtypes(include=['int64', 'float64'])
print(f"Numeric columns: {numeric_df.columns.tolist()}")

print("\nGet all object (string) columns:")
string_df = df.select_dtypes(include=['object'])
print(f"String columns: {string_df.columns.tolist()}")

print("\nGet all bool columns:")
bool_df = df.select_dtypes(include=['bool'])
print(f"Boolean columns: {bool_df.columns.tolist()}")

print("\n[Verification checklist]")
print("For each column, ask:")
print("  Type = what I expect? (int, float, object, bool)")
print("  If numeric, is it int64 or float64?")
print("  If object, should it be datetime64?")
print("  If object, should it be numeric (loaded wrong)?")

"""
================================================================================
MILESTONE 8: THE SCENARIO - TYPE MISMATCH ERRORS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 8: THE SCENARIO - TYPE MISMATCH ERRORS")
print("="*80)

print("\n[SCENARIO: Numeric operation fails due to type]")
print("""
You attempt to perform a numeric operation on a column
and encounter an error because the column is stored as
a string (object) instead of a number.

How could inspecting data types earlier have prevented this?
What signals would you look for?
""")

print("\n[Real-world example]")
print("CSV file with sales data:")
sales_csv = """Date,Amount,Region
2024-01-01,1000.50,North
2024-01-02,1500.75,South
2024-01-03,Unknown,East
2024-01-04,2000.00,West"""

print(sales_csv)

sales_file = 'sales_types.csv'
with open(sales_file, 'w') as f:
    f.write(sales_csv)

df_sales = pd.read_csv(sales_file)
print("\nAfter loading:")
print(df_sales)
print("\nData types:")
print(df_sales.dtypes)

print("\n[The problem appears]")
print("Attempting df['Amount'].mean()...")
try:
    mean_amount = df_sales['Amount'].mean()
    print(f"Result: {mean_amount}")
except TypeError as e:
    print(f"ERROR: {str(e)[:80]}...")

print("\n[How inspection would have caught this]")
print("Step 1: After loading, check df.dtypes")
print(f"  See: Amount dtype = {df_sales['Amount'].dtype}")
print(f"  Expected: Amount dtype = float64")
print("  RED FLAG: Mismatch!")

print("\nStep 2: Check df.head() to see values")
print(f"  See 'Unknown' in Amount column")
print("  Non-numeric value detected!")

print("\nStep 3: Open CSV file directly")
print("  Identify row with 'Unknown' value")
print("  Verify if this is real data or entry error")

print("\n[Prevention strategy]")
print("DO THIS AFTER EVERY CSV LOAD:")
print("1. df.dtypes -> Check all types match expectations")
print("2. df.head() -> See actual values")
print("3. If type mismatch -> Open CSV file")
print("4. Fix before proceeding with analysis")

print("\n[The preventive workflow]")
print("""
Load CSV
  |
  V
Check dtypes
  |
  ├-> All correct? -> Proceed to analysis
  |
  ├-> Mismatch? -> Open CSV file
  |
  ├-> Fix issue
  |
  V
Reload CSV (with corrections or proper dtype params)
  |
  V
Verify dtypes again
  |
  V
Safe to analyze
""")

"""
================================================================================
MILESTONE 9: PREVENTION STRATEGIES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 9: PREVENTION STRATEGIES")
print("="*80)

print("\n[Strategy 1: Specify dtypes at load time]")
print("Instead of guessing, tell Pandas what types to expect:")
print("""
df = pd.read_csv('file.csv', dtype={
    'Amount': 'float64',
    'Date': 'str',
    'Region': 'str'
})
""")
print("If Amount contains non-numeric, error occurs at load time")
print("You discover and fix the issue immediately")

print("\n[Strategy 2: Inspect immediately after loading]")
print("After EVERY CSV load:")
print("  1. df.dtypes -> Check types")
print("  2. df.head() -> See first rows")
print("  3. df.describe() -> Check statistics")
print("Only proceed if types match expectations")

print("\n[Strategy 3: Use data validation]")
print("After loading, verify assumptions:")
print(f"""
# For numeric columns, verify they're actually numeric
assert df['Amount'].dtype in ['int64', 'float64'], 'Amount should be numeric'
# For string columns, verify they're object or str
assert df['Region'].dtype in ['object', 'str'], 'Region should be string'
""")
print("If assertion fails, error appears before analysis")

print("\n[Strategy 4: Document your expectations]")
print("Before loading, write down expected types:")
print("""
# Expected types for sales.csv:
# - Date: str (to parse later if needed)
# - Amount: float64 (sum, mean, analysis)
# - Region: object (categories)
# - Quantity: int64 (count)

df = pd.read_csv('sales.csv')
df.dtypes  # Verify matches expectations
""")

print("\n[Strategy 5: Use parse_dates for dates]")
print("For date columns, let Pandas parse them:")
print("""
df = pd.read_csv('file.csv', parse_dates=['Date'])
# Now Date column is datetime64, not object
# Can do date arithmetic
""")

"""
================================================================================
MILESTONE 10: COMMON DATA TYPE ISSUES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 10: COMMON DATA TYPE ISSUES")
print("="*80)

print("\n[Issue 1: Numeric loaded as object (most common)]")
print("Cause: Non-numeric values mixed in (like 'Unknown', 'N/A')")
print("Signal in dtypes: -2500 is object instead of int64/float64")
print("Fix: Clean the data or use dtype={'column': 'float64'}")

print("\n[Issue 2: Date loaded as object]")
print("Cause: Not parsed as date during load")
print("Signal: 2024-01-15 shows as object, not datetime64")
print("Fix: Use parse_dates=['DateColumn'] during load")

print("\n[Issue 3: Boolean loaded as int or object]")
print("Cause: CSV doesn't have native bool representation")
print("Signal: True/False shows as 1/0 (int64) or 'True'/'False' (object)")
print("Fix: Use dtype={'column': 'bool'} or manually convert")

print("\n[Issue 4: Integer loaded as float]")
print("Cause: Even one missing value forces entire column to float")
print("Signal: ID column shows float64 instead of int64")
print("Fix: Check for NaN, decide on missing value strategy")

print("\n[Issue 5: Categorical as object]")
print("Cause: Not specified as category during load")
print("Signal: Column with few unique values is object (wastes memory)")
print("Fix: Use dtype={'column': 'category'}")

print("\n[Issue 6: ID columns treated as numeric]")
print("Cause: Leading zeros lost (001 becomes 1)")
print("Signal: Student ID '001001' becomes '1001'")
print("Fix: Use dtype={'StudentID': 'str'} to preserve leading zeros")

"""
================================================================================
MILESTONE 11: BEST PRACTICES FOR STRUCTURE UNDERSTANDING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 11: BEST PRACTICES FOR STRUCTURE UNDERSTANDING")
print("="*80)

print("\n[Best Practice 1: Always check shape first]")
print("After loading any DataFrame:")
print("  print(df.shape)")
print("  'How many records do I have? How many variables?'")
print("  This is your first question")

print("\n[Best Practice 2: Always inspect dtypes]")
print("After shape, check types:")
print("  print(df.dtypes)")
print("  'Does each column have the right type?'")
print("  This is your second question")

print("\n[Best Practice 3: Make it automatic]")
print("Create a function and use it every time:")
print("""
def check_structure(df, name='DataFrame'):
    rows, cols = df.shape
    print(f'{name} has {rows} rows and {cols} columns')
    print('Column types:')
    print(df.dtypes)
    print(f'Total cells: {rows * cols}')
    return df.shape

check_structure(df, 'Products')
""")

print("\n[Best Practice 4: Document expected structure]")
print("Before loading, remember:")
print("  'This dataset should have ~1000 rows'")
print("  'Price should be float64, Category should be object'")
print("  After loading, verify this")

print("\n[Best Practice 5: Use select_dtypes() to explore]")
print("Group columns by type:")
print("  numeric = df.select_dtypes(include='number')")
print("  strings = df.select_dtypes(include='object')")
print("  dates = df.select_dtypes(include='datetime64')")

print("\n[Best Practice 6: Verify before operations]")
print("Before doing analysis on a column:")
print("  if df['Amount'].dtype not in ['int64', 'float64']:")
print("      print('ERROR: Amount is not numeric!')")
print("      return")
print("  result = df['Amount'].sum()")

print("\n[Best Practice 7: Keep a structure reference]")
print("Save expected structure:")
print("""
expected_shape = (1000, 15)
expected_types = {
    'ID': 'int64',
    'Name': 'object',
    'Amount': 'float64'
}

# After loading, verify
assert df.shape == expected_shape
for col, dtype in expected_types.items():
    assert df[col].dtype == dtype
""")

print("\n[Best Practice 8: Use dtype parameter at load]")
print("Be explicit rather than hoping Pandas guesses right:")
print("""
df = pd.read_csv('data.csv', dtype={
    'ID': 'int64',
    'Name': 'str',
    'Price': 'float64',
    'Active': 'bool'
})
""")

print("\n[Best Practice 9: Handle type conversion carefully]")
print("If you need to change type:")
print("  df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')")
print("  This converts 'Unknown' to NaN (safer than error)")

print("\n[Best Practice 10: Never assume]")
print("Always verify structure:")
print("  Never assume types match your expectations")
print("  Always run df.dtypes after loading")
print("  Always compare with what you expected")
print("  If mismatch, investigate before proceeding")

print("\n" + "="*80)
print("MILESTONE 18 SUMMARY")
print("="*80)
print("""
Understanding DataFrame shape and types is foundational:

1. SHAPE - Understanding dataset size
   ├─ df.shape returns (rows, columns)
   ├─ Rows = individual records/observations
   ├─ Columns = attributes/features/variables
   └─ Critical for knowing data volume

2. DTYPES - Understanding column compatibility
   ├─ df.dtypes shows type of each column
   ├─ int64, float64 for numeric (can do math)
   ├─ object for strings (text operations)
   ├─ bool for True/False (logical operations)
   ├─ datetime64 for dates (date arithmetic)
   └─ Type determines valid operations

3. WHY IT MATTERS
   ├─ Wrong types cause operation failures
   ├─ Type mismatch silently corrupts analysis
   ├─ Prevention: Check types immediately after load
   ├─ Early detection saves hours of debugging
   └─ Professional standard: ALWAYS verify structure

4. PREVENTION WORKFLOW
   ├─ Load CSV
   ├─ Check df.shape
   ├─ Check df.dtypes
   ├─ Compare with expectations
   ├─ If mismatch -> Investigate before proceeding
   └─ Only proceed when confident structure is correct

5. THE SCENARIO (THE CRITICAL LESSON)
   Numeric operation fails due to type mismatch:
   ├─ Column loaded as object (string) instead of float64
   ├─ df['Amount'].sum() fails with TypeError
   ├─ But THIS WAS PREVENTABLE with inspecting dtypes first
   ├─ Early inspection saves hours of debugging
   ├─ Make it automatic: Always check structure first
   └─ 30 seconds of inspection vs hours of debugging

6. COMMON ERRORS TO AVOID
   ├─ Numeric as object (most common)
   ├─ Dates as object (not parsed)
   ├─ IDs as numeric (leading zeros lost)
   ├─ Booleans as int (True->1, False->0)
   └─ Categoricals as object (memory waste)

7. BEST PRACTICES (GOLDEN RULES)
   ├─ ALWAYS check shape after load
   ├─ ALWAYS check dtypes after load
   ├─ NEVER skip inspection
   ├─ ALWAYS specify dtypes at load if possible
   ├─ ALWAYS compare with expectations
   ├─ ALWAYS fix issues before analysis
   └─ Make it AUTOMATIC, not optional

Professional Standard:
Shape and type inspection takes ~30 seconds.
Problems caught here would take 30+ hours to debug later.
This is not optional—it's foundational to data work.
""")

print("="*80)
print("END OF MILESTONE 18")
print("="*80)

# Clean up
for file in [csv_file, problem_file, sales_file]:
    if os.path.exists(file):
        os.remove(file)

print("\nCleaned up temporary CSV files")
