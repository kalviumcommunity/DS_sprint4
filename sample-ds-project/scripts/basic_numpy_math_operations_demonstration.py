"""
=====================================================================
MILESTONE 11: PERFORMING BASIC MATHEMATICAL OPERATIONS ON NUMPY ARRAYS
=====================================================================

This script demonstrates:
1. Creating numeric NumPy arrays
2. Element-wise addition between arrays
3. Element-wise subtraction between arrays
4. Element-wise multiplication between arrays
5. Element-wise division between arrays
6. Scalar operations (adding scalar to array)
7. Scalar multiplication and division
8. Comparing NumPy math with Python list approaches
9. Array shape compatibility for operations
10. Common mathematical operation errors
11. Best practices for array mathematics

Focus: Element-wise operations and scalar operations, not advanced linear algebra.
=====================================================================
"""

import numpy as np


# =====================================================================
# SECTION 1: CREATING NUMERIC NUMPY ARRAYS FOR MATH
# =====================================================================

def demonstrate_numeric_arrays():
    """
    Show how to create numeric arrays suitable for mathematical operations.
    """
    print("\n" + "="*70)
    print("SECTION 1: CREATING NUMERIC NUMPY ARRAYS FOR MATH")
    print("="*70)
    
    print("\n--- Different Ways to Create Numeric Arrays ---")
    print()
    
    print("From Python lists:")
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"  np.array([1, 2, 3, 4, 5]) = {arr1}")
    print(f"  dtype: {arr1.dtype}")
    print()
    
    print("With float values:")
    arr2 = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    print(f"  np.array([1.5, 2.5, 3.5, 4.5, 5.5]) = {arr2}")
    print(f"  dtype: {arr2.dtype}")
    print()
    
    print("Using arange (like range, but returns array):")
    arr3 = np.arange(10)
    print(f"  np.arange(10) = {arr3}")
    print()
    
    print("Using linspace (evenly spaced values):")
    arr4 = np.linspace(0, 10, 5)
    print(f"  np.linspace(0, 10, 5) = {arr4}")
    print()
    
    print("Using zeros and ones:")
    arr5 = np.zeros(5)
    arr6 = np.ones(5)
    print(f"  np.zeros(5) = {arr5}")
    print(f"  np.ones(5) = {arr6}")
    print()
    
    print("All of these work for mathematical operations!")
    print()


# =====================================================================
# SECTION 2: ELEMENT-WISE ADDITION
# =====================================================================

def demonstrate_addition():
    """
    Show how element-wise addition works on NumPy arrays.
    """
    print("\n" + "="*70)
    print("SECTION 2: ELEMENT-WISE ADDITION")
    print("="*70)
    
    print("\n--- Adding Two Arrays ---")
    print()
    
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    
    print(f"arr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print()
    
    result = arr1 + arr2
    print(f"arr1 + arr2 = {result}")
    print()
    
    print("How it works (element-by-element):")
    print("  Position 0: 1 + 10 = 11")
    print("  Position 1: 2 + 20 = 22")
    print("  Position 2: 3 + 30 = 33")
    print("  Position 3: 4 + 40 = 44")
    print("  Position 4: 5 + 50 = 55")
    print()
    
    print("--- 2D Array Addition ---")
    print()
    
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[10, 20], [30, 40]])
    
    print("matrix1:")
    print(matrix1)
    print()
    print("matrix2:")
    print(matrix2)
    print()
    
    result = matrix1 + matrix2
    print("matrix1 + matrix2:")
    print(result)
    print()


# =====================================================================
# SECTION 3: ELEMENT-WISE SUBTRACTION
# =====================================================================

def demonstrate_subtraction():
    """
    Show how element-wise subtraction works on NumPy arrays.
    """
    print("\n" + "="*70)
    print("SECTION 3: ELEMENT-WISE SUBTRACTION")
    print("="*70)
    
    print("\n--- Subtracting Arrays ---")
    print()
    
    arr1 = np.array([100, 200, 300, 400, 500])
    arr2 = np.array([10, 20, 30, 40, 50])
    
    print(f"arr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print()
    
    result = arr1 - arr2
    print(f"arr1 - arr2 = {result}")
    print()
    
    print("Element-by-element:")
    print("  100 - 10 = 90")
    print("  200 - 20 = 180")
    print("  300 - 30 = 270")
    print("  400 - 40 = 360")
    print("  500 - 50 = 450")
    print()
    
    print("--- Subtracting in Reverse ---")
    print()
    
    result2 = arr2 - arr1
    print(f"arr2 - arr1 = {result2}")
    print()
    print("Notice: Order matters! arr2 - arr1 != arr1 - arr2")
    print()


# =====================================================================
# SECTION 4: ELEMENT-WISE MULTIPLICATION
# =====================================================================

def demonstrate_multiplication():
    """
    Show how element-wise multiplication works on NumPy arrays.
    """
    print("\n" + "="*70)
    print("SECTION 4: ELEMENT-WISE MULTIPLICATION")
    print("="*70)
    
    print("\n--- Multiplying Arrays ---")
    print()
    
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([2, 3, 4, 5, 6])
    
    print(f"arr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print()
    
    result = arr1 * arr2
    print(f"arr1 * arr2 = {result}")
    print()
    
    print("Element-by-element multiplication:")
    print("  1 * 2 = 2")
    print("  2 * 3 = 6")
    print("  3 * 4 = 12")
    print("  4 * 5 = 20")
    print("  5 * 6 = 30")
    print()
    
    print("IMPORTANT: This is NOT matrix multiplication!")
    print("(Matrix multiplication is arr1 @ arr2 or np.dot(arr1, arr2))")
    print("This is element-wise multiplication (also called Hadamard product)")
    print()


# =====================================================================
# SECTION 5: ELEMENT-WISE DIVISION
# =====================================================================

def demonstrate_division():
    """
    Show how element-wise division works on NumPy arrays.
    """
    print("\n" + "="*70)
    print("SECTION 5: ELEMENT-WISE DIVISION")
    print("="*70)
    
    print("\n--- Dividing Arrays ---")
    print()
    
    arr1 = np.array([100.0, 200.0, 300.0, 400.0])
    arr2 = np.array([2.0, 4.0, 5.0, 8.0])
    
    print(f"arr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print()
    
    result = arr1 / arr2
    print(f"arr1 / arr2 = {result}")
    print()
    
    print("Element-by-element division:")
    print("  100 / 2 = 50.0")
    print("  200 / 4 = 50.0")
    print("  300 / 5 = 60.0")
    print("  400 / 8 = 50.0")
    print()
    
    print("--- Integer Division ---")
    print()
    
    arr3 = np.array([10, 20, 30, 40])
    arr4 = np.array([3, 6, 7, 8])
    
    print(f"arr3 = {arr3}")
    print(f"arr4 = {arr4}")
    print()
    
    print("Regular division (returns floats):")
    print(f"  arr3 / arr4 = {arr3 / arr4}")
    print()
    
    print("Integer division (// operator):")
    print(f"  arr3 // arr4 = {arr3 // arr4}")
    print()


# =====================================================================
# SECTION 6: SCALAR OPERATIONS
# =====================================================================

def demonstrate_scalar_operations():
    """
    Show how to apply scalar (single number) operations to arrays.
    """
    print("\n" + "="*70)
    print("SECTION 6: SCALAR OPERATIONS")
    print("="*70)
    
    print("\n--- Adding a Scalar to an Array ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"arr = {arr}")
    print()
    
    result = arr + 10
    print(f"arr + 10 = {result}")
    print("(Adds 10 to EACH element)")
    print()
    
    print("--- Subtracting a Scalar ---")
    print()
    
    result = arr - 1
    print(f"arr - 1 = {result}")
    print()
    
    print("--- Multiplying by a Scalar ---")
    print()
    
    result = arr * 3
    print(f"arr * 3 = {result}")
    print()
    
    print("--- Dividing by a Scalar ---")
    print()
    
    result = arr / 2
    print(f"arr / 2 = {result}")
    print()
    
    print("--- Scalar Operations on 2D Arrays ---")
    print()
    
    matrix = np.array([[1, 2], [3, 4], [5, 6]])
    print("matrix:")
    print(matrix)
    print()
    
    print("matrix + 100:")
    print(matrix + 100)
    print()
    
    print("matrix * 2:")
    print(matrix * 2)
    print()


# =====================================================================
# SECTION 7: COMPARISON: NUMPY VS PYTHON LISTS FOR MATH
# =====================================================================

def demonstrate_numpy_vs_lists():
    """
    Show why NumPy is superior to Python lists for mathematical operations.
    """
    print("\n" + "="*70)
    print("SECTION 7: COMPARISON: NUMPY VS PYTHON LISTS FOR MATH")
    print("="*70)
    
    print("\n--- Python List: Trying to Add a Number ---")
    print()
    
    python_list = [1, 2, 3, 4, 5]
    print(f"python_list = {python_list}")
    print("Trying: python_list + 10")
    try:
        result = python_list + 10
        print(f"Result: {result}")
    except TypeError as e:
        print(f"ERROR: {e}")
        print("(Can't add a number to a list!)")
    print()
    
    print("Python list workaround (clumsy):")
    print("  result = [x + 10 for x in python_list]")
    result = [x + 10 for x in python_list]
    print(f"  Result: {result}")
    print()
    
    print("--- NumPy Array: Element-Wise Operation (Clean) ---")
    print()
    
    numpy_array = np.array([1, 2, 3, 4, 5])
    print(f"numpy_array = {numpy_array}")
    print("Trying: numpy_array + 10")
    result = numpy_array + 10
    print(f"Result: {result}")
    print("(Simple and intuitive!)")
    print()
    
    print("--- Speed Comparison (Conceptual) ---")
    print()
    print("Python list comprehension: Slow for large data")
    print("  - Loop in Python interpretor")
    print("  - Type checking each element")
    print("  - Memory overhead")
    print()
    print("NumPy operation: Fast (uses optimized C code)")
    print("  - Vectorized operation")
    print("  - Homogeneous data types")
    print("  - Single operation on all elements")
    print()
    
    print("For 1 million elements:")
    print("  List comprehension: milliseconds to seconds")
    print("  NumPy operation: microseconds")
    print()


# =====================================================================
# SECTION 8: ARRAY SHAPE COMPATIBILITY FOR OPERATIONS
# =====================================================================

def demonstrate_shape_compatibility():
    """
    Show which array shapes can be operated on together.
    """
    print("\n" + "="*70)
    print("SECTION 8: ARRAY SHAPE COMPATIBILITY FOR OPERATIONS")
    print("="*70)
    
    print("\n--- Same Shape Arrays (Works) ---")
    print()
    
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([10, 20, 30])
    
    print(f"arr1.shape = {arr1.shape}")
    print(f"arr2.shape = {arr2.shape}")
    print()
    
    result = arr1 + arr2
    print(f"arr1 + arr2 = {result}  [SUCCESS]")
    print()
    
    print("--- Different 1D Shapes (ERROR) ---")
    print()
    
    arr3 = np.array([1, 2, 3, 4])
    arr4 = np.array([10, 20, 30])
    
    print(f"arr3.shape = {arr3.shape}")
    print(f"arr4.shape = {arr4.shape}")
    print()
    
    print("Trying: arr3 + arr4")
    try:
        result = arr3 + arr4
        print(f"Result: {result}")
    except ValueError as e:
        print(f"ERROR: {e}")
        print("(Shapes don't match!)")
    print()
    
    print("--- Same 2D Shape (Works) ---")
    print()
    
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[10, 20], [30, 40]])
    
    print(f"matrix1.shape = {matrix1.shape}")
    print(f"matrix2.shape = {matrix2.shape}")
    print()
    
    result = matrix1 + matrix2
    print(f"matrix1 + matrix2 =")
    print(result)
    print("[SUCCESS]")
    print()
    
    print("--- Scalar Operation (Always Works) ---")
    print()
    
    print("Scalar works with ANY array shape:")
    print(f"  arr1 (shape {arr1.shape}) + 100 works fine")
    print(f"  matrix1 (shape {matrix1.shape}) + 100 works fine")
    print()


# =====================================================================
# SECTION 9: EXPONENTIATION AND OTHER OPERATIONS
# =====================================================================

def demonstrate_other_operations():
    """
    Show other mathematical operations beyond basic arithmetic.
    """
    print("\n" + "="*70)
    print("SECTION 9: EXPONENTIATION AND OTHER OPERATIONS")
    print("="*70)
    
    print("\n--- Exponentiation (Power) ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"arr = {arr}")
    print()
    
    result = arr ** 2
    print(f"arr ** 2 = {result}  (square each element)")
    print()
    
    result = arr ** 3
    print(f"arr ** 3 = {result}  (cube each element)")
    print()
    
    print("--- Square Root (using np.sqrt) ---")
    print()
    
    arr2 = np.array([1.0, 4.0, 9.0, 16.0, 25.0])
    print(f"arr2 = {arr2}")
    print()
    
    result = np.sqrt(arr2)
    print(f"np.sqrt(arr2) = {result}")
    print()
    
    print("--- Absolute Value ---")
    print()
    
    arr3 = np.array([-5, -2, 0, 2, 5])
    print(f"arr3 = {arr3}")
    print()
    
    result = np.abs(arr3)
    print(f"np.abs(arr3) = {result}")
    print()


# =====================================================================
# SECTION 10: COMMON MATHEMATICAL OPERATION ERRORS
# =====================================================================

def demonstrate_common_errors():
    """
    Show common mistakes when performing array math.
    """
    print("\n" + "="*70)
    print("SECTION 10: COMMON MATHEMATICAL OPERATION ERRORS")
    print("="*70)
    
    print("\n--- ERROR 1: Shape Mismatch ---")
    print()
    
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([10, 20])
    
    print(f"arr1.shape = {arr1.shape}")
    print(f"arr2.shape = {arr2.shape}")
    print("Trying: arr1 + arr2")
    print()
    
    try:
        result = arr1 + arr2
        print(f"Result: {result}")
    except ValueError as e:
        print(f"ERROR: {str(e)[:60]}...")
        print()
        print("WHY: Can't add arrays with different dimensions!")
        print(f"  arr1 has 3 elements, arr2 has 2 elements")
    print()
    
    print("--- ERROR 2: Mixing 1D and 2D Without Broadcasting ---")
    print()
    
    arr_1d = np.array([1, 2, 3])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(f"arr_1d.shape = {arr_1d.shape}")
    print(f"arr_2d.shape = {arr_2d.shape}")
    print("Trying: arr_1d + arr_2d")
    print()
    
    try:
        result = arr_1d + arr_2d
        print(f"Result:")
        print(result)
        print("(This works due to broadcasting!)")
    except ValueError as e:
        print(f"ERROR: {e}")
    print()
    
    print("--- ERROR 3: Integer Overflow (Rare) ---")
    print()
    
    # Create small integer arrays to avoid overflow in demo
    arr1 = np.array([1000, 2000, 3000], dtype=np.int32)
    arr2 = np.array([2000, 3000, 4000], dtype=np.int32)
    
    print("When multiplying large numbers, be aware of integer overflow")
    print("Consider using float64 for safety:")
    print()
    
    arr1_float = arr1.astype(float)
    arr2_float = arr2.astype(float)
    print(f"arr1_float * arr2_float = {arr1_float * arr2_float}")
    print()


# =====================================================================
# SECTION 11: BEST PRACTICES FOR ARRAY MATHEMATICS
# =====================================================================

def demonstrate_best_practices():
    """
    Show best practices for performing array mathematics safely.
    """
    print("\n" + "="*70)
    print("SECTION 11: BEST PRACTICES FOR ARRAY MATHEMATICS")
    print("="*70)
    
    print("\n--- BEST PRACTICE 1: Always Check Shapes First ---")
    print()
    
    print("GOOD CODE:")
    print("  array1.shape == array2.shape or compatible shapes")
    print("  result = array1 + array2")
    print()
    
    print("BAD CODE:")
    print("  result = array1 + array2  # Hope they match!")
    print()
    
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([10, 20, 30])
    
    if arr1.shape == arr2.shape:
        result = arr1 + arr2
        print(f"Arrays compatible: {result}")
    else:
        print(f"Arrays NOT compatible")
    print()
    
    print("--- BEST PRACTICE 2: Be Explicit About Data Types ---")
    print()
    
    print("GOOD (clear intention):")
    print("  arr_float = np.array([1.0, 2.0, 3.0])  # Float math")
    print("  result = arr_float / 2")
    print()
    
    arr_float = np.array([1.0, 2.0, 3.0])
    print(f"Result: {arr_float / 2}")
    print()
    
    print("BAD (might lose precision):")
    print("  arr_int = np.array([1, 2, 3])")
    print("  result = arr_int / 2  # May lose decimal places")
    print()
    
    arr_int = np.array([1, 2, 3])
    print(f"Result: {arr_int / 2}  (works, but converts to float)")
    print()
    
    print("--- BEST PRACTICE 3: Use NumPy Functions When Available ---")
    print()
    
    print("DON'T write loops for math:")
    print("  for i in range(len(arr)):")
    print("      result[i] = arr[i] ** 2")
    print()
    
    print("DO use NumPy operations:")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  arr ** 2 = {arr ** 2}")
    print()
    
    print("BENEFITS:")
    print("  - Much faster")
    print("  - More readable")
    print("  - Fewer opportunities for bugs")
    print()
    
    print("--- BEST PRACTICE 4: Use Meaningful Variable Names ---")
    print()
    
    print("UNCLEAR:")
    print("  a = np.array([...])")
    print("  b = np.array([...])")
    print("  c = a + b")
    print()
    
    print("CLEAR:")
    print("  temperatures = np.array([...])")
    print("  temperature_offsets = np.array([...])")
    print("  adjusted_temps = temperatures + temperature_offsets")
    print()
    
    print("Variable names should explain WHAT the data represents!")
    print()
    
    print("--- BEST PRACTICE 5: Validate Results ---")
    print()
    
    print("After math operations, sanity-check your results:")
    temperatures = np.array([68.0, 72.0, 75.0])
    offset = 5.0
    adjusted = temperatures + offset
    
    print(f"Original temps: {temperatures}")
    print(f"Adding offset {offset}: {adjusted}")
    print()
    
    print("Quick validations:")
    print(f"  All values increased? {np.all(adjusted > temperatures)}")
    print(f"  Increase is correct? {np.allclose(adjusted - temperatures, offset)}")
    print()


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "MILESTONE 11: BASIC MATHEMATICAL OPERATIONS ON NUMPY ARRAYS".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    # Run demonstrations
    demonstrate_numeric_arrays()
    demonstrate_addition()
    demonstrate_subtraction()
    demonstrate_multiplication()
    demonstrate_division()
    demonstrate_scalar_operations()
    demonstrate_numpy_vs_lists()
    demonstrate_shape_compatibility()
    demonstrate_other_operations()
    demonstrate_common_errors()
    demonstrate_best_practices()
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Element-wise operations apply to each element independently")
    print("  • Scalar operations apply a single value to all elements")
    print("  • NumPy arithmetic is much simpler than Python loops")
    print("  • Array shapes must be compatible for element-wise operations")
    print("  • Same shapes: element-wise operation works directly")
    print("  • Different shapes: error unless broadcasting rules apply")
    print("  • Scalar + array always works (scalar broadcasts)")
    print("  • Use np.sqrt(), np.abs(), etc. for common math functions")
    print("  • Always check shapes before operating")
    print("  • NumPy math is vectorized, loops are slow")
    print("  • Element-wise * is NOT matrix multiplication")
    print("\n")
