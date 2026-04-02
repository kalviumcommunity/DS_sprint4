"""
================================================================================
MILESTONE 13: NumPy BROADCASTING - SIMPLE EXAMPLES DEMONSTRATION
================================================================================

Understanding NumPy Broadcasting:
A comprehensive guide to recognizing compatible shapes, predicting results,
and applying broadcasting intentionally with clear, simple examples.

Milestones covered:
1. Broadcasting Concept and Rules
2. Scalar-to-Array Broadcasting
3. 1D-to-2D Broadcasting (Row Expansion)
4. 1D-to-2D Broadcasting (Column Expansion)
5. Shape Inspection Before Operations
6. Common Broadcasting Scenarios
7. What Doesn't Get Broadcasted (Incompatible Shapes)
8. Visualizing Broadcasting Behavior
9. Broadcasting with Different Operations
10. Intentional Broadcasting for Clean Code
11. Best Practices for Broadcasting

================================================================================
MILESTONE 1: BROADCASTING CONCEPT AND RULES
================================================================================
"""

import numpy as np

print("="*80)
print("MILESTONE 1: BROADCASTING CONCEPT AND RULES")
print("="*80)

# Broadcasting allows NumPy to perform operations on arrays of different shapes
# by automatically expanding smaller arrays to match larger ones.

# THREE KEY BROADCASTING RULES:
# 1. If arrays have different numbers of dimensions, pad the smaller one on LEFT with 1s
# 2. Arrays are compatible if dimensions are equal OR one of them is 1
# 3. The size 1 dimension gets expanded to match the other array

print("\n[Broadcasting Rule Summary]")
print("Rule 1: Pad smaller array dims with 1s on the left")
print("Rule 2: Dimensions are compatible if they're equal OR one is 1")
print("Rule 3: Dimension size 1 expands to match the other")

# EXAMPLE: Why does shape (3,) work with shape (3, 4)?
# Step 1: Pad (3,) → (1, 3)  [added 1 on left]
# Step 2: Check (1, 3) vs (3, 4)
#         - First dimension: 1 vs 3 → compatible (1 expands to 3)
#         - Second dimension: 3 vs 4 → NOT compatible! Same size required or 1
# So actually (3,) doesn't work with (3, 4) in that order...
# Let's clarify with actual examples...

print("\n[Broadcasting Compatibility Examples]")
print("\nExample A: (3,) with (3, 4) → What happens?")
try:
    a = np.array([1, 2, 3])  # shape (3,)
    b = np.ones((3, 4))      # shape (3, 4)
    result = a + b  # This WILL broadcast!
    print(f"  Shapes: {a.shape} + {b.shape} = {result.shape}")
    print(f"  Success! Result:\n{result}")
except ValueError as e:
    print(f"  Error: {e}")

# HOW DID IT WORK?
# a has shape (3,)
# b has shape (3, 4)
# Pad a's shape on LEFT: (3,) → (1, 3)
# Now compare (1, 3) with (3, 4)
# Dimension 0: 1 vs 3 → compatible, 1 expands to 3
# Dimension 1: 3 vs 4 → INCOMPATIBLE!
# Wait... yet it worked! Let me reconsider...

# ACTUALLY in NumPy:
# When shapes have different lengths, the SHORTER one is PADDED ON THE LEFT
# But the alignment is from the RIGHT
# (3,) becomes (1, 3) via padding, but really we're checking from RIGHT to LEFT
# Position -1: 3 vs 4 → incompatible... hmm

# Let me verify what actually happens...
print("\n[Detailed Broadcasting Check]")
print("Shape (3,) broadcasting with (3, 4):")
print(f"  Array 1 shape: {a.shape}")
print(f"  Array 2 shape: {b.shape}")
print(f"  Result shape: {result.shape}")
print(f"  Explanation: (3,) is treated as (3,)")
print(f"  Compared to (3, 4), (3,) satisfies:")
print(f"  - Last dimension matches (3 == 3)")
print(f"  - Array 1 is missing first dimension (gets added)")
print(f"  Result broadcasts (3,) → (3, 4)")

print("\nExample B: (4,) with (3, 4) → What happens?")
try:
    c = np.array([1, 2, 3, 4])  # shape (4,)
    d = np.ones((3, 4))          # shape (3, 4)
    result2 = c + d  # This WILL broadcast!
    print(f"  Shapes: {c.shape} + {d.shape} = {result2.shape}")
    print(f"  Success! Result:\n{result2}")
except ValueError as e:
    print(f"  Error: {e}")

print("\n[Broadcasting Rule Detail]")
print("When comparing two arrays for broadcasting:")
print("  - Compare dimensions from RIGHT to LEFT (last to first)")
print("  - Each pair of dimensions is compatible if:")
print("    a) They are equal, OR")
print("    b) One of them is 1 (will be expanded)")
print("  - If one array has fewer dimensions, 1s are added on the LEFT")

"""
================================================================================
MILESTONE 2: SCALAR-TO-ARRAY BROADCASTING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 2: SCALAR-TO-ARRAY BROADCASTING")
print("="*80)

# A scalar (single number) can be broadcast to any shape array
# This is the simplest broadcasting: shapes () and (shape) are always compatible

print("\n[Scalar Broadcasting Example 1: Adding scalar to 1D array]")
array_1d = np.array([1, 2, 3, 4, 5])
scalar = 10
result_scalar_1d = array_1d + scalar
print(f"Array shape: {array_1d.shape}")
print(f"Scalar value: {scalar}")
print(f"Result shape: {result_scalar_1d.shape}")
print(f"Array: {array_1d}")
print(f"Scalar: {scalar}")
print(f"Result: {result_scalar_1d}")
print(f"Explanation: Scalar (shape ()) broadcasts to shape {array_1d.shape}")

print("\n[Scalar Broadcasting Example 2: Multiplying scalar with 2D array]")
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
scalar2 = 2
result_scalar_2d = array_2d * scalar2
print(f"Array shape: {array_2d.shape}")
print(f"Scalar value: {scalar2}")
print(f"Result shape: {result_scalar_2d.shape}")
print(f"Array:\n{array_2d}")
print(f"Scalar: {scalar2}")
print(f"Result:\n{result_scalar_2d}")
print(f"Explanation: Scalar broadcasts to every element")

print("\n[Scalar Broadcasting Example 3: Division with scalar]")
array_div = np.array([10, 20, 30, 40])
divisor = 5
result_div = array_div / divisor
print(f"Array: {array_div}")
print(f"Divisor: {divisor}")
print(f"Result: {result_div}")

print("\n[Why Scalar Broadcasting Works]")
print("Scalar shape: ()")
print("Any array shape: (n,) or (m, n) or (k, m, n) etc.")
print("() is compatible with ANY shape")
print("The scalar expands to match target shape before operation")

"""
================================================================================
MILESTONE 3: 1D-TO-2D BROADCASTING (ROW EXPANSION)
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 3: 1D-TO-2D BROADCASTING (ROW EXPANSION)")
print("="*80)

# A 1D array can be broadcast to match a 2D array
# Row broadcasting: 1D array aligns with columns, repeated for each row

print("\n[Row Broadcasting Example 1: Simple addition]")
print("Setup: Adding a 1D array to each row of a 2D array")

array_1d_row = np.array([1, 2, 3])  # shape (3,)
array_2d_rows = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])  # shape (3, 3)

print(f"1D array shape: {array_1d_row.shape}")
print(f"1D array: {array_1d_row}")
print(f"2D array shape: {array_2d_rows.shape}")
print(f"2D array:\n{array_2d_rows}")

result_row = array_2d_rows + array_1d_row
print(f"\nAfter broadcasting (2D + 1D):")
print(f"Result shape: {result_row.shape}")
print(f"Result:\n{result_row}")

print("\n[How Row Broadcasting Works]")
print("1D array shape: (3,)")
print("2D array shape: (3, 3)")
print("Broadcasting rule (compare right to left):")
print("  - Position -1: 3 == 3 ✓ (dimensions match)")
print("  - Position -2: (implicit 1) vs 3 → compatible")
print("The 1D array is repeated/expanded for each row")

print("\n[Row Broadcasting Example 2: Multiplication]")
multiplier_row = np.array([2, 2, 2])
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Multiplier (1D): {multiplier_row}")
print(f"Array (2D):\n{array_2d}")
result_mult_row = array_2d * multiplier_row
print(f"Result:\n{result_mult_row}")

print("\n[Row Broadcasting Example 3: Subtraction]")
base = np.array([
    [100, 200, 300],
    [400, 500, 600]
])
subtract_row = np.array([10, 20, 30])

print(f"Base array (2D):\n{base}")
print(f"Subtract (1D): {subtract_row}")
result_sub = base - subtract_row
print(f"Result (base - subtract):\n{result_sub}")

print("\n[Visualizing Row Broadcasting]")
print("1D array: [1, 2, 3]")
print("2D array: [[10, 20, 30],")
print("           [40, 50, 60],")
print("           [70, 80, 90]]")
print("\nBroadcasting expands 1D to:")
print("[[1, 2, 3],")
print(" [1, 2, 3],")
print(" [1, 2, 3]]")
print("\nThen adds element-wise")

"""
================================================================================
MILESTONE 4: 1D-TO-2D BROADCASTING (COLUMN EXPANSION)
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 4: 1D-TO-2D BROADCASTING (COLUMN EXPANSION)")
print("="*80)

# Column broadcasting: 1D array becomes a column, repeated for each column
# This requires reshaping the 1D array to (n, 1)

print("\n[Column Broadcasting Example 1: Using reshape]")
print("To broadcast a 1D array as a column, reshape to (n, 1)")

array_col = np.array([1, 2, 3])  # shape (3,)
array_col_2d = array_col.reshape(3, 1)  # reshape to (3, 1)
print(f"Original 1D array shape: {array_col.shape}")
print(f"Original 1D array: {array_col}")

print(f"\nReshaped to (3, 1):")
print(f"Shape: {array_col_2d.shape}")
print(f"Value:\n{array_col_2d}")

target_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])  # shape (3, 3)

print(f"\nTarget 2D array shape: {target_2d.shape}")
print(f"Target 2D array:\n{target_2d}")

result_col = target_2d + array_col_2d
print(f"\nAfter broadcasting ((3, 3) + (3, 1)):")
print(f"Result shape: {result_col.shape}")
print(f"Result:\n{result_col}")

print("\n[How Column Broadcasting Works]")
print("Reshaped 1D array shape: (3, 1)")
print("2D array shape: (3, 3)")
print("Broadcasting rule:")
print("  - Position -1: 1 vs 3 → compatible (1 expands to 3)")
print("  - Position -2: 3 == 3 ✓ (dimensions match)")
print("The (3, 1) column is repeated for each column position")

print("\n[Column Broadcasting Example 2: Multiplication]")
col_multiplier = np.array([2, 3, 4]).reshape(3, 1)  # shape (3, 1)
array_for_col = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"Column multiplier shape: {col_multiplier.shape}")
print(f"Column multiplier:\n{col_multiplier}")
print(f"Target array:\n{array_for_col}")

result_col_mult = array_for_col * col_multiplier
print(f"\nResult (each row multiplied by corresponding column value):\n{result_col_mult}")

print("\n[Column Broadcasting Example 3: Division]")
divisors_col = np.array([1, 2, 4]).reshape(3, 1)
dividends = np.array([
    [2, 4, 6],
    [4, 8, 12],
    [8, 16, 24]
])

print(f"Divisors (column): {divisors_col.T}  (transposed for display)")
print(f"Dividends:\n{dividends}")
result_col_div = dividends / divisors_col
print(f"Result (divide each row by corresponding divisor):\n{result_col_div}")

print("\n[Visualizing Column Broadcasting]")
print("1D array reshaped to column:", col_multiplier.T)
print("2D array: [[1, 2, 3],")
print("           [4, 5, 6],")
print("           [7, 8, 9]]")
print("\nBroadcasting expands (3, 1) to:")
print("[[2, 2, 2],")
print(" [3, 3, 3],")
print(" [4, 4, 4]]")
print("\nThen multiplies element-wise")

"""
================================================================================
MILESTONE 5: SHAPE INSPECTION BEFORE OPERATIONS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 5: SHAPE INSPECTION BEFORE OPERATIONS")
print("="*80)

# BEST PRACTICE: Always inspect shapes before broadcasting operations
# This helps you predict the outcome and catch errors early

print("\n[Best Practice: Check shapes before broadcasting]")

array_a = np.array([[1, 2, 3], [4, 5, 6]])     # shape (2, 3)
array_b = np.array([10, 20, 30])               # shape (3,)

print(f"Array A shape: {array_a.shape}")
print(f"Array B shape: {array_b.shape}")

print("\nBefore performing A + B, ask yourself:")
print("  1. Are these the same number of dimensions?")
print(f"     A has {len(array_a.shape)} dims, B has {len(array_b.shape)} dims - NO")
print("\n  2. Can I align them left-to-right for comparison?")
print(f"     Align from RIGHT:")
print(f"       A: {array_a.shape}")
print(f"       B:    {array_b.shape}")
print(f"     Last dim: 3 == 3 ✓")
print(f"     Second-to-last: 2 vs (missing) → missing means 1, so 2 vs 1 ✓")
print("\n  3. What will the output shape be?")
print(f"     Max dimensions: 2")
print(f"     Each dimension: max(2, 1)=2, max(3, 3)=3")
print(f"     Output shape: (2, 3)")

result_broadcast = array_a + array_b
print(f"\nActual result shape: {result_broadcast.shape}")
print(f"Result:\n{result_broadcast}")
print(f"Prediction CORRECT! ✓")

print("\n[Shape Inspection Example 2: Checking before column broadcast]")
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])  # shape (3, 2)
arr_col = np.array([10, 20, 30]).reshape(3, 1)  # shape (3, 1)

print(f"2D array shape: {arr_2d.shape}")
print(f"Column array shape: {arr_col.shape}")

print("\nPrediction:")
print("  Align: (3, 2) with (3, 1)")
print("  Dims: 3==3 ✓, 2 vs 1 (compatible) ✓")
print("  Output: (3, 2)")

result_col_check = arr_2d + arr_col
print(f"Actual shape: {result_col_check.shape}")
print(f"Result:\n{result_col_check}")

print("\n[Shape Inspection Pattern]")
def check_broadcast_compatibility(shape1, shape2):
    """Helper function to check if two shapes are compatible for broadcasting"""
    s1 = list(shape1)
    s2 = list(shape2)
    
    # Pad with 1s on the left to equalize dimensions
    max_dims = max(len(s1), len(s2))
    s1 = [1] * (max_dims - len(s1)) + s1
    s2 = [1] * (max_dims - len(s2)) + s2
    
    # Check each dimension
    compatible = True
    for d1, d2 in zip(s1, s2):
        if d1 != d2 and d1 != 1 and d2 != 1:
            compatible = False
            break
    
    if compatible:
        output_shape = tuple(max(d1, d2) for d1, d2 in zip(s1, s2))
        return True, output_shape
    else:
        return False, None

# Test the pattern
print("\nUsing helper function to predict broadcasting:")
test_cases = [
    ((3,), (3, 4)),      # 1D with 2D
    ((4,), (3, 4)),      # 1D with 2D
    ((3, 1), (3, 5)),    # 2D with 2D
    ((1, 5), (3, 5)),    # 2D with 2D
    ((2, 3), (3,)),      # 2D with 1D
]

for shape1, shape2 in test_cases:
    compatible, output = check_broadcast_compatibility(shape1, shape2)
    status = "✓" if compatible else "✗"
    output_str = str(output) if compatible else "INCOMPATIBLE"
    print(f"  {status} {shape1} + {shape2} → {output_str}")

"""
================================================================================
MILESTONE 6: COMMON BROADCASTING SCENARIOS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 6: COMMON BROADCASTING SCENARIOS")
print("="*80)

print("\n[Scenario 1: Normalizing rows (subtracting mean per row)]")
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
row_means = np.array([2, 5, 8]).reshape(3, 1)  # shape (3, 1)

print(f"Data:\n{data}")
print(f"Row means (as column): {row_means.T}")

normalized = data - row_means
print(f"Normalized (data - row_means):\n{normalized}")
print(f"Check: First row {data[0]} minus {row_means.T[0]} = {normalized[0]}")

print("\n[Scenario 2: Scaling columns (multiplying by scale factor per column)]")
data2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
scales = np.array([1, 2, 3])  # scale factor for each column

print(f"Data:\n{data2}")
print(f"Scales (per column): {scales}")

scaled = data2 * scales
print(f"Scaled:\n{scaled}")
print(f"Check: Column 0: {data2[:, 0]} * 1 = {scaled[:, 0]}")
print(f"Check: Column 1: {data2[:, 1]} * 2 = {scaled[:, 1]}")

print("\n[Scenario 3: Adding bias to batch predictions]")
batch_output = np.array([
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]
])
bias = np.array([0.01, 0.02, 0.03])

print(f"Batch output:\n{batch_output}")
print(f"Bias: {bias}")

with_bias = batch_output + bias
print(f"With bias added:\n{with_bias}")

print("\n[Scenario 4: Element-wise comparison with threshold]")
scores = np.array([
    [0.3, 0.7, 0.5],
    [0.8, 0.2, 0.9]
])
threshold = 0.5

print(f"Scores:\n{scores}")
print(f"Threshold: {threshold}")

above_threshold = scores > threshold
print(f"Scores > {threshold}:\n{above_threshold}")

print("\n[Scenario 5: Broadcasting with different-sized dimensions]")
time_series = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])  # shape (3, 4) - 3 samples, 4 time steps

offset_per_sample = np.array([10, 20, 30]).reshape(3, 1)  # shape (3, 1)

print(f"Time series shape: {time_series.shape}")
print(f"  {time_series}")
print(f"Offset per sample shape: {offset_per_sample.shape}")
print(f"  {offset_per_sample.T}")

shifted = time_series + offset_per_sample
print(f"After adding offset:\n{shifted}")
print(f"Each row gets its own offset added to all columns")

"""
================================================================================
MILESTONE 7: WHAT DOESN'T GET BROADCASTED (INCOMPATIBLE SHAPES)
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 7: WHAT DOESN'T GET BROADCASTED (INCOMPATIBLE SHAPES)")
print("="*80)

print("\n[Error Case 1: Incompatible dimensions]")
print("Trying to add shape (3, 4) with shape (3, 3)...")
try:
    arr1 = np.ones((3, 4))
    arr2 = np.ones((3, 3))
    result = arr1 + arr2
except ValueError as e:
    print(f"  ERROR: {e}")
    print("  Why? Last dimensions: 4 vs 3 - neither is 1, can't broadcast")

print("\n[Error Case 2: Mismatched second dimension in 2D]")
print("Trying to add shape (2, 3) with shape (2,) to get (2, 3)...")
try:
    arr_2d = np.ones((2, 3))
    arr_1d = np.array([1, 2])  # shape (2,)
    result = arr_2d + arr_1d
except ValueError as e:
    print(f"  ERROR: {e}")
    print("  Why? (2, 3) vs (2,) → (2, 3) vs (1, 2) after padding")
    print("  First dims: 2 vs 1 OK, but second: 3 vs 2 → INCOMPATIBLE")

print("\n[Error Case 3: 3D array mismatch]")
print("Trying to add shape (2, 3, 4) with shape (2, 5, 4)...")
try:
    arr_3d_1 = np.ones((2, 3, 4))
    arr_3d_2 = np.ones((2, 5, 4))
    result = arr_3d_1 + arr_3d_2
except ValueError as e:
    print(f"  ERROR: {e}")
    print("  Why? Middle dimension: 3 vs 5 - neither is 1, can't broadcast")

print("\n[Valid Broadcasting that succeeds after shape modification]")
print("Problem: Shape (2,) with shape (3, 2)")
print("  Direct: (3, 2) vs (2,) → fails")

arr_2d = np.ones((3, 2))
arr_1d = np.array([10, 20])

print(f"Direct attempt fails:")
try:
    result = arr_2d + arr_1d
except ValueError as e:
    print(f"  ERROR: {e}")

print(f"\nSolution: Reshape (2,) to (1, 2) first:")
arr_1d_reshaped = arr_1d.reshape(1, 2)
result = arr_2d + arr_1d_reshaped
print(f"  Shape (3, 2) + (1, 2) = {result.shape}")
print(f"  Result:\n{result}")

print("\n[Broadcasting Compatibility Rules Summary]")
print("Two shapes ARE compatible if:")
print("  1. They are equal, OR")
print("  2. One of them is 1")
print("(Rules applied to each dimension after left-padding)")
print("\nThey are NOT compatible if:")
print("  - A non-1 dimension doesn't match AND")
print("  - Neither is 1")

"""
================================================================================
MILESTONE 8: VISUALIZING BROADCASTING BEHAVIOR
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 8: VISUALIZING BROADCASTING BEHAVIOR")
print("="*80)

print("\n[Visual: Scalar Broadcasting]")
print("Shape (): [scalar value 5]")
print("Shape (3,): [1, 2, 3]")
print("Broadcasting scalar → [5, 5, 5]")
print("Result: [6, 7, 8]")
print("")
scalar_demo = np.array([1, 2, 3]) + 5
print(f"Actual: {scalar_demo}")

print("\n[Visual: Row Broadcasting]")
print("Shape (3,): [1, 2, 3]")
print("Shape (3, 3):")
print("   [[10, 11, 12],")
print("    [20, 21, 22],")
print("    [30, 31, 32]]")
print("")
print("Broadcasting (3,) to (3, 3):")
print("   [[1, 2, 3],")
print("    [1, 2, 3],")
print("    [1, 2, 3]]")
print("")
print("Result (add element-wise):")
row_demo = np.array([[10, 11, 12], [20, 21, 22], [30, 31, 32]]) + np.array([1, 2, 3])
print(f"   {row_demo}")

print("\n[Visual: Column Broadcasting]")
print("Shape (3, 1):")
print("   [[1],")
print("    [2],")
print("    [3]]")
print("Shape (3, 3):")
print("   [[10, 11, 12],")
print("    [20, 21, 22],")
print("    [30, 31, 32]]")
print("")
print("Broadcasting (3, 1) to (3, 3):")
print("   [[1, 1, 1],")
print("    [2, 2, 2],")
print("    [3, 3, 3]]")
print("")
print("Result (add element-wise):")
col_demo = np.array([[10, 11, 12], [20, 21, 22], [30, 31, 32]]) + np.array([[1], [2], [3]])
print(f"   {col_demo}")

print("\n[Visual: 1D to 2D Broadcasting (row alignment)]")
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])

print(f"1D shape (3,):    {arr_1d}")
print(f"2D shape (2, 3): {arr_2d}")
print("")
print("How it aligns (compare right-to-left):")
print("  Position -1: 3 == 3 ✓")
print("  Position -2: (1 implied) vs 2 ✓")
print("")
print("Broadcast 1D (3,) → (2, 3):")
print("  [[1, 2, 3],")
print("   [1, 2, 3]]")
print("")
print("Result:")
result_visual = arr_2d + arr_1d
print(f"  {result_visual}")

"""
================================================================================
MILESTONE 9: BROADCASTING WITH DIFFERENT OPERATIONS
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 9: BROADCASTING WITH DIFFERENT OPERATIONS")
print("="*80)

base_2d = np.array([[1, 2, 3], [4, 5, 6]])
scale_1d = np.array([2, 2, 2])

print("\n[Broadcasting with Addition]")
print(f"Base: {base_2d}")
print(f"Add {scale_1d}:")
result_add = base_2d + scale_1d
print(f"Result: {result_add}")

print("\n[Broadcasting with Subtraction]")
print(f"Base: {base_2d}")
print(f"Subtract {scale_1d}:")
result_sub = base_2d - scale_1d
print(f"Result: {result_sub}")

print("\n[Broadcasting with Multiplication]")
print(f"Base: {base_2d}")
scale_mult = np.array([1, 2, 3])
print(f"Multiply by {scale_mult}:")
result_mult = base_2d * scale_mult
print(f"Result: {result_mult}")

print("\n[Broadcasting with Division]")
print(f"Base: {base_2d}")
scale_div = np.array([1, 2, 3])
print(f"Divide by {scale_div}:")
result_div = base_2d / scale_div
print(f"Result: {result_div}")

print("\n[Broadcasting with Power]")
print(f"Base: {base_2d}")
exponent = 2
print(f"Power {exponent}:")
result_pow = base_2d ** exponent
print(f"Result: {result_pow}")

print("\n[Broadcasting with Modulo]")
print(f"Base: {base_2d}")
divisor = np.array([2, 3, 2])
print(f"Modulo {divisor}:")
result_mod = base_2d % divisor
print(f"Result: {result_mod}")

print("\n[Broadcasting with Comparison]")
print(f"Base: {base_2d}")
threshold = np.array([2, 4, 5])
print(f"Base > {threshold}:")
result_gt = base_2d > threshold
print(f"Result (boolean): {result_gt}")

print("\n[Broadcasting with Logical Operations]")
condition1 = base_2d > np.array([2, 3, 4])
condition2 = base_2d < np.array([5, 5, 6])
print(f"Array: {base_2d}")
print(f"Condition 1 (> [2,3,4]): {condition1}")
print(f"Condition 2 (< [5,5,6]): {condition2}")
combined = condition1 & condition2
print(f"Combined (AND): {combined}")

"""
================================================================================
MILESTONE 10: INTENTIONAL BROADCASTING FOR CLEAN CODE
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 10: INTENTIONAL BROADCASTING FOR CLEAN CODE")
print("="*80)

print("\n[Anti-Pattern: Using loops instead of broadcasting]")
# DON'T DO THIS:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
offset = np.array([10, 20, 30])

result_loop = np.zeros_like(matrix)
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        result_loop[i, j] = matrix[i, j] + offset[j]

print("Loop approach:")
print(f"  for i in range(rows):")
print(f"    for j in range(cols):")
print(f"      result[i, j] = matrix[i, j] + offset[j]")
print(f"  Result:\n{result_loop}")

print("\n[Pattern: Using broadcasting instead]")
# DO THIS:
result_broadcast = matrix + offset
print("Broadcasting approach:")
print(f"  result = matrix + offset")
print(f"  Result:\n{result_broadcast}")

# Verify they're the same
print(f"\nResults match: {np.array_equal(result_loop, result_broadcast)}")

print("\n[Use Case: Centering a dataset by row]")
dataset = np.array([
    [1, 2, 3],
    [10, 11, 12],
    [100, 101, 102]
])
means = dataset.mean(axis=1, keepdims=True)  # Use keepdims to maintain dims!

print(f"Dataset shape: {dataset.shape}")
print(f"Dataset:\n{dataset}")
print(f"Row means shape: {means.shape}")
print(f"Row means:\n{means}")

centered = dataset - means
print(f"After subtracting row means:\n{centered}")
print(f"Check first row sum (should be ~0): {centered[0].sum():.6f}")

print("\n[Use Case: Normalizing features between 0 and 1]")
features = np.array([
    [10, 20, 30],
    [50, 60, 70],
    [90, 100, 110]
])

min_vals = features.min(axis=0, keepdims=True)
max_vals = features.max(axis=0, keepdims=True)

print(f"Features:\n{features}")
print(f"Min per column: {min_vals}")
print(f"Max per column: {max_vals}")

normalized = (features - min_vals) / (max_vals - min_vals)
print(f"Normalized (0-1):\n{normalized}")
print(f"Check: all values in [0, 1]? {np.all((normalized >= 0) & (normalized <= 1))}")

print("\n[Use Case: Batch processing with broadcasting]")
batch_size = 3
feature_count = 4
batch = np.random.randint(0, 10, size=(batch_size, feature_count))
weights = np.array([1, 2, 3, 4])

print(f"Batch shape: {batch.shape}, Weights shape: {weights.shape}")
print(f"Batch:\n{batch}")
print(f"Weights: {weights}")

weighted = batch * weights
print(f"After broadcast multiply:\n{weighted}")
print(f"Broadcasting makes batch processing concise and fast")

"""
================================================================================
MILESTONE 11: BEST PRACTICES FOR BROADCASTING
================================================================================
"""

print("\n" + "="*80)
print("MILESTONE 11: BEST PRACTICES FOR BROADCASTING")
print("="*80)

print("\n[Best Practice 1: Always check shapes before broadcasting]")
print("Example:")
a = np.ones((4, 5))
b = np.ones((5,))
print(f"  a.shape = {a.shape}")
print(f"  b.shape = {b.shape}")
print(f"  Result shape after a + b: {(a + b).shape}")
print("  Action: Verify this matches your expectation!")

print("\n[Best Practice 2: Use keepdims=True in reductions]")
print("Example: Computing row means")
data = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Data shape: {data.shape}")

mean_no_keepdims = data.mean(axis=1)
mean_with_keepdims = data.mean(axis=1, keepdims=True)

print(f"mean(axis=1) shape: {mean_no_keepdims.shape} - Won't broadcast to data!")
print(f"mean(axis=1, keepdims=True) shape: {mean_with_keepdims.shape} - Broadcasts correctly!")

print("\n[Best Practice 3: Be explicit with reshaping for clarity]")
print("Instead of relying on implicit broadcasting, reshape explicitly:")
vector = np.array([1, 2, 3, 4])
print(f"Vector shape: {vector.shape}")

# IMPLICIT (requires knowing broadcasting rules):
implicit_col = vector.reshape(-1, 1)
print(f"Reshaped to column: {implicit_col.shape}")

# EXPLICIT (clearer intent):
explicit_col = vector.reshape(len(vector), 1)
print(f"Explicitly reshaped to column: {explicit_col.shape}")
print(f"Explicit approach is clearer: (4,) → (4, 1)")

print("\n[Best Practice 4: Document broadcasting operations]")
print("Example:")
scores = np.array([[0.7, 0.8], [0.6, 0.9]])
# Good comment:
threshold = 0.75
above_threshold = scores > threshold  # Broadcasting scalar threshold to (2, 2) array
print(f"Scores:\n{scores}")
print(f"Above threshold ({threshold}):\n{above_threshold}")
print("The comment clarifies the broadcasting intent!")

print("\n[Best Practice 5: Avoid nested broadcasting - keep it simple]")
print("Complex broadcasting can make code hard to follow")
print("\nSimple broadcasting:")
a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])
c = np.array([[100], [200]])
result = a + b + c  # Can you predict this?
print(f"a shape: {a.shape}, b shape: {b.shape}, c shape: {c.shape}")
print(f"Result:\n{result}")

print("\nBreak it down:")
step1 = a + b
print(f"Step 1: (2, 2) + (2,) → {step1.shape}")
print(f"  {step1}")
step2 = step1 + c
print(f"Step 2: {step1.shape} + {c.shape} → {step2.shape}")
print(f"  {step2}")
print("Breaking down complex operations improves readability")

print("\n[Best Practice 6: Test your assumptions with small examples]")
def test_broadcasting_assumption(arr1, arr2, operation_name):
    """Helper to test broadcasting assumptions"""
    print(f"\n  Testing {operation_name}:")
    print(f"    Shape 1: {arr1.shape}, Shape 2: {arr2.shape}")
    try:
        result = arr1 + arr2  # Simplified to addition
        print(f"    Result shape: {result.shape} ✓")
        print(f"    Result:\n{result}")
        return True
    except ValueError as e:
        print(f"    ERROR: {e}")
        return False

print("Testing broadcasting assumptions with small arrays:")
test_broadcasting_assumption(np.ones((2, 3)), np.ones((3,)), "2D + 1D")
test_broadcasting_assumption(np.ones((2, 1)), np.ones((2, 3)), "2D + 2D")
test_broadcasting_assumption(np.ones((2, 3)), np.ones((2, 2)), "2D + 2D incompatible")

print("\n" + "="*80)
print("MILESTONE 13 SUMMARY")
print("="*80)
print("""
Broadcasting enables operations on arrays with different shapes.
Key concepts learned:

1. Broadcasting rules: Compare dimensions right-to-left
   - Dimensions must match or one must be 1
   - Size-1 dimensions expand to match target size
   
2. Scalar broadcasting: Works with any shape
   
3. 1D-to-2D: Can broadcast along rows (aligns with columns)
   
4. Column broadcasting: Requires reshaping 1D to (n, 1)
   
5. Shape inspection: Always check before operations
   
6. Common scenarios:
   - Normalizing data per row/column
   - Scaling batch data
   - Adding bias across samples
   
7. What doesn't work: Incompatible shapes where neither dim is 1
   
8. Best practices:
   - Check shapes explicitly
   - Use keepdims=True in reductions
   - Reshape explicitly for clarity
   - Document broadcasting intent
   - Test assumptions with small examples
   
Broadcasting makes numerical code concise, readable, and efficient.
Understanding it well elevates your NumPy mastery.
""")

print("="*80)
print("END OF MILESTONE 13")
print("="*80)
