"""
================================================================================
MILESTONE 14: PANDAS SERIES - CREATING FROM LISTS AND ARRAYS
================================================================================

Understanding Pandas Series:
A comprehensive guide to creating Pandas Series from Python lists and NumPy
arrays, understanding their structure, and recognizing how index-based alignment
differs from NumPy's position-based operations.

Milestones covered:
1. Introduction and Pandas Import
2. Creating Series from Python Lists
3. Creating Series from NumPy Arrays
4. Understanding Default Indexing
5. Creating Custom Indices
6. Inspecting Series Structure (values, index, dtype)
7. Series vs NumPy Arrays: Key Differences
8. Index-Based Alignment in Operations
9. Accessing Series Elements
10. Series Attributes and Methods
11. Best Practices for Series Creation

================================================================================
MILESTONE 1: INTRODUCTION AND PANDAS IMPORT
================================================================================
"""

import numpy as np
import pandas as pd

print("="*80)
print("MILESTONE 1: INTRODUCTION AND PANDAS IMPORT")
print("="*80)

print("\n[What is a Pandas Series?]")
print("A Pandas Series is a 1D labeled array that combines:")
print("  1. VALUES: The actual data (like a NumPy array)")
print("  2. INDEX: Labels for each value (unlike NumPy arrays)")
print("")
print("Key difference from NumPy arrays:")
print("  - NumPy array: [10, 20, 30]  → Access by position (0, 1, 2)")
print("  - Pandas Series: labels matter → Access by label OR position")
print("")
print("Why?")
print("  - Labels make operations intuitive and safer")
print("  - Different Series align by labels, not positions")
print("  - Perfect for time series, categorical data, and DataFrames")

print("\n[Checking Pandas Version]")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")

print("\n[Series Import Pattern]")
print("Standard import: import pandas as pd")
print("Create Series: pd.Series(data, index=None)")

"""
================================================================================
MILESTONE 2: CREATING SERIES FROM PYTHON LISTS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 2: CREATING SERIES FROM PYTHON LISTS")
print("="*80)

print("\n[Creating a Series from a simple list]")
simple_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(simple_list)

print(f"Original list: {simple_list}")
print(f"Type: {type(simple_list)}")
print(f"\nCreated Series:")
print(series_from_list)
print(f"\nSeries type: {type(series_from_list)}")

print("\n[Understanding default indexing]")
print("Notice the OUTPUT above:")
print("  - Left column (0, 1, 2, 3, 4): These are the default indices")
print("  - Right column (10, 20, 30, 40, 50): These are the values")
print("When you don't provide an index, Pandas creates 0, 1, 2, ... automatically")

print("\n[Creating Series from different list types]")
int_list = [1, 2, 3, 4, 5]
series_int = pd.Series(int_list)
print(f"Integer list Series:\n{series_int}")

float_list = [1.5, 2.5, 3.5]
series_float = pd.Series(float_list)
print(f"\nFloat list Series:\n{series_float}")

string_list = ['apple', 'banana', 'orange']
series_string = pd.Series(string_list)
print(f"\nString list Series:\n{series_string}")

mixed_list = [1, 'two', 3.0, None]
series_mixed = pd.Series(mixed_list)
print(f"\nMixed types Series (object dtype):\n{series_mixed}")

print("\n[Checking dtype of Series]")
print(f"Integer Series dtype: {series_int.dtype}")
print(f"Float Series dtype: {series_float.dtype}")
print(f"String Series dtype: {series_string.dtype}")
print(f"Mixed Series dtype: {series_mixed.dtype}")

print("\n[Creating empty Series]")
empty_series = pd.Series([])
print(f"Empty Series:\n{empty_series}")
print(f"Empty Series type: {type(empty_series)}")

"""
================================================================================
MILESTONE 3: CREATING SERIES FROM NUMPY ARRAYS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 3: CREATING SERIES FROM NUMPY ARRAYS")
print("="*80)

print("\n[Creating a Series from a NumPy array]")
numpy_array = np.array([100, 200, 300, 400, 500])
series_from_array = pd.Series(numpy_array)

print(f"NumPy array: {numpy_array}")
print(f"Type: {type(numpy_array)}")
print(f"\nCreated Series from array:")
print(series_from_array)

print("\n[Data type preservation]")
print(f"NumPy array dtype: {numpy_array.dtype}")
print(f"Pandas Series dtype: {series_from_array.dtype}")
print("The dtype is preserved when converting from NumPy to Pandas!")

print("\n[Creating Series from different NumPy arrays]")
float_array = np.array([1.1, 2.2, 3.3, 4.4])
series_float_array = pd.Series(float_array)
print(f"Float array Series:\n{series_float_array}")

int_array = np.arange(5, 11)  # [5, 6, 7, 8, 9, 10]
series_range = pd.Series(int_array)
print(f"\nSeries from np.arange():\n{series_range}")

linspace_array = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
series_linspace = pd.Series(linspace_array)
print(f"\nSeries from np.linspace():\n{series_linspace}")

print("\n[Creating Series from 2D array (first row)]")
array_2d = np.array([[10, 20], [30, 40], [50, 60]])
series_from_2d_row = pd.Series(array_2d[0])  # First row
print(f"2D array first row: {array_2d[0]}")
print(f"Series from first row:\n{series_from_2d_row}")

print("\n[NumPy-Pandas relationship]")
print("NumPy arrays are often used to create Series efficiently")
print("Reason: NumPy operations are fast, then convert to Series for labels")
prices = np.array([10.5, 20.3, 15.8, 22.1])
prices_series = pd.Series(prices, name="Product Prices")
print(f"Prices:\n{prices_series}")

"""
================================================================================
MILESTONE 4: UNDERSTANDING DEFAULT INDEXING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 4: UNDERSTANDING DEFAULT INDEXING")
print("="*80)

print("\n[Default Index: RangeIndex]")
data = [100, 200, 300]
s = pd.Series(data)
print(f"Series:\n{s}")
print(f"\nIndex type: {type(s.index)}")
print(f"Index values: {s.index.tolist()}")
print(f"Index start: {s.index[0]}, end: {s.index[-1]}")

print("\n[Default index is 0-based]")
print("Always starts at 0, increments by 1")
for i in range(len(s)):
    print(f"  Index {i}: Value {s.iloc[i]}")

print("\n[Relationship: Position vs Label]")
s_default = pd.Series([10, 20, 30, 40])
print(f"Series:\n{s_default}")
print(f"\nAccessing by POSITION (iloc):")
print(f"  s[0] (first element): {s_default.iloc[0]}")
print(f"  s[1] (second element): {s_default.iloc[1]}")
print(f"  s[2] (third element): {s_default.iloc[2]}")

print(f"\nAccessing by LABEL (loc) - since labels=positions in this case:")
print(f"  s.loc[0]: {s_default.loc[0]}")
print(f"  s.loc[1]: {s_default.loc[1]}")

print("\n[Important: With default index, iloc and loc return same values]")
print("But they are NOT the same concept!")
print("  - iloc: INTEGER location (0, 1, 2, ... based on position)")
print("  - loc: LABEL (can be anything, happens to be 0, 1, 2 by default)")

print("\n[Index naming]")
s_named = pd.Series([10, 20, 30], index=[0, 1, 2], name="My Series")
print(f"Series with name:\n{s_named}")
print(f"Series name: {s_named.name}")

"""
================================================================================
MILESTONE 5: CREATING CUSTOM INDICES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 5: CREATING CUSTOM INDICES")
print("="*80)

print("\n[Creating Series with string index]")
temperatures = [20, 22, 19, 21, 23]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temp_series = pd.Series(temperatures, index=days)

print(f"Temperatures:\n{temp_series}")
print(f"\nNow you access by day name, not position!")
print(f"  Temperature on Monday: {temp_series['Monday']}")
print(f"  Temperature on Wednesday: {temp_series['Wednesday']}")

print("\n[Creating Series with numeric custom index]")
scores = [85, 90, 78, 92, 88]
student_ids = [101, 102, 103, 104, 105]
score_series = pd.Series(scores, index=student_ids)

print(f"Student scores:\n{score_series}")
print(f"\nAccessing by student ID:")
print(f"  Student 101 score: {score_series[101]}")
print(f"  Student 104 score: {score_series[104]}")

print("\n[Creating Series with mixed-type index]")
months = [1, 2, 3, 4]
month_names = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1200, 1100, 1300]
sales_series = pd.Series(sales, index=month_names)

print(f"Monthly sales:\n{sales_series}")
print(f"March sales: {sales_series['Mar']}")

print("\n[Index length must match data length]")
try:
    bad_series = pd.Series([1, 2, 3], index=['a', 'b'])  # 3 values, 2 labels
except ValueError as e:
    print(f"ERROR: {e}")
    print("The index must have same length as data!")

print("\n[Benefits of custom indexing]")
print("1. Meaningful access: scores['Alice'] instead of scores[0]")
print("2. Safer operations: Alignment by label prevents position mismatches")
print("3. Self-documenting: Code intention is clear")
print("4. Time series: Use dates as index")

print("\n[Custom index from range]")
prices = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
product_series = pd.Series(prices, index=np.arange(1001, 1006))
print(f"Products with IDs:\n{product_series}")

"""
================================================================================
MILESTONE 6: INSPECTING SERIES STRUCTURE
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 6: INSPECTING SERIES STRUCTURE")
print("="*80)

data = [10, 20, 30, 40, 50]
labels = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=labels)

print(f"Series:\n{s}")

print("\n[Accessing values]")
print(f"s.values: {s.values}")
print(f"Type of s.values: {type(s.values)}")
print(f"Note: .values returns a NumPy array!")

print("\n[Accessing index]")
print(f"s.index: {s.index}")
print(f"Type of s.index: {type(s.index)}")
print(f"Index as list: {s.index.tolist()}")

print("\n[Series shape and size]")
print(f"Series shape: {s.shape}")
print(f"Series size: {s.size}")
print(f"Series length: {len(s)}")
print("Note: 1D Series has shape (n,), where n is the number of elements")

print("\n[Data type information]")
print(f"s.dtype: {s.dtype}")
print(f"s.dtypes: {s.dtypes}")

print("\n[Series info()]")
print("While df.info() is common for DataFrames, Series uses describe():")
print(f"s.describe():\n{s.describe()}")

print("\n[Basic statistics]")
print(f"s.mean(): {s.mean()}")
print(f"s.sum(): {s.sum()}")
print(f"s.min(): {s.min()}")
print(f"s.max(): {s.max()}")
print(f"s.std(): {s.std()}")

print("\n[Checking for NaN/None]")
s_with_nan = pd.Series([10, np.nan, 30, None, 50])
print(f"Series with NaN:\n{s_with_nan}")
print(f"s.isna():\n{s_with_nan.isna()}")
print(f"Number of NaN values: {s_with_nan.isna().sum()}")

print("\n[First and last elements]")
print(f"s.head(): {s.head().to_list()}")  # Default: first 5
print(f"s.head(2): {s.head(2).to_list()}")
print(f"s.tail(): {s.tail().to_list()}")  # Default: last 5
print(f"s.tail(2): {s.tail(2).to_list()}")

"""
================================================================================
MILESTONE 7: SERIES VS NUMPY ARRAYS - KEY DIFFERENCES
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 7: SERIES VS NUMPY ARRAYS - KEY DIFFERENCES")
print("="*80)

print("\n[Comparison: NumPy vs Pandas]")
print("┌─────────────────┬──────────────────┬──────────────────┐")
print("│ Feature         │ NumPy Array      │ Pandas Series    │")
print("├─────────────────┼──────────────────┼──────────────────┤")
print("│ Index           │ Position-based   │ Label-based      │")
print("│                 │ (0, 1, 2, ...)   │ (customizable)   │")
print("├─────────────────┼──────────────────┼──────────────────┤")
print("│ Access          │ arr[0] → 1st     │ s['label'] → ok  │")
print("│                 │ Position only    │ s[0] also works  │")
print("├─────────────────┼──────────────────┼──────────────────┤")
print("│ Alignment       │ By position      │ By label         │")
print("├─────────────────┼──────────────────┼──────────────────┤")
print("│ Operations      │ Element-wise     │ Label-aware      │")
print("├─────────────────┼──────────────────┼──────────────────┤")
print("│ Size           │ Fixed at creation│ Fixed at creation│")
print("└─────────────────┴──────────────────┴──────────────────┘")

print("\n[Example 1: Simple Difference]")
np_arr = np.array([10, 20, 30])
pd_ser = pd.Series([10, 20, 30])

print(f"NumPy array: {np_arr}")
print(f"Access by position: arr[0] = {np_arr[0]}")

print(f"\nPandas Series:\n{pd_ser}")
print(f"Access by label: series[0] = {pd_ser[0]} (label happens to be 0)")

print("\n[Example 2: Custom Index Shows the Difference]")
np_arr = np.array([10, 20, 30])
pd_ser = pd.Series([10, 20, 30], index=['x', 'y', 'z'])

print(f"NumPy array: {np_arr}")
print(f"  Access arr[0] = {np_arr[0]} (1st element)")
print(f"  NO way to access by label 'x'!")

print(f"\nPandas Series with custom index:\n{pd_ser}")
print(f"  Access series[0] = {pd_ser.iloc[0]} (using iloc for position 0)")
print(f"  Access series['x'] = {pd_ser['x']} (using label 'x')")
print(f"  Both refer to the same element, but different methods!")

print("\n[Example 3: Why This Matters - Operations]")
print("If you have misaligned data:")
print("")
np_arr1 = np.array([10, 20, 30])
np_arr2 = np.array([1, 100, 3])
result_np = np_arr1 + np_arr2
print(f"NumPy (position-based):")
print(f"  [10, 20, 30] + [1, 100, 3] = {result_np}")
print(f"  Result at position 1: 20 + 100 = 120 (always position 1)")

print(f"\nPandas (label-based):")
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 100, 3], index=['a', 'c', 'b'])  # Different order!
result_pd = s1 + s2
print(f"  Series 1: {s1.to_dict()}")
print(f"  Series 2: {s2.to_dict()}")
print(f"  Result:\n{result_pd}")
print(f"  Result at label 'b': 20 + 3 = 23 (combines matching labels!)")

"""
================================================================================
MILESTONE 8: INDEX-BASED ALIGNMENT IN OPERATIONS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 8: INDEX-BASED ALIGNMENT IN OPERATIONS")
print("="*80)

print("\n[The Key Difference: Index Alignment]")
print("When you add two Pandas Series, Pandas automatically aligns by index!")

print("\n[Example 1: Aligned indices - straightforward]")
s1 = pd.Series([10, 20, 30], index=['apple', 'banana', 'cherry'])
s2 = pd.Series([1, 2, 3], index=['apple', 'banana', 'cherry'])

print(f"Series 1: {s1.to_dict()}")
print(f"Series 2: {s2.to_dict()}")
print(f"Series 1 + Series 2:")
result = s1 + s2
print(result)
print("Result is straightforward: matching indices are added")

print("\n[Example 2: Same data, different order]")
s1 = pd.Series([10, 20, 30], index=['apple', 'banana', 'cherry'])
s2 = pd.Series([3, 2, 1], index=['cherry', 'banana', 'apple'])

print(f"Series 1: {s1.to_dict()}")
print(f"Series 2: {s2.to_dict()}")
print(f"Series 1 + Series 2:")
result = s1 + s2
print(result)
print("Notice: Result is [31, 22, 13] NOT [13, 22, 31]")
print("Why? Pandas aligns 'apple' with 'apple', 'banana' with 'banana', etc.")

print("\n[Example 3: Partially overlapping indices]")
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([100, 200], index=['b', 'c'])

print(f"Series 1: {s1.to_dict()}")
print(f"Series 2: {s2.to_dict()}")
print(f"Series 1 + Series 2:")
result = s1 + s2
print(result)
print("Result has NaN for 'a' (only in s1) and 'c' (only in s2)")
print("Only 'b' has a value (20 + 100 = 120)")

print("\n[Example 4: No overlapping indices]")
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([100, 200], index=['c', 'd'])

print(f"Series 1: {s1.to_dict()}")
print(f"Series 2: {s2.to_dict()}")
print(f"Series 1 + Series 2:")
result = s1 + s2
print(result)
print("Result is all NaN because no indices match!")

print("\n[Why This Matters (The Scenario)]")
print("""
SCENARIO: You perform an operation on two Series and get unexpected results.

Example:
  Sales for Monday-Wednesday: [100, 150, 120]
  Sales for Tuesday-Thursday: [160, 130, 110]
  
If you add these without thinking about index alignment:
  Series 1: Mon=100, Tue=150, Wed=120
  Series 2: Tue=160, Wed=130, Thu=110
  
Expected by a NumPy user: [100+160, 150+130, 120+110] = [260, 280, 230]
Actual result: Mon=NaN, Tue=310, Wed=250, Thu=NaN

Because Pandas aligns by LABEL (day name), not POSITION!

KEY INSIGHT: This is why understanding index matters in Pandas!
""")

"""
================================================================================
MILESTONE 9: ACCESSING SERIES ELEMENTS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 9: ACCESSING SERIES ELEMENTS")
print("="*80)

s = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])

print(f"Series:\n{s}\n")

print("\n[Accessing by label]")
print(f"s['a'] = {s['a']}")
print(f"s['c'] = {s['c']}")
print(f"s['e'] = {s['e']}")

print("\n[Accessing by integer position with iloc]")
print(f"s.iloc[0] = {s.iloc[0]} (first element)")
print(f"s.iloc[2] = {s.iloc[2]} (third element)")
print(f"s.iloc[-1] = {s.iloc[-1]} (last element)")

print("\n[Accessing by label with loc]")
print(f"s.loc['a'] = {s.loc['a']}")
print(f"s.loc['c'] = {s.loc['c']}")

print("\n[Key Difference: s[0] vs s.iloc[0] vs s.loc[0]]")
s_numeric_index = pd.Series([10, 20, 30], index=[10, 20, 30])
print(f"Series with numeric index [10, 20, 30]:\n{s_numeric_index}")

try:
    # This is ambiguous! Does [0] mean label 0 or position 0?
    result = s_numeric_index[0]
    print(f"s[0] = {result}")
except KeyError:
    print(f"s[0] raises KeyError (label 0 doesn't exist, position 0 would be s.iloc[0])")

print(f"s.iloc[0] = {s_numeric_index.iloc[0]} (position 0, value10)")
print(f"s.loc[10] = {s_numeric_index.loc[10]} (label 10, value 10)")

print("\n[Slicing a Series]")
print(f"s['a':'c'] (by label, inclusive on both ends):\n{s['a':'c']}")
print(f"s.iloc[0:3] (by position, exclusive on end):\n{s.iloc[0:3]}")

print("\n[Getting multiple elements]")
print(f"s[['a', 'c', 'e']] (multiple labels):\n{s[['a', 'c', 'e']]}")
print(f"s.iloc[[0, 2, 4]] (multiple positions):\n{s.iloc[[0, 2, 4]]}")

print("\n[Filtering with boolean indexing]")
s_numeric = pd.Series([10, 20, 30, 40, 50])
mask = s_numeric > 25
print(f"Series: {s_numeric.to_list()}")
print(f"Mask (> 25): {mask.to_list()}")
print(f"s[s > 25]:\n{s_numeric[mask]}")

"""
================================================================================
MILESTONE 10: SERIES ATTRIBUTES AND METHODS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 10: SERIES ATTRIBUTES AND METHODS")
print("="*80)

s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

print(f"Series: {s.to_dict()}\n")

print("\n[Attributes (properties)]")
print(f"s.index: {s.index.tolist()}")
print(f"s.values: {s.values}")
print(f"s.dtype: {s.dtype}")
print(f"s.size: {s.size}")
print(f"s.shape: {s.shape}")
print(f"s.name: {s.name}")

print("\n[Statistics methods]")
print(f"s.count(): {s.count()} (number of non-NaN values)")
print(f"s.sum(): {s.sum()}")
print(f"s.mean(): {s.mean()}")
print(f"s.median(): {s.median()}")
print(f"s.min(): {s.min()}")
print(f"s.max(): {s.max()}")
print(f"s.std(): {s.std()} (standard deviation)")

print("\n[Unique and value counts]")
s_repeated = pd.Series([1, 2, 2, 3, 3, 3, 4])
print(f"Series: {s_repeated.to_list()}")
print(f"s.unique(): {s_repeated.unique()}")
print(f"s.value_counts():\n{s_repeated.value_counts()}")

print("\n[Sorting]")
s_unsorted = pd.Series([50, 10, 30, 20, 40], index=['e', 'a', 'c', 'b', 'd'])
print(f"Original:\n{s_unsorted}")
print(f"s.sort_values():\n{s_unsorted.sort_values()}")
print(f"s.sort_index():\n{s_unsorted.sort_index()}")

print("\n[String operations (for string dtype)]")
s_strings = pd.Series(['apple', 'banana', 'cherry'])
print(f"Series: {s_strings.to_list()}")
print(f"s.str.upper():\n{s_strings.str.upper()}")
print(f"s.str.len():\n{s_strings.str.len()}")

print("\n[Resetting index]")
s_labeled = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(f"Original:\n{s_labeled}")
print(f"s.reset_index(drop=True):")
print(s_labeled.reset_index(drop=True))

"""
================================================================================
MILESTONE 11: BEST PRACTICES FOR SERIES CREATION
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 11: BEST PRACTICES FOR SERIES CREATION")
print("="*80)

print("\n[Best Practice 1: Use meaningful index labels]")
# DON'T:
bad_series = pd.Series([100, 200, 300])
print(f"❌ Bad: {bad_series.to_dict()}")

# DO:
good_series = pd.Series([100, 200, 300], index=['Jan', 'Feb', 'Mar'])
print(f"✓ Good: {good_series.to_dict()}")

print("\n[Best Practice 2: Always verify index length matches data]")
try:
    # Don't do this:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b'])
except ValueError as e:
    print(f"❌ Error: Index length 2 doesn't match data length 4")

print("\n[Best Practice 3: Be explicit with iloc for position-based access]")
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# Confusing:
print(f"❌ Confusing: s[0] might mean label 0 or position 0")

# Clear:
print(f"✓ Clear: s.iloc[0] for position access = {s.iloc[0]}")
print(f"✓ Clear: s.loc['a'] for label access = {s.loc['a']}")

print("\n[Best Practice 4: Use keepdims for reductions that might broadcast]")
# When reducing dimensions, keep structure for alignment
arr = np.array([[1, 2, 3], [4, 5, 6]])
s_from_array = pd.Series(arr)  # Creates Series of arrays, usually not what you want
print(f"Don't do this - Series from 2D array:\n{s_from_array}")

# Better for 1D:
arr_1d = np.array([1, 2, 3, 4, 5])
s_from_1d = pd.Series(arr_1d)
print(f"\n✓ Good: Series from 1D array:\n{s_from_1d}")

print("\n[Best Practice 5: Specify dtype when appropriate]")
# Let Pandas infer (usually fine):
s1 = pd.Series([1, 2, 3])
print(f"Inferred dtype: {s1.dtype}")

# Explicit (safer for mixed operations):
s2 = pd.Series([1, 2, 3], dtype='float64')
print(f"Explicit dtype: {s2.dtype}")

print("\n[Best Practice 6: Add name when creating Series]")
# Without name:
s_no_name = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(f"Series without name: {s_no_name.name}")

# With name (helpful when part of DataFrame):
s_named = pd.Series([10, 20, 30], index=['a', 'b', 'c'], name='measurements')
print(f"Series with name: {s_named.name}")

print("\n[Best Practice 7: Check for NaN values after operations]")
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([10, 20], index=['b', 'c'])
result = s1 + s2
print(f"s1 + s2:\n{result}")
print(f"NaN mask: {result.isna()}")
print(f"Count non-NaN: {result.count()}")

print("\n[Best Practice 8: Use Series for 1D, DataFrame for 2D and beyond]")
print("Series: 1D labeled data with optional custom index")
print("DataFrame: 2D+ data with labeled rows AND columns")
print("Use the right tool for your data structure!")

print("\n" + "="*80)
print("MILESTONE 14 SUMMARY")
print("="*80)
print("""
Creating Pandas Series enables intuitive, label-aware data manipulation.
Key concepts learned:

1. Series = Values + Index (labels)
   - Values: The actual data (like NumPy arrays)
   - Index: Labels for each value (customizable)

2. Creating Series:
   - From lists: pd.Series([1, 2, 3])
   - From arrays: pd.Series(numpy_array)
   - With custom index: pd.Series(data, index=labels)

3. Operations are INDEX-AWARE:
   - NumPy: Position-based always
   - Pandas: Label-based alignment
   - Different order = Different result!

4. Index alignment is automatic:
   - Series with mismatched indices produce NaN where no match
   - This prevents silent data corruption

5. Access methods:
   - By label: series[label] or series.loc[label]
   - By position: series.iloc[position]
   - Always use iloc for position to avoid ambiguity

6. Best practices:
   - Use meaningful index labels
   - Verify index length matches data
   - Use iloc explicitly for position-based access
   - Check for NaN after operations
   - Use Series for 1D data, DataFrame for 2D+
   
Understanding Series is foundational for all Pandas work!
""")

print("="*80)
print("END OF MILESTONE 14")
print("="*80)
