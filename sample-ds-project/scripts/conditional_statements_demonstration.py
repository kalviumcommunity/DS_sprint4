"""
Python Conditional Statements for Data Logic Demonstration

This script demonstrates core understanding of:
- Basic if statements
- if-else branching
- if-elif-else structures with multiple conditions
- Logical operators (and, or, not)
- Data type considerations in comparisons
- Common pitfalls and debugging techniques
"""


def demonstrate_basic_if():
    """
    Demonstrate simple if statements with basic conditions.
    """
    print("\n" + "=" * 60)
    print("1. BASIC IF STATEMENTS")
    print("=" * 60)

    # Basic if with numeric comparison
    print("\n--- Basic If: Numeric Comparison ---")
    age = 18
    print(f"age = {age}")
    print(f"Condition: if age >= 18")

    if age >= 18:
        print("[OK] Condition is True: You are an adult")

    print()

    age = 16
    print(f"age = {age}")
    print(f"Condition: if age >= 18")

    if age >= 18:
        print("[OK] Condition is True: You are an adult")
    # If condition is False, nothing happens (no output)
    print("(No output because condition is False)")

    # Basic if with string comparison
    print("\n--- Basic If: String Comparison ---")
    status = "active"
    print(f"status = '{status}'")
    print(f"Condition: if status == 'active'")

    if status == "active":
        print("[OK] Condition is True: Account is active")

    print()

    status = "inactive"
    print(f"status = '{status}'")
    print(f"Condition: if status == 'active'")
    if status == "active":
        print("[OK] Condition is True: Account is active")
    print("(No output because condition is False)")

    # Basic if with list membership
    print("\n--- Basic If: Membership Testing ---")
    permissions = ["read", "write", "delete"]
    print(f"permissions = {permissions}")
    print(f"Condition: if 'write' in permissions")

    if "write" in permissions:
        print("[OK] Condition is True: User has write permission")

    print()

    print(f"Condition: if 'admin' in permissions")
    if "admin" in permissions:
        print("[OK] Condition is True: User is admin")
    print("(No output because condition is False)")


def demonstrate_if_else():
    """
    Demonstrate if-else decision branches.
    """
    print("\n" + "=" * 60)
    print("2. IF-ELSE BRANCHING (Two Paths)")
    print("=" * 60)

    # Numeric if-else
    print("\n--- Numeric If-Else ---")
    score = 75
    print(f"score = {score}")
    print(f"Condition: if score >= 60:")

    if score >= 60:
        print("[OK] Condition is True: PASS")
    else:
        print("[FAIL] Condition is False: FAIL")

    print()

    score = 45
    print(f"score = {score}")
    print(f"Condition: if score >= 60:")

    if score >= 60:
        print("[OK] Condition is True: PASS")
    else:
        print("[FAIL] Condition is False: FAIL")

    # String comparison if-else
    print("\n--- String If-Else ---")
    user_role = "admin"
    print(f"user_role = '{user_role}'")
    print(f"Condition: if user_role == 'admin':")

    if user_role == "admin":
        print("[OK] Admin access granted")
    else:
        print("[FAIL] Standard user access only")

    print()

    user_role = "guest"
    print(f"user_role = '{user_role}'")
    print(f"Condition: if user_role == 'admin':")

    if user_role == "admin":
        print("[OK] Admin access granted")
    else:
        print("[FAIL] Standard user access only")

    # Boolean if-else
    print("\n--- Boolean If-Else ---")
    is_authenticated = True
    print(f"is_authenticated = {is_authenticated}")
    print(f"Condition: if is_authenticated:")

    if is_authenticated:
        print("[OK] User is authenticated: Allow access")
    else:
        print("[FAIL] User not authenticated: Deny access")

    print()

    is_authenticated = False
    print(f"is_authenticated = {is_authenticated}")
    print(f"Condition: if is_authenticated:")

    if is_authenticated:
        print("[OK] User is authenticated: Allow access")
    else:
        print("[FAIL] User not authenticated: Deny access")


def demonstrate_if_elif_else():
    """
    Demonstrate if-elif-else structures with multiple conditions.
    """
    print("\n" + "=" * 60)
    print("3. IF-ELIF-ELSE (Multiple Conditions)")
    print("=" * 60)

    # Grade classification example
    print("\n--- Grade Classification (Multiple Paths) ---")

    def classify_grade(score):
        print(f"\nScore: {score}")
        if score >= 90:
            print("  -> Condition 1 (>= 90) is True")
            print("  Grade: A (Excellent)")
        elif score >= 80:
            print("  -> Condition 2 (>= 80) is True")
            print("  Grade: B (Good)")
        elif score >= 70:
            print("  -> Condition 3 (>= 70) is True")
            print("  Grade: C (Satisfactory)")
        elif score >= 60:
            print("  -> Condition 4 (>= 60) is True")
            print("  Grade: D (Passing)")
        else:
            print("  -> All conditions are False")
            print("  Grade: F (Failing)")

    classify_grade(95)
    classify_grade(85)
    classify_grade(75)
    classify_grade(65)
    classify_grade(50)

    # Membership status example
    print("\n--- User Membership Status (Multiple Paths) ---")

    def get_discount(membership_level):
        print(f"\nMembership: '{membership_level}'")
        if membership_level == "gold":
            print("  -> Condition 1 (== 'gold') is True")
            print("  Discount: 20%")
        elif membership_level == "silver":
            print("  -> Condition 2 (== 'silver') is True")
            print("  Discount: 10%")
        elif membership_level == "bronze":
            print("  -> Condition 3 (== 'bronze') is True")
            print("  Discount: 5%")
        else:
            print("  -> All conditions are False")
            print("  Discount: 0% (No membership)")

    get_discount("gold")
    get_discount("silver")
    get_discount("bronze")
    get_discount("none")


def demonstrate_logical_operators():
    """
    Demonstrate use of logical operators (and, or, not).
    """
    print("\n" + "=" * 60)
    print("4. LOGICAL OPERATORS (and, or, not)")
    print("=" * 60)

    # AND operator (both conditions must be True)
    print("\n--- Logical AND (Both conditions must be True) ---")

    age = 25
    has_license = True
    print(f"age = {age}, has_license = {has_license}")
    print(f"Condition: if age >= 18 and has_license:")

    if age >= 18 and has_license:
        print("[OK] Both conditions are True: Can drive")
    else:
        print("[FAIL] At least one condition is False: Cannot drive")

    print()

    age = 16
    has_license = True
    print(f"age = {age}, has_license = {has_license}")
    print(f"Condition: if age >= 18 and has_license:")

    if age >= 18 and has_license:
        print("[OK] Both conditions are True: Can drive")
    else:
        print("[FAIL] At least one condition is False: Cannot drive")

    # OR operator (at least one condition must be True)
    print("\n--- Logical OR (At least one condition must be True) ---")

    is_weekend = True
    is_holiday = False
    print(f"is_weekend = {is_weekend}, is_holiday = {is_holiday}")
    print(f"Condition: if is_weekend or is_holiday:")

    if is_weekend or is_holiday:
        print("[OK] At least one condition is True: Day off!")
    else:
        print("[FAIL] Both conditions are False: Work day")

    print()

    is_weekend = False
    is_holiday = True
    print(f"is_weekend = {is_weekend}, is_holiday = {is_holiday}")
    print(f"Condition: if is_weekend or is_holiday:")

    if is_weekend or is_holiday:
        print("[OK] At least one condition is True: Day off!")
    else:
        print("[FAIL] Both conditions are False: Work day")

    print()

    is_weekend = False
    is_holiday = False
    print(f"is_weekend = {is_weekend}, is_holiday = {is_holiday}")
    print(f"Condition: if is_weekend or is_holiday:")

    if is_weekend or is_holiday:
        print("[OK] At least one condition is True: Day off!")
    else:
        print("[FAIL] Both conditions are False: Work day")

    # NOT operator (negates condition)
    print("\n--- Logical NOT (Negates condition) ---")

    is_available = False
    print(f"is_available = {is_available}")
    print(f"Condition: if not is_available:")

    if not is_available:
        print("[OK] NOT inverted the condition: Item is unavailable")
    else:
        print("[FAIL] Item is available")

    print()

    is_available = True
    print(f"is_available = {is_available}")
    print(f"Condition: if not is_available:")

    if not is_available:
        print("[OK] NOT inverted the condition: Item is unavailable")
    else:
        print("[FAIL] Item is available")

    # Complex combinations
    print("\n--- Complex Combinations ---")

    age = 25
    income = 50000
    credit_score = 720
    print(f"age = {age}, income = {income}, credit_score = {credit_score}")
    print(f"Condition: if age >= 21 and (income >= 30000 or credit_score >= 700):")

    if age >= 21 and (income >= 30000 or credit_score >= 700):
        print("[OK] Loan application APPROVED")
    else:
        print("[FAIL] Loan application DENIED")

    print()

    age = 19
    income = 25000
    credit_score = 650
    print(f"age = {age}, income = {income}, credit_score = {credit_score}")
    print(f"Condition: if age >= 21 and (income >= 30000 or credit_score >= 700):")

    if age >= 21 and (income >= 30000 or credit_score >= 700):
        print("[OK] Loan application APPROVED")
    else:
        print("[FAIL] Loan application DENIED")


def demonstrate_data_type_considerations():
    """
    Demonstrate common issues with data types in conditions.
    """
    print("\n" + "=" * 60)
    print("5. DATA TYPE CONSIDERATIONS (Common Pitfalls)")
    print("=" * 60)

    # String vs Integer comparison
    print("\n--- Pitfall 1: String vs Integer ---")
    user_input = "25"
    print(f"user_input = '{user_input}' (type: {type(user_input).__name__})")
    print(f"Condition: if user_input > 18:")
    print("[ERROR] This will cause a TypeError: can't compare str and int")
    print("   Solution: Convert to int first")

    print(f"\nCorrected: if int(user_input) > 18:")
    if int(user_input) > 18:
        print("[OK] Correctly converted and compared")

    # Case sensitivity in string comparison
    print("\n--- Pitfall 2: Case Sensitivity ---")
    status = "Active"
    print(f"status = '{status}'")
    print(f"Condition: if status == 'active':")

    if status == "active":
        print("[OK] Match found")
    else:
        print("[FAIL] No match (uppercase 'A' != lowercase 'a')")

    print(f"\nCorrected: if status.lower() == 'active':")
    if status.lower() == "active":
        print("[OK] Case-insensitive comparison works")

    # Whitespace in strings
    print("\n--- Pitfall 3: Whitespace in Strings ---")
    name = "Alice "
    print(f"name = '{name}' (note trailing space)")
    print(f"Condition: if name == 'Alice':")

    if name == "Alice":
        print("[OK] Match found")
    else:
        print("[FAIL] No match (extra space causes mismatch)")

    print(f"\nCorrected: if name.strip() == 'Alice':")
    if name.strip() == "Alice":
        print("[OK] Whitespace removed, match found")

    # False vs 0 vs empty string
    print("\n--- Pitfall 4: Falsy Values ---")
    print("Python has multiple 'falsy' values: False, 0, '', [], None")

    value = 0
    print(f"\nvalue = {value}")
    print(f"Condition: if value:")
    if value:
        print("[OK] Truthy")
    else:
        print("[FAIL] Falsy (0 is falsy in Python)")

    value = ""
    print(f"\nvalue = '{value}' (empty string)")
    print(f"Condition: if value:")
    if value:
        print("[OK] Truthy")
    else:
        print("[FAIL] Falsy (empty string is falsy)")

    # Operator precedence
    print("\n--- Pitfall 5: Operator Precedence ---")
    x = 5
    y = 10
    z = 15
    print(f"x = {x}, y = {y}, z = {z}")
    print(f"Condition: if x < y < z:")

    if x < y < z:
        print("[OK] Python chains comparisons left to right: (x < y) and (y < z)")
    else:
        print("[FAIL] Not satisfied")


def demonstrate_practical_scenarios():
    """
    Practical scenarios combining conditional logic.
    """
    print("\n" + "=" * 60)
    print("6. PRACTICAL SCENARIOS")
    print("=" * 60)

    # E-commerce order validation
    print("\n--- E-commerce Order Validation ---")

    def validate_order(total_price, quantity, is_member):
        print(f"\nOrder Details:")
        print(f"  Total Price: ${total_price}")
        print(f"  Quantity: {quantity}")
        print(f"  Is Member: {is_member}")

        if total_price < 0:
            print("  [FAIL] Invalid: Negative price")
            return False
        elif quantity <= 0:
            print("  [FAIL] Invalid: Quantity must be positive")
            return False
        elif total_price > 1000 and not is_member:
            print("  [FAIL] Invalid: High-value orders require membership")
            return False
        else:
            print("  [OK] Valid order")
            return True

    validate_order(50.00, 2, False)
    validate_order(1500.00, 5, False)
    validate_order(1500.00, 5, True)
    validate_order(100.00, -2, False)

    # User access control
    print("\n--- User Access Control ---")

    def check_access(user_role, action, is_authenticated):
        print(f"\nAccess Request:")
        print(f"  Role: {user_role}")
        print(f"  Action: {action}")
        print(f"  Authenticated: {is_authenticated}")

        if not is_authenticated:
            print("  [FAIL] ACCESS DENIED: Not authenticated")
        elif user_role == "admin":
            print("  [OK] ACCESS ALLOWED: Admin")
        elif user_role == "editor" and action in ["read", "write"]:
            print("  [OK] ACCESS ALLOWED: Editor can read/write")
        elif user_role == "viewer" and action == "read":
            print("  [OK] ACCESS ALLOWED: Viewer can read")
        else:
            print(f"  [FAIL] ACCESS DENIED: {user_role} cannot {action}")

    check_access("admin", "delete", True)
    check_access("editor", "write", True)
    check_access("viewer", "delete", True)
    check_access("editor", "delete", False)

    # Product eligibility
    print("\n--- Product Eligibility ---")

    def recommend_product(age, income, credit_score):
        print(f"\nUser Profile:")
        print(f"  Age: {age}")
        print(f"  Income: ${income}")
        print(f"  Credit Score: {credit_score}")

        if age < 18:
            print("  [WARNING] Not eligible: Must be 18+")
        elif income < 30000 and credit_score < 650:
            print("  [WARNING] Not eligible: Low income and credit score")
        elif income >= 100000 and credit_score >= 750:
            print("  [OK] PREMIUM products available")
        elif income >= 50000 or credit_score >= 700:
            print("  [OK] STANDARD products available")
        else:
            print("  [OK] BASIC products available")

    recommend_product(25, 120000, 780)
    recommend_product(22, 55000, 680)
    recommend_product(20, 40000, 750)
    recommend_product(17, 80000, 800)


def demonstrate_debugging_conditions():
    """
    Demonstrate how to debug conditions that don't work as expected.
    """
    print("\n" + "=" * 60)
    print("7. DEBUGGING: Condition Always False?")
    print("=" * 60)

    print("\n--- Common Mistake 1: Using = instead of == ---")
    print("[ERROR] Wrong:")
    print("   if x = 5:")
    print("      SyntaxError: invalid syntax")
    print("\n[OK] Correct:")
    x = 5
    if x == 5:
        print("   if x == 5: [OK] Works")

    print("\n--- Common Mistake 2: Type Mismatch ---")
    print("[ERROR] Wrong:")
    value = "100"
    print(f"   value = '{value}' (string)")
    print(f"   if value > 50: -> TypeError")
    print("\n[OK] Correct:")
    if int(value) > 50:
        print(f"   if int(value) > 50: -> True [OK]")

    print("\n--- Common Mistake 3: Case Sensitivity ---")
    print("[ERROR] Wrong:")
    status = "Active"
    print(f"   status = '{status}'")
    print(f"   if status == 'active': -> False")
    print("\n[OK] Correct:")
    if status.lower() == "active":
        print(f"   if status.lower() == 'active': -> True [OK]")

    print("\n--- Common Mistake 4: Condition Order ---")
    print("[ERROR] Wrong (first condition catches everything):")
    print("   if age >= 0:")
    print("       print('Allow')")
    print("   elif age >= 18:")
    print("       print('Adult') -> Never reached!")
    print("\n[OK] Correct (specific conditions first):")
    age = 25
    if age >= 18:
        print("   if age >= 18: -> Adult")
    elif age >= 0:
        print("   elif age >= 0: (only reached if age < 18)")

    print("\n--- Common Mistake 5: Logical Operator Confusion ---")
    print("[ERROR] Wrong:")
    print("   if role == 'admin' or 'user':")
    print("       Always True! ('user' string is truthy)")
    print("\n[OK] Correct:")
    role = "viewer"
    if role == "admin" or role == "user":
        print(f"   if role == 'admin' or role == 'user': -> False [OK]")

    print("\n--- Debugging Tip: Print the values and condition ---")
    print("[OK] Use print() to debug:")
    user_age = 16
    print(f"   user_age = {user_age}")
    print(f"   user_age >= 18? {user_age >= 18}")
    if user_age >= 18:
        print("   [OK] Condition is True")
    else:
        print("   [OK] Can see why condition is False")


if __name__ == "__main__":
    print("\n" + "*" * 60)
    print("PYTHON CONDITIONAL STATEMENTS DEMONSTRATION")
    print("*" * 60)

    demonstrate_basic_if()
    demonstrate_if_else()
    demonstrate_if_elif_else()
    demonstrate_logical_operators()
    demonstrate_data_type_considerations()
    demonstrate_practical_scenarios()
    demonstrate_debugging_conditions()

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("[OK] if: Single condition, no alternative")
    print("[OK] if-else: Two branches, one executes")
    print("[OK] if-elif-else: Multiple branches, first True executes")
    print("[OK] and: Both conditions must be True")
    print("[OK] or: At least one condition must be True")
    print("[OK] not: Inverts the condition")
    print("[OK] Always check data types before comparison")
    print("[OK] Remember: Order matters in if-elif-else chains")
    print("[OK] Use print() to debug unexpected condition behavior")
    print("\n")
