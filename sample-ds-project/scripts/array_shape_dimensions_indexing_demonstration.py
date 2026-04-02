"""
=====================================================================
MILESTONE 10: UNDERSTANDING ARRAY SHAPE, DIMENSIONS, AND INDEX POSITIONS
=====================================================================

This script demonstrates:
1. Array shape and what it means
2. Number of dimensions (.ndim)
3. Understanding 1D array structure
4. Understanding 2D array structure (rows and columns)
5. Zero-based indexing fundamentals
6. Accessing elements by index position in 1D arrays
7. Accessing elements by index position in 2D arrays
8. Index out of range errors and how to prevent them
9. Safe indexing practices
10. Defensive programming with array inspection

Focus: Understanding array layout and correct element access, not advanced operations.
=====================================================================
"""

import numpy as np


# =====================================================================
# SECTION 1: WHAT IS ARRAY SHAPE?
# =====================================================================

def demonstrate_array_shape():
    """
    Show what shape means and how to interpret it.
    """
    print("\n" + "="*70)
    print("SECTION 1: WHAT IS ARRAY SHAPE?")
    print("="*70)
    
    print("\n--- The Concept of Shape ---")
    print()
    print("Array shape tells us the SIZE of each DIMENSION.")
    print()
    
    print("For a 1D array:")
    print("  shape = (5,)")
    print("  = One dimension with 5 elements")
    print("  = A vector or list")
    print()
    
    print("For a 2D array:")
    print("  shape = (3, 4)")
    print("  = Two dimensions: 3 rows and 4 columns")
    print("  = A matrix")
    print()
    
    print("For a 3D array:")
    print("  shape = (2, 3, 4)")
    print("  = Three dimensions: 2 blocks, 3 rows per block, 4 columns per row")
    print("  = A tensor or cube")
    print()
    
    print("--- Accessing .shape Property ---")
    print()
    
    # 1D array
    arr_1d = np.array([10, 20, 30, 40, 50])
    print("1D array:")
    print(f"  arr_1d = {arr_1d}")
    print(f"  arr_1d.shape = {arr_1d.shape}")
    print(f"  Meaning: 5 elements in 1 dimension")
    print()
    
    # 2D array
    arr_2d = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]])
    print("2D array:")
    print(f"  arr_2d =")
    print(arr_2d)
    print(f"  arr_2d.shape = {arr_2d.shape}")
    print(f"  Meaning: 3 rows, 4 columns")
    print()
    
    print("--- Accessing .ndim Property ---")
    print()
    
    print("Number of dimensions:")
    print(f"  arr_1d.ndim = {arr_1d.ndim}  (1D array)")
    print(f"  arr_2d.ndim = {arr_2d.ndim}  (2D array)")
    print()
    
    print("Key Insight:")
    print("  .shape tells you SIZE, .ndim tells you DIMENSIONS")
    print("  .shape = (3, 4)  ->  .ndim = 2 (it's 2D)")
    print()


# =====================================================================
# SECTION 2: UNDERSTANDING 1D ARRAY STRUCTURE
# =====================================================================

def demonstrate_1d_array_structure():
    """
    Show the structure of 1D arrays and how elements are positioned.
    """
    print("\n" + "="*70)
    print("SECTION 2: UNDERSTANDING 1D ARRAY STRUCTURE")
    print("="*70)
    
    print("\n--- 1D Array Layout ---")
    print()
    
    arr = np.array([100, 200, 300, 400, 500])
    print(f"Array: {arr}")
    print()
    
    print("Visual representation:")
    print("Position:  [0]  [1]  [2]  [3]  [4]")
    print("Element:  [100][200][300][400][500]")
    print()
    print("Shape: (5,) - one dimension with 5 elements")
    print("ndim: 1 - it's a 1D array")
    print()
    
    print("--- Understanding Indexing ---")
    print()
    print("Indexing means 'which element to access'")
    print()
    
    print("Element at index 0:")
    print(f"  arr[0] = {arr[0]}")
    print(f"  (first element)")
    print()
    
    print("Element at index 2:")
    print(f"  arr[2] = {arr[2]}")
    print(f"  (third element)")
    print()
    
    print("Element at index 4:")
    print(f"  arr[4] = {arr[4]}")
    print(f"  (fifth element)")
    print()
    
    print("--- Zero-Based Indexing ---")
    print()
    print("IMPORTANT: Python and NumPy use ZERO-BASED indexing")
    print()
    print("  Index 0 = first element")
    print("  Index 1 = second element")
    print("  Index 2 = third element")
    print("  Index N-1 = last element")
    print()
    print("For an array with 5 elements:")
    print("  Valid indices: 0, 1, 2, 3, 4")
    print("  INVALID: 5 (out of range), -1, 6, 100, etc.")
    print()
    
    print("--- Negative Indexing ---")
    print()
    print("NumPy also allows negative indices (counting from end):")
    print()
    
    print(f"  arr[-1] = {arr[-1]}  (last element)")
    print(f"  arr[-2] = {arr[-2]}  (second to last)")
    print(f"  arr[-5] = {arr[-5]}  (first element)")
    print()
    
    print("But usually, positive indices are clearer:")
    print(f"  arr[4] = {arr[4]}  (clearer than arr[-1])")
    print()


# =====================================================================
# SECTION 3: UNDERSTANDING 2D ARRAY STRUCTURE
# =====================================================================

def demonstrate_2d_array_structure():
    """
    Show the structure of 2D arrays and how rows and columns work.
    """
    print("\n" + "="*70)
    print("SECTION 3: UNDERSTANDING 2D ARRAY STRUCTURE")
    print("="*70)
    
    print("\n--- 2D Array as Rows and Columns ---")
    print()
    
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    
    print("2D array:")
    print(arr)
    print()
    
    print("Grid representation with indices:")
    print("        col 0  col 1  col 2")
    print("row 0 [   1      2      3   ]")
    print("row 1 [   4      5      6   ]")
    print("row 2 [   7      8      9   ]")
    print()
    
    print(f"Shape: {arr.shape}  (3 rows, 3 columns)")
    print(f"ndim: {arr.ndim}  (2 dimensions)")
    print()
    
    print("--- Accessing Elements in 2D Arrays ---")
    print()
    print("Syntax: array[row_index, column_index]")
    print()
    
    print("Element at row 0, column 0:")
    print(f"  arr[0, 0] = {arr[0, 0]}  (first row, first column)")
    print()
    
    print("Element at row 0, column 2:")
    print(f"  arr[0, 2] = {arr[0, 2]}  (first row, third column)")
    print()
    
    print("Element at row 1, column 1:")
    print(f"  arr[1, 1] = {arr[1, 1]}  (second row, second column)")
    print()
    
    print("Element at row 2, column 2:")
    print(f"  arr[2, 2] = {arr[2, 2]}  (third row, third column)")
    print()
    
    print("--- Valid Index Ranges in 2D Arrays ---")
    print()
    print(f"Array shape: {arr.shape}  (3 rows, 3 columns)")
    print()
    print("Valid row indices: 0, 1, 2")
    print("Valid column indices: 0, 1, 2")
    print()
    print("Valid element accesses:")
    print(f"  arr[0, 0] through arr[2, 2]")
    print()
    print("INVALID - row index out of range:")
    print("  arr[3, 0]  [ERROR: row 3 doesn't exist, only 0-2]")
    print("  arr[5, 1]  [ERROR: row 5 doesn't exist]")
    print()
    print("INVALID - column index out of range:")
    print("  arr[0, 3]  [ERROR: column 3 doesn't exist, only 0-2]")
    print("  arr[1, 5]  [ERROR: column 5 doesn't exist]")
    print()


# =====================================================================
# SECTION 4: ACCESSING ELEMENTS SAFELY
# =====================================================================

def demonstrate_safe_access():
    """
    Show how to access elements safely and check bounds.
    """
    print("\n" + "="*70)
    print("SECTION 4: ACCESSING ELEMENTS SAFELY")
    print("="*70)
    
    print("\n--- Understanding Index Ranges ---")
    print()
    
    arr_1d = np.array([10, 20, 30, 40, 50])
    print("1D array:")
    print(f"  arr = {arr_1d}")
    print(f"  shape = {arr_1d.shape}")
    print()
    
    print("To access elements safely in a 1D array with shape (5,):")
    print("  Valid indices: 0, 1, 2, 3, 4")
    print("  Formula: valid indices are 0 through (n-1)")
    print(f"           where n = size = {arr_1d.shape[0]}")
    print()
    
    print("Safe access pattern:")
    print(f"  arr[0] = {arr_1d[0]}  [SAFE]")
    print(f"  arr[2] = {arr_1d[2]}  [SAFE]")
    print(f"  arr[4] = {arr_1d[4]}  [SAFE]")
    print()
    
    print("Both of these FAIL (out of range):")
    print(f"  arr[5]  [ERROR: no element at index 5]")
    print(f"  arr[10]  [ERROR: no element at index 10]")
    print()
    
    print("--- Understanding Row and Column Ranges ---")
    print()
    
    arr_2d = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8]])
    print("2D array:")
    print(arr_2d)
    print(f"Shape: {arr_2d.shape}  (2 rows, 4 columns)")
    print()
    
    print("To access safely:")
    print("  Valid row indices: 0, 1  (0 through shape[0]-1)")
    print("  Valid column indices: 0, 1, 2, 3  (0 through shape[1]-1)")
    print()
    
    print("Safe accesses:")
    print(f"  arr[0, 0] = {arr_2d[0, 0]}  [SAFE]")
    print(f"  arr[0, 3] = {arr_2d[0, 3]}  [SAFE]")
    print(f"  arr[1, 2] = {arr_2d[1, 2]}  [SAFE]")
    print()
    
    print("These FAIL (out of range):")
    print(f"  arr[2, 0]  [ERROR: only rows 0-1 exist]")
    print(f"  arr[0, 4]  [ERROR: only columns 0-3 exist]")
    print(f"  arr[5, 10]  [ERROR: both out of range]")
    print()


# =====================================================================
# SECTION 5: DEFENSIVE PROGRAMMING - CHECKING BEFORE ACCESSING
# =====================================================================

def demonstrate_defensive_programming():
    """
    Show how to check array properties before accessing elements.
    """
    print("\n" + "="*70)
    print("SECTION 5: DEFENSIVE PROGRAMMING - CHECKING BEFORE ACCESSING")
    print("="*70)
    
    print("\n--- Pattern 1: Inspect Array First ---")
    print()
    
    arr = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90],
                    [100, 110, 120]])
    
    print("Best practice: Always inspect array properties first")
    print()
    print("Step 1: Check what you're working with")
    print(f"  arr.shape = {arr.shape}")
    print(f"  arr.ndim = {arr.ndim}")
    print(f"  arr.size = {arr.size}")
    print()
    
    print("Step 2: Plan your access")
    print("  'I have a 4x3 array (4 rows, 3 columns)'")
    print("  'Valid row indices: 0, 1, 2, 3'")
    print("  'Valid column indices: 0, 1, 2'")
    print()
    
    print("Step 3: Access safely")
    print(f"  arr[0, 0] = {arr[0, 0]}  [OK]")
    print(f"  arr[3, 2] = {arr[3, 2]}  [OK]")
    print()
    
    print("--- Pattern 2: Check Dimensions Before Indexing ---")
    print()
    
    print("DEFENSIVE CODE PATTERN:")
    print()
    print("  rows, cols = arr.shape")
    print("  if 0 <= row_index < rows and 0 <= col_index < cols:")
    print("      element = arr[row_index, col_index]")
    print("  else:")
    print("      print('Index out of range')")
    print()
    
    print("Let's apply this:")
    rows, cols = arr.shape
    print(f"  rows = {rows}, cols = {cols}")
    print()
    
    # Safe access
    row_index, col_index = 2, 1
    if 0 <= row_index < rows and 0 <= col_index < cols:
        element = arr[row_index, col_index]
        print(f"  Accessing arr[{row_index}, {col_index}]: {element}  [SUCCESS]")
    else:
        print(f"  ERROR: Index out of range")
    print()
    
    # Unsafe access detected
    row_index, col_index = 5, 1
    if 0 <= row_index < rows and 0 <= col_index < cols:
        element = arr[row_index, col_index]
        print(f"  Accessing arr[{row_index}, {col_index}]: {element}")
    else:
        print(f"  Attempting arr[{row_index}, {col_index}]: INDEX OUT OF RANGE!")
        print(f"  (row {row_index} doesn't exist; only 0-{rows-1})")
    print()


# =====================================================================
# SECTION 6: COMMON INDEXING MISTAKES
# =====================================================================

def demonstrate_common_mistakes():
    """
    Show common indexing errors and how to avoid them.
    """
    print("\n" + "="*70)
    print("SECTION 6: COMMON INDEXING MISTAKES")
    print("="*70)
    
    print("\n--- MISTAKE 1: Forgetting Zero-Based Indexing ---")
    print()
    
    arr = np.array([100, 200, 300, 400, 500])
    print("Array:")
    print(f"  {arr}")
    print("Mistake: Trying to access 'first element' with index 1")
    print(f"  arr[1] = {arr[1]}  [This is SECOND element, not first!]")
    print()
    print("Correct: First element uses index 0")
    print(f"  arr[0] = {arr[0]}  [CORRECT]")
    print()
    
    print("--- MISTAKE 2: Off-By-One Error ---")
    print()
    
    arr = np.array([10, 20, 30, 40])
    print("Array:")
    print(f"  {arr}")
    print(f"  Shape: {arr.shape}")
    print()
    print("Mistake: Trying to access last element")
    print("  arr[4]  [WRONG: shape is (4,), so indices are 0-3]")
    print()
    print("Correct: Last element is at index (size - 1)")
    print(f"  arr[3] = {arr[3]}  [CORRECT - last element]")
    print()
    
    print("--- MISTAKE 3: Confusing Row/Column in 2D Arrays ---")
    print()
    
    arr = np.array([[1, 2, 3],
                    [4, 5, 6]])
    print("2D array:")
    print(arr)
    print()
    print("Syntax for 2D: array[ROW, COLUMN]")
    print()
    print("Mistake: arr[2, 1]  Can't match rows")
    print("  This tries to access row 2, but only rows 0-1 exist!")
    print()
    print("Correct: arr[1, 1]")
    print(f"  arr[1, 1] = {arr[1, 1]}  [row 1, column 1]")
    print()
    
    print("--- MISTAKE 4: Not Checking Shape First ---")
    print()
    
    print("BAD PRACTICE:")
    print("  result = arr[i, j]  # Hope indices are valid")
    print()
    print("GOOD PRACTICE:")
    print("  rows, cols = arr.shape")
    print("  if 0 <= i < rows and 0 <= j < cols:")
    print("      result = arr[i, j]")
    print()


# =====================================================================
# SECTION 7: INTERPRETING SHAPE FOR DIFFERENT ARRAY TYPES
# =====================================================================

def demonstrate_shape_interpretation():
    """
    Show how to interpret shape for various array structures.
    """
    print("\n" + "="*70)
    print("SECTION 7: INTERPRETING SHAPE FOR DIFFERENT ARRAY TYPES")
    print("="*70)
    
    print("\n--- 1D Array ---")
    print()
    
    arr_1d = np.array([1, 2, 3, 4, 5, 6])
    print(f"Array: {arr_1d}")
    print(f"Shape: {arr_1d.shape}")
    print(f"Meaning: {arr_1d.shape[0]} elements arranged in 1 row")
    print(f"Access pattern: arr[i]  where i = 0 to {arr_1d.shape[0]-1}")
    print()
    
    print("--- 2D Array (Matrix) ---")
    print()
    
    arr_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
    print("Array:")
    print(arr_2d)
    print(f"Shape: {arr_2d.shape}")
    rows, cols = arr_2d.shape
    print(f"Meaning: {rows} rows, {cols} columns")
    print(f"Access pattern: arr[i, j]")
    print(f"  i (row) = 0 to {rows-1}")
    print(f"  j (col) = 0 to {cols-1}")
    print()
    
    print("--- Rectangular (Non-Square) 2D Arrays ---")
    print()
    
    tall = np.array([[1],
                     [2],
                     [3],
                     [4],
                     [5]])
    print("Tall array (5 rows, 1 column):")
    print(tall)
    print(f"Shape: {tall.shape}")
    print()
    
    wide = np.array([[1, 2, 3, 4, 5, 6, 7]])
    print("Wide array (1 row, 7 columns):")
    print(wide)
    print(f"Shape: {wide.shape}")
    print()


# =====================================================================
# SECTION 8: RELATIONSHIP BETWEEN SHAPE AND INDEX RANGES
# =====================================================================

def demonstrate_shape_index_relationship():
    """
    Show the exact relationship between shape and valid indices.
    """
    print("\n" + "="*70)
    print("SECTION 8: RELATIONSHIP BETWEEN SHAPE AND INDEX RANGES")
    print("="*70)
    
    print("\n--- The Formula ---")
    print()
    print("For any dimension of size N:")
    print("  Valid indices: 0, 1, 2, ..., N-1")
    print("  INVALID indices: N, N+1, -0, -N-1, etc.")
    print()
    
    print("--- 1D Example ---")
    print()
    
    arr = np.array([100, 200, 300, 400])
    print(f"Array: {arr}")
    print(f"Shape: {arr.shape}")
    print()
    
    size = arr.shape[0]
    print(f"Size (from shape): {size}")
    print(f"Valid indices: 0, 1, 2, 3  (which is 0 to {size-1})")
    print()
    for i in range(size):
        print(f"  arr[{i}] = {arr[i]}")
    print()
    
    print("--- 2D Example ---")
    print()
    
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])
    print("Array:")
    print(arr)
    print()
    print(f"Shape: {arr.shape}")
    rows, cols = arr.shape
    print(f"Rows (from shape[0]): {rows}")
    print(f"Columns (from shape[1]): {cols}")
    print()
    print(f"Valid row indices: 0 to {rows-1}  ({rows} total)")
    print(f"Valid column indices: 0 to {cols-1}  ({cols} total)")
    print()
    
    print("All valid element accesses:")
    for i in range(rows):
        for j in range(cols):
            print(f"  arr[{i},{j}]={arr[i,j]}", end="  ")
        print()
    print()


# =====================================================================
# SECTION 9: INDEX OUT OF RANGE - DEBUGGING
# =====================================================================

def demonstrate_index_errors():
    """
    Show how to understand and debug index out of range errors.
    """
    print("\n" + "="*70)
    print("SECTION 9: INDEX OUT OF RANGE - DEBUGGING")
    print("="*70)
    
    print("\n--- What Causes Index Out of Range? ---")
    print()
    
    arr = np.array([[1, 2, 3],
                    [4, 5, 6]])
    print("Array:")
    print(arr)
    print(f"Shape: {arr.shape}  (2 rows, 3 columns)")
    print()
    
    print("Scenario 1: Row index too large")
    print("  Trying: arr[2, 0]")
    print("  Error: index 2 is out of bounds for axis 0 with size 2")
    print("  Why: rows are indexed 0-1, row 2 doesn't exist")
    print("  Fix: use row indices 0 or 1")
    print()
    
    print("Scenario 2: Column index too large")
    print("  Trying: arr[0, 3]")
    print("  Error: index 3 is out of bounds for axis 1 with size 3")
    print("  Why: columns are indexed 0-2, column 3 doesn't exist")
    print("  Fix: use column indices 0, 1, or 2")
    print()
    
    print("Scenario 3: Both out of bounds")
    print("  Trying: arr[5, 5]")
    print("  Error: index 5 is out of bounds for axis 0 with size 2")
    print("  Why: neither index is valid")
    print("  Fix: check shape first!")
    print()
    
    print("--- How to Debug ---")
    print()
    print("WHEN you get an index error:")
    print("  1. Check arr.shape")
    print("  2. Check which axis (0 = rows, 1 = columns)")
    print("  3. Verify your indices are within valid range")
    print()
    
    print("EXAMPLE:")
    print(f"  Current shape: {arr.shape}")
    print("  You got error about axis 1")
    print("  Solution: make sure second index < 3")
    print()


# =====================================================================
# SECTION 10: BEST PRACTICES FOR SAFE INDEXING
# =====================================================================

def demonstrate_best_practices():
    """
    Show best practices for safe and clear indexing.
    """
    print("\n" + "="*70)
    print("SECTION 10: BEST PRACTICES FOR SAFE INDEXING")
    print("="*70)
    
    print("\n--- BEST PRACTICE 1: Always Check Shape First ---")
    print()
    
    arr = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])
    
    print("GOOD:")
    print("  rows, cols = arr.shape")
    print(f"  # Now you know: rows={arr.shape[0]}, cols={arr.shape[1]}")
    print()
    
    print("BAD:")
    print("  arr[i, j]  # Hope you get the indices right!")
    print()
    
    print("--- BEST PRACTICE 2: Use Bounds Checking ---")
    print()
    
    print("GOOD CODE:")
    print("  if 0 <= row < rows and 0 <= col < cols:")
    print("      value = arr[row, col]")
    print()
    
    print("BAD CODE:")
    print("  value = arr[row, col]  # Crash if out of range")
    print()
    
    print("--- BEST PRACTICE 3: Understand Your Data Structure ---")
    print()
    
    print("Know BEFORE indexing:")
    print("  Is this 1D or 2D?")
    print("  What's the valid range?")
    print("  What does each dimension mean?")
    print()
    
    print("Example with clear variable names:")
    print("  data_array = np.array([[...], [...]])")
    print("  num_samples, num_features = data_array.shape")
    print("  # Now accessing arr[sample_idx, feature_idx] is clear!")
    print()
    
    print("--- BEST PRACTICE 4: Use Meaningful Index Variables ---")
    print()
    
    print("BAD (unclear):")
    print("  for i in range(arr.shape[0]):")
    print("      for j in range(arr.shape[1]):")
    print("          print(arr[i, j])")
    print()
    
    print("GOOD (clear):")
    print("  num_rows, num_cols = arr.shape")
    print("  for row_idx in range(num_rows):")
    print("      for col_idx in range(num_cols):")
    print("          element = arr[row_idx, col_idx]")
    print("          print(element)")
    print()
    
    print("--- BEST PRACTICE 5: Verify Common Cases ---")
    print()
    print("Always test these index accesses:")
    print("  - First element: arr[0, 0]")
    print("  - Last element: arr[rows-1, cols-1]")
    print("  - Middle element: arr[rows//2, cols//2]")
    print()
    
    arr = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])
    rows, cols = arr.shape
    print(f"Test on our array (shape {arr.shape}):")
    print(f"  First: arr[0, 0] = {arr[0, 0]}")
    print(f"  Last: arr[{rows-1}, {cols-1}] = {arr[rows-1, cols-1]}")
    print(f"  Middle: arr[{rows//2}, {cols//2}] = {arr[rows//2, cols//2]}")
    print()


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "MILESTONE 10: ARRAY SHAPE, DIMENSIONS, INDEX POSITIONS".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    # Run demonstrations
    demonstrate_array_shape()
    demonstrate_1d_array_structure()
    demonstrate_2d_array_structure()
    demonstrate_safe_access()
    demonstrate_defensive_programming()
    demonstrate_common_mistakes()
    demonstrate_shape_interpretation()
    demonstrate_shape_index_relationship()
    demonstrate_index_errors()
    demonstrate_best_practices()
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Shape tells you the SIZE of each dimension")
    print("  • 1D array shape (n,) = n elements, index 0 to n-1")
    print("  • 2D array shape (m,n) = m rows, n columns")
    print("  • Always use ZERO-BASED indexing: 0, 1, 2, ..., n-1")
    print("  • For 2D: arr[row, col] where row < rows and col < cols")
    print("  • ALWAYS check shape before accessing elements")
    print("  • Valid indices go from 0 to (dimension_size - 1)")
    print("  • Index out of range errors mean your index >= dimension_size")
    print("  • Use defensive programming: check bounds before accessing")
    print("  • ndim tells you number of dimensions, shape tells you sizes")
    print("\n")
