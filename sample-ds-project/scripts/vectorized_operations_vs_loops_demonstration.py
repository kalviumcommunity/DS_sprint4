"""
=====================================================================
MILESTONE 12: APPLYING VECTORIZED OPERATIONS INSTEAD OF PYTHON LOOPS
=====================================================================

This script demonstrates:
1. Loop-based operations on NumPy arrays
2. Equivalent vectorized operations
3. Verifying that both approaches produce identical results
4. Readability improvements with vectorization
5. Performance implications (conceptual)
6. When vectorization is appropriate
7. Common loop-to-vector conversion patterns
8. Avoiding loops in mathematical operations
9. Numpy functions as vectorized replacements
10. Trade-offs and best practices

Focus: Correctness and readability, not advanced performance benchmarking.
=====================================================================
"""

import numpy as np


# =====================================================================
# SECTION 1: ADDING A SCALAR TO EACH ARRAY ELEMENT
# =====================================================================

def demonstrate_scalar_addition():
    """
    Show loop vs vectorized approach for adding a scalar to each element.
    """
    print("\n" + "="*70)
    print("SECTION 1: ADDING A SCALAR TO EACH ARRAY ELEMENT")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5])
    scalar = 10
    
    print(f"Array: {arr}")
    print(f"Scalar to add: {scalar}")
    print("Goal: Add the scalar to each element")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  result = np.zeros(len(arr))")
    print("  for i in range(len(arr)):")
    print("      result[i] = arr[i] + scalar")
    print()
    
    result_loop = np.zeros(len(arr))
    for i in range(len(arr)):
        result_loop[i] = arr[i] + scalar
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH ---")
    print()
    print("Code:")
    print("  result = arr + scalar")
    print()
    
    result_vector = arr + scalar
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.array_equal(result_loop, result_vector)}")
    print()
    
    print("--- COMPARISON ---")
    print()
    print("Loop version:")
    print("  - Requires creating empty array")
    print("  - Loop over each index")
    print("  - Manual assignment to each element")
    print("  - More verbose and error-prone")
    print()
    print("Vectorized version:")
    print("  - One simple operation: arr + scalar")
    print("  - Clean and readable")
    print("  - No explicit loop, no index management")
    print("  - Broadcasting handled automatically")
    print()


# =====================================================================
# SECTION 2: MULTIPLYING ARRAYS ELEMENT-WISE
# =====================================================================

def demonstrate_element_multiplication():
    """
    Show loop vs vectorized approach for element-wise multiplication.
    """
    print("\n" + "="*70)
    print("SECTION 2: MULTIPLYING ARRAYS ELEMENT-WISE")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr1 = np.array([2, 4, 6, 8, 10])
    arr2 = np.array([1, 2, 3, 4, 5])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print("Goal: Multiply corresponding elements")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  result = np.zeros(len(arr1))")
    print("  for i in range(len(arr1)):")
    print("      result[i] = arr1[i] * arr2[i]")
    print()
    
    result_loop = np.zeros(len(arr1))
    for i in range(len(arr1)):
        result_loop[i] = arr1[i] * arr2[i]
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH ---")
    print()
    print("Code:")
    print("  result = arr1 * arr2")
    print()
    
    result_vector = arr1 * arr2
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.array_equal(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 3: CONDITIONAL OPERATIONS
# =====================================================================

def demonstrate_conditional_operations():
    """
    Show loop vs vectorized approach for conditional operations.
    """
    print("\n" + "="*70)
    print("SECTION 3: CONDITIONAL OPERATIONS (e.g., applying function conditionally)")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Array: {arr}")
    print("Goal: Double values >= 5, keep others as is")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  result = np.zeros(len(arr))")
    print("  for i in range(len(arr)):")
    print("      if arr[i] >= 5:")
    print("          result[i] = arr[i] * 2")
    print("      else:")
    print("          result[i] = arr[i]")
    print()
    
    result_loop = np.zeros(len(arr))
    for i in range(len(arr)):
        if arr[i] >= 5:
            result_loop[i] = arr[i] * 2
        else:
            result_loop[i] = arr[i]
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH (using np.where) ---")
    print()
    print("Code:")
    print("  result = np.where(arr >= 5, arr * 2, arr)")
    print()
    
    result_vector = np.where(arr >= 5, arr * 2, arr)
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.array_equal(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 4: APPLYING MATHEMATICAL FUNCTIONS
# =====================================================================

def demonstrate_mathematical_functions():
    """
    Show loop vs vectorized approach for applying math functions.
    """
    print("\n" + "="*70)
    print("SECTION 4: APPLYING MATHEMATICAL FUNCTIONS")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([1.0, 4.0, 9.0, 16.0, 25.0])
    print(f"Array: {arr}")
    print("Goal: Take square root of each element")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  import math")
    print("  result = np.zeros(len(arr))")
    print("  for i in range(len(arr)):")
    print("      result[i] = math.sqrt(arr[i])")
    print()
    
    import math
    result_loop = np.zeros(len(arr))
    for i in range(len(arr)):
        result_loop[i] = math.sqrt(arr[i])
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH (using np.sqrt) ---")
    print()
    print("Code:")
    print("  result = np.sqrt(arr)")
    print()
    
    result_vector = np.sqrt(arr)
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.allclose(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 5: ACCUMULATING VALUES
# =====================================================================

def demonstrate_accumulation():
    """
    Show loop vs vectorized approach for accumulation.
    """
    print("\n" + "="*70)
    print("SECTION 5: ACCUMULATING VALUES")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print("Goal: Create cumulative sum (running total)")
    print()
    
    print("Example:")
    print("  Input:  [1, 2, 3, 4, 5]")
    print("  Output: [1, 3, 6, 10, 15]  (each element is sum up to that point)")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  result = np.zeros(len(arr))")
    print("  total = 0")
    print("  for i in range(len(arr)):")
    print("      total += arr[i]")
    print("      result[i] = total")
    print()
    
    result_loop = np.zeros(len(arr))
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        result_loop[i] = total
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH (using np.cumsum) ---")
    print()
    print("Code:")
    print("  result = np.cumsum(arr)")
    print()
    
    result_vector = np.cumsum(arr)
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.array_equal(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 6: ABSOLUTE VALUE TRANSFORMATION
# =====================================================================

def demonstrate_absolute_value():
    """
    Show loop vs vectorized approach for absolute value.
    """
    print("\n" + "="*70)
    print("SECTION 6: ABSOLUTE VALUE TRANSFORMATION")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([-5, -2, 0, 3, -8, 7])
    print(f"Array: {arr}")
    print("Goal: Convert all values to absolute value (remove negative sign)")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  result = np.zeros(len(arr))")
    print("  for i in range(len(arr)):")
    print("      if arr[i] < 0:")
    print("          result[i] = -arr[i]")
    print("      else:")
    print("          result[i] = arr[i]")
    print()
    
    result_loop = np.zeros(len(arr))
    for i in range(len(arr)):
        if arr[i] < 0:
            result_loop[i] = -arr[i]
        else:
            result_loop[i] = arr[i]
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH (using np.abs) ---")
    print()
    print("Code:")
    print("  result = np.abs(arr)")
    print()
    
    result_vector = np.abs(arr)
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.array_equal(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 7: FILTERING (MASKING)
# =====================================================================

def demonstrate_filtering():
    """
    Show loop vs vectorized approach for filtering.
    """
    print("\n" + "="*70)
    print("SECTION 7: FILTERING (MASKING) - EXTRACTING ELEMENTS THAT MEET CRITERIA")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Array: {arr}")
    print("Goal: Keep only even numbers")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  result = []")
    print("  for i in range(len(arr)):")
    print("      if arr[i] % 2 == 0:")
    print("          result.append(arr[i])")
    print("  result = np.array(result)")
    print()
    
    result_loop = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            result_loop.append(arr[i])
    result_loop = np.array(result_loop)
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH (using boolean indexing) ---")
    print()
    print("Code:")
    print("  result = arr[arr % 2 == 0]")
    print()
    
    result_vector = arr[arr % 2 == 0]
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.array_equal(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 8: COMPLEX OPERATION - NORMALIZING DATA
# =====================================================================

def demonstrate_normalization():
    """
    Show loop vs vectorized approach for normalization.
    """
    print("\n" + "="*70)
    print("SECTION 8: COMPLEX OPERATION - NORMALIZING DATA")
    print("="*70)
    
    print("\n--- The Problem ---")
    print()
    
    arr = np.array([10.0, 50.0, 30.0, 70.0, 20.0])
    print(f"Array: {arr}")
    print("Goal: Normalize to 0-1 range using min-max scaling")
    print("Formula: (x - min) / (max - min)")
    print()
    
    print("--- LOOP-BASED APPROACH ---")
    print()
    print("Code:")
    print("  min_val = min(arr)")
    print("  max_val = max(arr)")
    print("  result = np.zeros(len(arr))")
    print("  for i in range(len(arr)):")
    print("      result[i] = (arr[i] - min_val) / (max_val - min_val)")
    print()
    
    min_val = min(arr)
    max_val = max(arr)
    result_loop = np.zeros(len(arr))
    for i in range(len(arr)):
        result_loop[i] = (arr[i] - min_val) / (max_val - min_val)
    
    print(f"Result: {result_loop}")
    print()
    
    print("--- VECTORIZED APPROACH ---")
    print()
    print("Code:")
    print("  min_val = arr.min()")
    print("  max_val = arr.max()")
    print("  result = (arr - min_val) / (max_val - min_val)")
    print()
    
    min_val_v = arr.min()
    max_val_v = arr.max()
    result_vector = (arr - min_val_v) / (max_val_v - min_val_v)
    
    print(f"Result: {result_vector}")
    print()
    
    print("--- VERIFICATION ---")
    print()
    print(f"Loop and vectorized produce same result? {np.allclose(result_loop, result_vector)}")
    print()


# =====================================================================
# SECTION 9: READABILITY IMPROVEMENTS WITH VECTORIZATION
# =====================================================================

def demonstrate_readability():
    """
    Show how vectorization improves code readability.
    """
    print("\n" + "="*70)
    print("SECTION 9: READABILITY IMPROVEMENTS WITH VECTORIZATION")
    print("="*70)
    
    print("\n--- HARD TO READ (Loop) ---")
    print()
    print("Code:")
    print("  for i in range(len(prices)):")
    print("      discounts = []")
    print("      for j in range(len(prices[i])):")
    print("          if prices[i][j] > 100:")
    print("              discounts.append(prices[i][j] * 0.9)")
    print("          else:")
    print("              discounts.append(prices[i][j])")
    print()
    print("Problems:")
    print("  - Nested loops are hard to follow")
    print("  - Index management is error-prone")
    print("  - Intent is buried in implementation details")
    print("  - Hard to debug")
    print()
    
    print("--- EASY TO READ (Vectorized) ---")
    print()
    print("Code:")
    print("  prices = np.array([[120, 80, 150], [50, 200, 75]])")
    print("  discounted = np.where(prices > 100, prices * 0.9, prices)")
    print()
    print("Benefits:")
    print("  - Clear intent: 'where price > 100, apply 10% discount'")
    print("  - Concise and readable")
    print("  - No index management")
    print("  - Directly expresses the logic")
    print()


# =====================================================================
# SECTION 10: WHEN TO USE VECTORIZATION
# =====================================================================

def demonstrate_when_to_vectorize():
    """
    Show when vectorization is appropriate vs when loops might be needed.
    """
    print("\n" + "="*70)
    print("SECTION 10: WHEN TO USE VECTORIZATION")
    print("="*70)
    
    print("\n--- GOOD CANDIDATE FOR VECTORIZATION ---")
    print()
    print("Mathematical operations on arrays:")
    print("  - Element-wise arithmetic")
    print("  - Applying mathematical functions")
    print("  - Filtering or masking")
    print("  - Aggregations (sum, mean, etc.)")
    print()
    
    print("Example:")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([2, 4, 6, 8, 10])
    result = arr1 * arr2 + 10
    print(f"  arr1 * arr2 + 10 = {result}  ← Vectorized!")
    print()
    
    print("--- NOT IDEAL FOR VECTORIZATION ---")
    print()
    print("When you need:")
    print("  - Complex conditional logic with many branches")
    print("  - Interactions between iterations")
    print("  - Dynamic array building")
    print()
    print("Example:")
    print("  for i in range(len(arr)):")
    print("      if condition1(arr[i]):")
    print("          if condition2(arr[i]):")
    print("              if condition3(arr[i]):")
    print("                  # Complex nested logic")
    print()
    print("In these cases, loops may be more readable!")
    print()


# =====================================================================
# SECTION 11: BEST PRACTICES FOR VECTORIZATION
# =====================================================================

def demonstrate_best_practices():
    """
    Show best practices when writing vectorized code.
    """
    print("\n" + "="*70)
    print("SECTION 11: BEST PRACTICES FOR VECTORIZATION")
    print("="*70)
    
    print("\n--- BEST PRACTICE 1: Use NumPy Functions When Available ---")
    print()
    print("Instead of:")
    print("  result = [math.sqrt(x) for x in arr]  ← Slow!")
    print()
    print("Use:")
    arr = np.array([1.0, 4.0, 9.0, 16.0])
    print(f"  result = np.sqrt(arr)  = {np.sqrt(arr)}")
    print()
    
    print("--- BEST PRACTICE 2: Avoid Loops Over Large Arrays ---")
    print()
    print("DON'T:")
    print("  for i in range(1000000):")
    print("      result[i] = arr[i] + 1  ← Very slow for large arrays")
    print()
    print("DO:")
    print("  result = arr + 1  ← Vectorized, much faster")
    print()
    
    print("--- BEST PRACTICE 3: Use Boolean Indexing For Filtering ---")
    print()
    print("DON'T:")
    print("  result = []")
    print("  for x in arr:")
    print("      if x > 5:")
    print("          result.append(x)")
    print()
    arr = np.array([1, 3, 5, 7, 9])
    print(f"DO:")
    print(f"  result = arr[arr > 5]  = {arr[arr > 5]}")
    print()
    
    print("--- BEST PRACTICE 4: Keep Code Readable ---")
    print()
    print("Sometimes a small loop is clearer than complex vectorization:")
    print()
    print("TOO COMPLEX:")
    print("  result = np.vectorize(lambda x: x**2 if x > 0 else 0)(arr)")
    print()
    print("CLEARER:")
    print("  result = np.where(arr > 0, arr**2, 0)")
    print()
    print("Still vectorized, but more readable!")
    print()
    
    print("--- BEST PRACTICE 5: Test Your Vectorized Code ---")
    print()
    print("Before replacing loops, verify correctness:")
    print("  loop_result = apply_loop_version(arr)")
    print("  vector_result = apply_vectorized_version(arr)")
    print("  assert np.allclose(loop_result, vector_result)")
    print()


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "MILESTONE 12: VECTORIZED OPERATIONS INSTEAD OF LOOPS".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    # Run demonstrations
    demonstrate_scalar_addition()
    demonstrate_element_multiplication()
    demonstrate_conditional_operations()
    demonstrate_mathematical_functions()
    demonstrate_accumulation()
    demonstrate_absolute_value()
    demonstrate_filtering()
    demonstrate_normalization()
    demonstrate_readability()
    demonstrate_when_to_vectorize()
    demonstrate_best_practices()
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Vectorized operations apply to entire arrays without explicit loops")
    print("  • Use array operations instead of loops wherever possible")
    print("  • Scalar operations: arr + scalar, arr * scalar, etc.")
    print("  • Boolean indexing for filtering: arr[condition]")
    print("  • NumPy functions: np.sqrt(), np.abs(), np.sum(), etc.")
    print("  • np.where() for conditional operations (replaces if-else)")
    print("  • np.cumsum() for accumulation (replaces running loop)")
    print("  • Vectorized code is more readable (intent is clear)")
    print("  • Vectorized code is more maintainable (fewer moving parts)")
    print("  • Always verify vectorized version produces same result as loop")
    print("  • Readability still matters - don't over-complicate for speed")
    print("\n")
