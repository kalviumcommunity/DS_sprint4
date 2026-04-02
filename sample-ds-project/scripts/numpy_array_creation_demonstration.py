"""
=====================================================================
MILESTONE 9: CREATING NUMPY ARRAYS FROM PYTHON LISTS
=====================================================================

This script demonstrates:
1. NumPy import and conventions
2. Creating 1D NumPy arrays from lists
3. Creating 2D NumPy arrays from nested lists
4. Inspecting array properties (shape, dtype, size)
5. Differences between Python lists and NumPy arrays
6. Basic array operations and element-wise behavior
7. Array indexing and slicing
8. Common array creation patterns
9. Best practices for NumPy array creation

Focus: Understanding array creation and basic structure, not advanced usage.
=====================================================================
"""

# =====================================================================
# SECTION 1: IMPORTING NUMPY AND CONVENTIONS
# =====================================================================

def demonstrate_numpy_import():
    """
    Show how to import NumPy correctly using standard conventions.
    """
    print("\n" + "="*70)
    print("SECTION 1: IMPORTING NUMPY AND CONVENTIONS")
    print("="*70)
    
    print("\n--- Importing NumPy ---")
    print()
    print("Standard import (CORRECT):")
    print("  import numpy as np")
    print()
    
    # Do the import
    import numpy as np
    print("[NumPy successfully imported as 'np']")
    print()
    
    print("Why 'np' as alias?")
    print("  - Convention: all NumPy code uses 'np'")
    print("  - Shorter than typing 'numpy' repeatedly")
    print("  - Makes code immediately recognizable as NumPy code")
    print("  - Other aliases like 'numpy' or 'np2' are wrong and confusing")
    print()
    
    print("Check NumPy version:")
    print(f"  NumPy version: {np.__version__}")
    print()
    
    print("Verify import:")
    print(f"  type(np): {type(np)}")
    print(f"  np.array: {np.array}")
    print()
    
    return np


# =====================================================================
# SECTION 2: CREATING 1D NUMPY ARRAYS FROM LISTS
# =====================================================================

def demonstrate_1d_array_creation(np):
    """
    Show how to create 1D NumPy arrays from Python lists.
    """
    print("\n" + "="*70)
    print("SECTION 2: CREATING 1D NUMPY ARRAYS FROM LISTS")
    print("="*70)
    
    print("\n--- Python List vs NumPy Array ---")
    print()
    
    # Python list
    python_list = [1, 2, 3, 4, 5]
    print("Python list:")
    print(f"  python_list = {python_list}")
    print(f"  type: {type(python_list)}")
    print()
    
    # Convert to NumPy array
    numpy_array = np.array(python_list)
    print("Convert to NumPy array:")
    print(f"  numpy_array = np.array(python_list)")
    print(f"  Result: {numpy_array}")
    print(f"  type: {type(numpy_array)}")
    print()
    
    print("--- Creating 1D Arrays with Different Data ---")
    print()
    
    # Integer array
    print("From integer list:")
    int_array = np.array([10, 20, 30, 40, 50])
    print(f"  int_array = np.array([10, 20, 30, 40, 50])")
    print(f"  Result: {int_array}")
    print(f"  dtype: {int_array.dtype}")
    print()
    
    # Float array
    print("From float list:")
    float_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    print(f"  float_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])")
    print(f"  Result: {float_array}")
    print(f"  dtype: {float_array.dtype}")
    print()
    
    # Mixed numbers (becomes float)
    print("From mixed int/float list:")
    mixed_array = np.array([1, 2.5, 3, 4.5])
    print(f"  mixed_array = np.array([1, 2.5, 3, 4.5])")
    print(f"  Result: {mixed_array}")
    print(f"  dtype: {mixed_array.dtype}  (notice: all converted to float)")
    print()
    
    # String array
    print("From string list:")
    str_array = np.array(['apple', 'banana', 'cherry'])
    print(f"  str_array = np.array(['apple', 'banana', 'cherry'])")
    print(f"  Result: {str_array}")
    print(f"  dtype: {str_array.dtype}")
    print()
    
    print("Key insight:")
    print("  - NumPy automatically detects data type")
    print("  - All elements should be same type for numerical arrays")
    print("  - Mixed numbers become floats (loss of integer precision avoided)")
    
    return numpy_array, int_array, float_array


# =====================================================================
# SECTION 3: CREATING 2D NUMPY ARRAYS FROM NESTED LISTS
# =====================================================================

def demonstrate_2d_array_creation(np):
    """
    Show how to create 2D NumPy arrays from nested lists.
    """
    print("\n" + "="*70)
    print("SECTION 3: CREATING 2D NUMPY ARRAYS FROM NESTED LISTS")
    print("="*70)
    
    print("\n--- Creating a 2D Array ---")
    print()
    
    # Nested list (represents a matrix)
    nested_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Nested list (matrix-like):")
    print(f"  nested_list = {nested_list}")
    print()
    
    # Convert to 2D array
    array_2d = np.array(nested_list)
    print("Convert to 2D NumPy array:")
    print(f"  array_2d = np.array(nested_list)")
    print(f"  Result:")
    print(array_2d)
    print()
    
    print("--- Visualizing 2D Array Structure ---")
    print()
    print("Visual representation:")
    print("     col0  col1  col2")
    print("row0 [  1     2     3  ]")
    print("row1 [  4     5     6  ]")
    print("row2 [  7     8     9  ]")
    print()
    
    print("--- Creating 2D Arrays with Different Shapes ---")
    print()
    
    # 2x4 array
    print("2x4 array (2 rows, 4 columns):")
    array_2x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(f"  array_2x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])")
    print(array_2x4)
    print()
    
    # 4x2 array
    print("4x2 array (4 rows, 2 columns):")
    array_4x2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(f"  array_4x2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])")
    print(array_4x2)
    print()
    
    print("--- Jagged Arrays (Not Recommended) ---")
    print()
    
    # Jagged list (rows of different lengths)
    jagged_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print("Jagged list (rows of different lengths):")
    print(f"  jagged_list = {jagged_list}")
    jagged_array = np.array(jagged_list, dtype=object)
    print(f"  jagged_array = np.array(jagged_list, dtype=object)")
    print(f"  Result: {jagged_array}")
    print(f"  Problem: Not a true 2D array, harder to work with")
    print(f"  Solution: Make all rows same length, or use different data structure")
    print()
    
    return array_2d, array_2x4


# =====================================================================
# SECTION 4: INSPECTING ARRAY PROPERTIES
# =====================================================================

def demonstrate_array_properties(np):
    """
    Show how to inspect array properties like shape, dtype, size.
    """
    print("\n" + "="*70)
    print("SECTION 4: INSPECTING ARRAY PROPERTIES")
    print("="*70)
    
    print("\n--- 1D Array Properties ---")
    print()
    
    array_1d = np.array([10, 20, 30, 40, 50])
    print(f"Array: {array_1d}")
    print()
    
    print("Properties:")
    print(f"  .shape: {array_1d.shape}     (number of elements)")
    print(f"           = (5,) means 5 elements in 1 dimension")
    print()
    
    print(f"  .dtype: {array_1d.dtype}     (data type)")
    print(f"          = integer 64-bit")
    print()
    
    print(f"  .size: {array_1d.size}      (total number of elements)")
    print()
    
    print(f"  .ndim: {array_1d.ndim}       (number of dimensions)")
    print(f"         = 1 (it's a 1D array)")
    print()
    
    print("--- 2D Array Properties ---")
    print()
    
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Array:")
    print(array_2d)
    print()
    
    print("Properties:")
    print(f"  .shape: {array_2d.shape}    (rows, columns)")
    print(f"          = (2, 3) means 2 rows, 3 columns")
    print()
    
    print(f"  .dtype: {array_2d.dtype}     (data type)")
    print()
    
    print(f"  .size: {array_2d.size}      (total number of elements)")
    print(f"         = 2 * 3 = 6 elements")
    print()
    
    print(f"  .ndim: {array_2d.ndim}       (number of dimensions)")
    print(f"         = 2 (it's a 2D array)")
    print()
    
    print("--- Understanding Shape ---")
    print()
    print("shape tells you the size of each dimension:")
    print("  (5,)        = 1D array with 5 elements")
    print("  (3, 4)      = 2D array with 3 rows and 4 columns")
    print("  (2, 3, 4)   = 3D array (matrix of matrices)")
    print()


# =====================================================================
# SECTION 5: PYTHON LISTS VS NUMPY ARRAYS - THE KEY DIFFERENCES
# =====================================================================

def demonstrate_lists_vs_arrays(np):
    """
    Show the critical differences between Python lists and NumPy arrays.
    This is the core of why NumPy matters.
    """
    print("\n" + "="*70)
    print("SECTION 5: PYTHON LISTS VS NUMPY ARRAYS - KEY DIFFERENCES")
    print("="*70)
    
    print("\n--- DIFFERENCE 1: Element-wise Operations ---")
    print()
    
    print("Python list: Add a number to each element")
    python_list = [1, 2, 3, 4, 5]
    print(f"  list = {python_list}")
    print(f"  list + 10")
    try:
        result = python_list + 10
        print(f"  Result: {result}")
    except TypeError as e:
        print(f"  ERROR: {e}")
        print(f"  Can't add number to list directly!")
    print()
    
    print("NumPy array: Add a number to each element")
    numpy_array = np.array([1, 2, 3, 4, 5])
    print(f"  array = {numpy_array}")
    print(f"  array + 10")
    result = numpy_array + 10
    print(f"  Result: {result}")
    print(f"  SUCCESS: Added to each element!")
    print()
    
    print("--- DIFFERENCE 2: Multiply All Elements ---")
    print()
    
    print("Python list: Multiple a list (repetition)")
    python_list = [1, 2, 3]
    print(f"  list = {python_list}")
    print(f"  list * 2")
    result = python_list * 2
    print(f"  Result: {result}")
    print(f"  = Repeated the list, not multiplied elements")
    print()
    
    print("NumPy array: Multiply each element")
    numpy_array = np.array([1, 2, 3])
    print(f"  array = {numpy_array}")
    print(f"  array * 2")
    result = numpy_array * 2
    print(f"  Result: {result}")
    print(f"  = Each element multiplied by 2")
    print()
    
    print("--- DIFFERENCE 3: Element-wise Arithmetic ---")
    print()
    
    print("Python lists: Can't do arithmetic between lists")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"  list1 = {list1}")
    print(f"  list2 = {list2}")
    print(f"  list1 + list2")
    result = list1 + list2
    print(f"  Result: {result}")
    print(f"  = Concatenated, not added element-wise!")
    print()
    
    print("NumPy arrays: Element-wise arithmetic")
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"  arr1 = {arr1}")
    print(f"  arr2 = {arr2}")
    print(f"  arr1 + arr2")
    result = arr1 + arr2
    print(f"  Result: {result}")
    print(f"  = Each element added to corresponding element")
    print()
    
    print("--- DIFFERENCE 4: Data Homogeneity ---")
    print()
    
    print("Python lists: Can mix any types")
    mixed_list = [1, 'hello', 3.14, True, None]
    print(f"  list = {mixed_list}")
    print(f"  types = {[type(x).__name__ for x in mixed_list]}")
    print(f"  This works but makes arithmetic impossible")
    print()
    
    print("NumPy arrays: All same type (for efficiency)")
    print(f"  array = {np.array([1, 2, 3, 4, 5])}")
    print(f"  All integers = can do fast arithmetic operations")
    print(f"  Homogeneity enables efficient computation")
    print()
    
    print("--- Summary: Why NumPy Matters ---")
    print()
    print("Use Python lists for:")
    print("  - Mixed data types (different types)")
    print("  - Unstructured data")
    print("  - Small data that doesn't need arithmetic")
    print()
    print("Use NumPy arrays for:")
    print("  - Numerical data")
    print("  - Matrix/tensor operations")
    print("  - Element-wise arithmetic")
    print("  - Mathematical computing")
    print("  - Large data sets")


# =====================================================================
# SECTION 6: BASIC ARRAY OPERATIONS AND ELEMENT-WISE BEHAVIOR
# =====================================================================

def demonstrate_array_operations(np):
    """
    Show basic arithmetic operations on NumPy arrays.
    """
    print("\n" + "="*70)
    print("SECTION 6: BASIC ARRAY OPERATIONS AND ELEMENT-WISE BEHAVIOR")
    print("="*70)
    
    print("\n--- Basic Arithmetic Operations ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print()
    
    print("Addition:")
    print(f"  arr + 10 = {arr + 10}")
    print()
    
    print("Subtraction:")
    print(f"  arr - 1 = {arr - 1}")
    print()
    
    print("Multiplication:")
    print(f"  arr * 2 = {arr * 2}")
    print()
    
    print("Division:")
    print(f"  arr / 2 = {arr / 2}")
    print()
    
    print("Exponentiation:")
    print(f"  arr ** 2 = {arr ** 2}")
    print()
    
    print("--- Element-wise Operations Between Arrays ---")
    print()
    
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([10, 20, 30, 40])
    print(f"arr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print()
    
    print(f"arr1 + arr2 = {arr1 + arr2}")
    print(f"arr2 - arr1 = {arr2 - arr1}")
    print(f"arr1 * arr2 = {arr1 * arr2}")
    print(f"arr2 / arr1 = {arr2 / arr1}")
    print()
    
    print("Key: Each operation applied element-by-element")
    print("     Position 0: 1 + 10 = 11")
    print("     Position 1: 2 + 20 = 22")
    print("     Position 2: 3 + 30 = 33")
    print("     Position 3: 4 + 40 = 44")
    print()
    
    print("--- 2D Array Operations ---")
    print()
    
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D array:")
    print(array_2d)
    print()
    
    print("Add 100 to every element:")
    print(array_2d + 100)
    print()
    
    print("Multiply every element by 2:")
    print(array_2d * 2)
    print()
    
    print("Element-wise behavior applies to all dimensions!")


# =====================================================================
# SECTION 7: ARRAY INDEXING AND SLICING
# =====================================================================

def demonstrate_array_indexing(np):
    """
    Show how to access elements and slices of arrays.
    """
    print("\n" + "="*70)
    print("SECTION 7: ARRAY INDEXING AND SLICING")
    print("="*70)
    
    print("\n--- 1D Array Indexing ---")
    print()
    
    arr = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr}")
    print(f"       [0] [1] [2] [3] [4]  (indices)")
    print()
    
    print(f"arr[0] = {arr[0]}  (first element)")
    print(f"arr[2] = {arr[2]}  (third element)")
    print(f"arr[4] = {arr[4]}  (last element)")
    print(f"arr[-1] = {arr[-1]}  (last element using negative index)")
    print()
    
    print("--- 1D Array Slicing ---")
    print()
    
    print(f"arr[1:4] = {arr[1:4]}  (elements at indices 1, 2, 3)")
    print(f"arr[0:3] = {arr[0:3]}  (first three elements)")
    print(f"arr[2:] = {arr[2:]}   (from index 2 to end)")
    print(f"arr[:3] = {arr[:3]}   (from start to index 3)")
    print(f"arr[::2] = {arr[::2]}  (every other element)")
    print()
    
    print("--- 2D Array Indexing ---")
    print()
    
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("2D array:")
    print(array_2d)
    print()
    
    print(f"array_2d[0] = {array_2d[0]}  (first row)")
    print(f"array_2d[0, 0] = {array_2d[0, 0]}  (element at row 0, col 0)")
    print(f"array_2d[1, 2] = {array_2d[1, 2]}  (element at row 1, col 2)")
    print(f"array_2d[2, 1] = {array_2d[2, 1]}  (element at row 2, col 1)")
    print()
    
    print("--- 2D Array Slicing ---")
    print()
    
    print("Get first 2 rows:")
    print(array_2d[0:2])
    print()
    
    print("Get first 2 columns:")
    print(array_2d[:, 0:2])
    print()
    
    print("Get middle column:")
    print(array_2d[:, 1])


# =====================================================================
# SECTION 8: COMMON ARRAY CREATION PATTERNS
# =====================================================================

def demonstrate_array_creation_patterns(np):
    """
    Show convenient ways to create special arrays.
    """
    print("\n" + "="*70)
    print("SECTION 8: COMMON ARRAY CREATION PATTERNS")
    print("="*70)
    
    print("\n--- Create Array of Zeros ---")
    print()
    
    print("1D array of zeros:")
    print(f"  np.zeros(5) = {np.zeros(5)}")
    print()
    
    print("2D array of zeros:")
    print(f"  np.zeros((2, 3)) =")
    print(np.zeros((2, 3)))
    print()
    
    print("--- Create Array of Ones ---")
    print()
    
    print("1D array of ones:")
    print(f"  np.ones(5) = {np.ones(5)}")
    print()
    
    print("2D array of ones:")
    print(f"  np.ones((3, 2)) =")
    print(np.ones((3, 2)))
    print()
    
    print("--- Create Array of Sequential Numbers ---")
    print()
    
    print("Using arange (like range, but returns array):")
    print(f"  np.arange(10) = {np.arange(10)}")
    print(f"  np.arange(2, 8) = {np.arange(2, 8)}")
    print(f"  np.arange(0, 10, 2) = {np.arange(0, 10, 2)}")
    print()
    
    print("Using linspace (evenly spaced numbers):")
    print(f"  np.linspace(0, 10, 5) = {np.linspace(0, 10, 5)}")
    print(f"  (5 numbers evenly spaced between 0 and 10)")
    print()
    
    print("--- Specify Data Type ---")
    print()
    
    print("Create array with specific dtype:")
    print(f"  np.array([1, 2, 3], dtype=float) = {np.array([1, 2, 3], dtype=float)}")
    print(f"  np.zeros(5, dtype=int) = {np.zeros(5, dtype=int)}")
    print()


# =====================================================================
# SECTION 9: BEST PRACTICES AND COMMON MISTAKES
# =====================================================================

def demonstrate_best_practices(np):
    """
    Show best practices and common mistakes with NumPy arrays.
    """
    print("\n" + "="*70)
    print("SECTION 9: BEST PRACTICES AND COMMON MISTAKES")
    print("="*70)
    
    print("\n--- BEST PRACTICE 1: Use Standard Import Convention ---")
    print()
    
    print("CORRECT:")
    print("  import numpy as np")
    print()
    print("WRONG (but sometimes seen):")
    print("  import numpy")
    print("  import numpy as numpy")
    print()
    print("WHY: 'np' is the universal convention. Anyone reading your code")
    print("     expects NumPy arrays when they see 'np'.")
    print()
    
    print("--- BEST PRACTICE 2: Understand Element-wise Behavior ---")
    print()
    
    print("UNDERSTAND THIS:")
    arr = np.array([1, 2, 3, 4])
    print(f"  arr = {arr}")
    print(f"  arr + arr = {arr + arr}  (element-wise addition)")
    print(f"  arr * 2 = {arr * 2}      (element-wise multiplication)")
    print()
    print("Confusion point: What about list concatenation?")
    print(f"  [1, 2] + [3, 4] = {[1, 2] + [3, 4]}  (concatenation, not addition)")
    print(f"  np.array([1, 2]) + np.array([3, 4]) = {np.array([1, 2]) + np.array([3, 4])}  (element-wise)")
    print()
    
    print("--- BEST PRACTICE 3: Convert Lists to Arrays Early ---")
    print()
    
    print("GOOD approach:")
    print("  data = [1, 2, 3, 4, 5]")
    print("  arr = np.array(data)  # Convert to array once")
    print("  result = arr * 2      # Then work with array")
    print()
    print("AVOID:")
    print("  data = [1, 2, 3, 4, 5]")
    print("  result = [x * 2 for x in data]  # Using list comprehension")
    print("           ^ This is slow! Use NumPy instead")
    print()
    
    print("--- BEST PRACTICE 4: Check Array Shape and Type ---")
    print()
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Always inspect your array:")
    print(f"  arr.shape = {arr.shape}  (verify dimensions before operating)")
    print(f"  arr.dtype = {arr.dtype}  (verify data type)")
    print(f"  arr.size = {arr.size}   (verify total elements)")
    print()
    
    print("--- COMMON MISTAKE 1: Forgetting to Convert List ---")
    print()
    
    print("WRONG:")
    print("  data = [1, 2, 3, 4]")
    print("  result = data * 2  # Repeats list, doesn't multiply elements")
    print(f"  Result: {[1, 2, 3, 4] * 2}")
    print()
    
    print("CORRECT:")
    print("  data = [1, 2, 3, 4]")
    print("  arr = np.array(data)")
    print("  result = arr * 2  # Multiplies each element")
    arr = np.array([1, 2, 3, 4])
    print(f"  Result: {arr * 2}")
    print()
    
    print("--- COMMON MISTAKE 2: Misunderstanding Shape ---")
    print()
    
    print("Shape (3,) is 1D array with 3 elements:")
    arr_1d = np.array([1, 2, 3])
    print(f"  arr = {arr_1d}")
    print(f"  shape = {arr_1d.shape}")
    print()
    
    print("Shape (3, 1) is 2D array with 3 rows, 1 column:")
    arr_3x1 = np.array([[1], [2], [3]])
    print(f"  arr = {arr_3x1}")
    print(f"  shape = {arr_3x1.shape}")
    print()
    print("These look similar but are different data structures!")


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "MILESTONE 9: CREATING NUMPY ARRAYS FROM PYTHON LISTS".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    # Run demonstrations
    np = demonstrate_numpy_import()
    demonstrate_1d_array_creation(np)
    demonstrate_2d_array_creation(np)
    demonstrate_array_properties(np)
    demonstrate_lists_vs_arrays(np)
    demonstrate_array_operations(np)
    demonstrate_array_indexing(np)
    demonstrate_array_creation_patterns(np)
    demonstrate_best_practices(np)
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Import NumPy as 'np' (universal convention)")
    print("  • Convert Python lists to NumPy arrays using np.array()")
    print("  • NumPy arrays enable element-wise arithmetic operations")
    print("  • Use .shape, .dtype, .size to inspect arrays")
    print("  • NumPy arrays are homogeneous (all same type)")
    print("  • 1D arrays have shape (n,), 2D arrays have shape (rows, cols)")
    print("  • Element-wise operations are much faster than list comprehensions")
    print("  • NumPy is essential for numerical computing in Python")
    print("\n")
