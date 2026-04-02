"""
=====================================================================
MILESTONE 8: STRUCTURING PYTHON CODE FOR READABILITY AND REUSE
=====================================================================

This script demonstrates:
1. Before/after: monolithic vs structured code
2. Clear section organization (imports, setup, functions, main)
3. Function extraction to avoid code duplication
4. Logical code organization patterns
5. Single responsibility principle
6. Data flow through organized functions
7. Execution flow and entry points
8. Common structural mistakes and how to fix them
9. Best practices for code organization

Focus: Clean, maintainable code that's easy to understand and extend.
=====================================================================
"""

# =====================================================================
# SECTION 1: BEFORE/AFTER - MONOLITHIC VS STRUCTURED CODE
# =====================================================================

def demonstrate_monolithic_vs_structured():
    """
    Show how monolithic (unstructured) code compares to organized code.
    """
    print("\n" + "="*70)
    print("SECTION 1: BEFORE/AFTER - MONOLITHIC VS STRUCTURED CODE")
    print("="*70)
    
    print("\n--- MONOLITHIC CODE (BAD) ---")
    print("Everything crammed into one place, hard to follow:")
    print()
    
    monolithic = """
# MONOLITHIC SCRIPT - Everything jumbled together
users = []
user = {"name": "alice", "age": 28, "email": "alice@example.com"}
users.append(user)
user = {"name": "bob", "age": 35, "email": "bob@example.com"}
users.append(user)

for u in users:
    if "@" in u["email"]:
        valid = True
    else:
        valid = False
    
    if valid:
        print(f"User: {u['name']}, Email: {u['email']}")
    
    if u["age"] > 30:
        print(f"  {u['name']} is older than 30")

print(f"Total users: {len(users)}")
years_sum = 0
for u in users:
    years_sum += u["age"]
avg_age = years_sum / len(users)
print(f"Average age: {avg_age}")
    """
    
    print(monolithic)
    print()
    print("PROBLEMS:")
    print("  - Logic is scattered throughout")
    print("  - If you want to reuse email validation elsewhere, tough luck")
    print("  - Hard to tell what the script does (many mixed concerns)")
    print("  - Changes to age calculation require hunting through the code")
    print("  - Testing individual pieces is impossible")
    print("  - Impossible to understand flow at a glance")
    
    print("\n--- STRUCTURED CODE (GOOD) ---")
    print("Organized, clear flow, reusable functions:")
    print()
    
    structured = """
# STRUCTURED SCRIPT - clear organization and flow

# 1. IMPORTS (at top)
# (none in this example, but would go here)

# 2. HELPER FUNCTIONS (extracting logic)
def is_valid_email(email):
    '''Check if email is valid (contains @).'''
    return "@" in email

def is_senior(age, threshold=30):
    '''Check if age exceeds threshold.'''
    return age > threshold

def calculate_average_age(users):
    '''Calculate average age of users.'''
    if not users:
        return 0
    total = sum(user["age"] for user in users)
    return total / len(users)

# 3. DATA SETUP
def initialize_users():
    '''Create and return list of users.'''
    users = [
        {"name": "alice", "age": 28, "email": "alice@example.com"},
        {"name": "bob", "age": 35, "email": "bob@example.com"},
    ]
    return users

# 4. MAIN PROCESSING LOGIC
def process_users(users):
    '''Process and display user information.'''
    for user in users:
        # Only process valid emails
        if is_valid_email(user["email"]):
            print(f"User: {user['name']}, Email: {user['email']}")
            
            # Check if senior
            if is_senior(user["age"]):
                print(f"  {user['name']} is older than 30")

# 5. REPORTING
def display_statistics(users):
    '''Display user statistics.'''
    average_age = calculate_average_age(users)
    print(f"Total users: {len(users)}")
    print(f"Average age: {average_age:.1f}")

# 6. MAIN ENTRY POINT
if __name__ == "__main__":
    users = initialize_users()
    process_users(users)
    display_statistics(users)
    """
    
    print(structured)
    print()
    print("BENEFITS:")
    print("  - Functions are reusable (is_valid_email used anywhere)")
    print("  - Structure is immediately clear")
    print("  - Each function does one thing")
    print("  - Easy to test individual functions")
    print("  - Easy to read from top to bottom (intent is obvious)")
    print("  - Easy to modify (age threshold? Change one parameter)")
    
    print("\n--- Organization Comparison ---")
    print("MONOLITHIC:")
    print("  - Read file top to bottom: lost in the details")
    print("  - Find feature: hunt through mixed logic")
    print("  - Reuse logic: copy/paste everywhere")
    print("  - Test feature: can't isolate it")
    print()
    print("STRUCTURED:")
    print("  - Read file: understand at a glance (has sections)")
    print("  - Find feature: go to the relevant function")
    print("  - Reuse logic: call the function")
    print("  - Test feature: test the function in isolation")


# =====================================================================
# SECTION 2: CLEAR SECTION ORGANIZATION
# =====================================================================

def demonstrate_section_organization():
    """
    Show the recommended Python file structure.
    """
    print("\n" + "="*70)
    print("SECTION 2: CLEAR SECTION ORGANIZATION")
    print("="*70)
    
    print("\n--- Standard Python File Structure ---")
    print()
    print("1. MODULE DOCSTRING")
    print("   - What does this file do?")
    print("   - Brief description at the top")
    print()
    print('   Example:')
    print('   """')
    print('   User management script.')
    print('   Handles user data loading, validation, and reporting.')
    print('   """')
    print()
    
    print("2. IMPORTS (all at top)")
    print("   - Standard library imports first")
    print("   - Then third-party imports")
    print("   - Then local imports")
    print()
    print("   Example:")
    print("   import os")
    print("   import sys")
    print("   import json")
    print("   import pandas as pd")
    print("   from my_module import helper_function")
    print()
    
    print("3. CONSTANTS (uppercase names)")
    print("   - Configuration values")
    print("   - Settings that might need change")
    print()
    print("   Example:")
    print("   MAX_USERS = 1000")
    print('   DATABASE_URL = "localhost:5432"')
    print("   VALID_STATUSES = ['active', 'inactive']")
    print()
    
    print("4. HELPER FUNCTIONS (small, focused functions)")
    print("   - Utility functions used by main logic")
    print("   - Validation functions")
    print("   - Data transformation functions")
    print()
    print("   Example:")
    print("   def is_valid_email(email):")
    print("       return '@' in email")
    print()
    
    print("5. MAIN FUNCTIONS (larger orchestration functions)")
    print("   - Primary logic of the script")
    print("   - Functions that coordinate other functions")
    print()
    print("   Example:")
    print("   def process_all_users(users):")
    print("       for user in users:")
    print("           validate_user(user)")
    print()
    
    print("6. EXECUTION (if __name__ == '__main__':)")
    print("   - Script entry point")
    print("   - Only code that should run when script is executed")
    print("   - NOT run when imported as module elsewhere")
    print()
    print("   Example:")
    print("   if __name__ == '__main__':")
    print("       main()")
    print()
    
    print("--- Why This Order? ---")
    print()
    print("  1. Docstring: Reader knows what file does immediately")
    print("  2. Imports: Dependencies are clear upfront")
    print("  3. Constants: Config values gathered in one place")
    print("  4. Helpers: Small functions first (foundations)")
    print("  5. Main: Complex functions that build on helpers")
    print("  6. Execution: Entry point at the bottom calls main()")
    print()
    print("When you read the file top-to-bottom:")
    print("  - You understand dependencies")
    print("  - You see building blocks")
    print("  - You see high-level flow at the bottom")
    print("  - Everything is in logical order")


# =====================================================================
# SECTION 3: FUNCTION EXTRACTION TO AVOID DUPLICATION
# =====================================================================

def demonstrate_function_extraction():
    """
    Show how to identify and extract repeated code into functions.
    """
    print("\n" + "="*70)
    print("SECTION 3: FUNCTION EXTRACTION TO AVOID DUPLICATION")
    print("="*70)
    
    print("\n--- DUPLICATED CODE (BAD) ---")
    print("Same logic repeated multiple times:")
    print()
    
    print("# Send email to alice")
    print("email = 'alice@example.com'")
    print("if '@' not in email:")
    print("    print('Invalid email')")
    print("else:")
    print("    print(f'Sending to {email}')")
    print()
    print("# Send email to bob")
    print("email = 'bob@example.com'")
    print("if '@' not in email:")
    print("    print('Invalid email')")
    print("else:")
    print("    print(f'Sending to {email}')")
    print()
    print("# Send email to charlie")
    print("email = 'charlie@example.com'")
    print("if '@' not in email:")
    print("    print('Invalid email')")
    print("else:")
    print("    print(f'Sending to {email}')")
    print()
    print("PROBLEMS:")
    print("  - Same code written 3 times (or more)")
    print("  - If you fix a bug, must fix it 3 places")
    print("  - Hard to see the overall logic (lost in repetition)")
    print("  - Adding a new email means copy/paste again")
    
    print("\n--- EXTRACTED FUNCTION (GOOD) ---")
    print()
    
    print("def send_email(email):")
    print("    '''Send email if valid, otherwise report error.'''")
    print("    if '@' not in email:")
    print("        print('Invalid email')")
    print("    else:")
    print("        print(f'Sending to {email}')")
    print()
    print("# Use the function repeatedly")
    print("send_email('alice@example.com')")
    print("send_email('bob@example.com')")
    print("send_email('charlie@example.com')")
    print()
    print("# Or loop over a list")
    print("emails = ['alice@example.com', 'bob@example.com', 'charlie@example.com']")
    print("for email in emails:")
    print("    send_email(email)")
    print()
    print("BENEFITS:")
    print("  - Write logic once, use many times")
    print("  - Fix bug in one place")
    print("  - Easy to see the flow (loop + function call)")
    print("  - Easy to add new emails (just extend list)")
    
    print("\n--- Pattern Recognition: When to Extract a Function ---")
    print()
    
    patterns = [
        ("Code appears 2+ times", "Extract to function, call multiple times"),
        ("Logic answers one question", "Extract to function with clear name"),
        ("Always used with similar steps", "Extract to function that handles flow"),
        ("Hard to understand at a glance", "Extract helper function for clarity"),
        ("Want to test it in isolation", "Extract to function, write unit test"),
    ]
    
    for trigger, action in patterns:
        print(f"  [TRIGGER] {trigger}")
        print(f"  [ACTION]  {action}")
        print()


# =====================================================================
# SECTION 4: LOGICAL CODE ORGANIZATION PATTERNS
# =====================================================================

def demonstrate_organization_patterns():
    """
    Show different ways to organize code logically.
    """
    print("\n" + "="*70)
    print("SECTION 4: LOGICAL CODE ORGANIZATION PATTERNS")
    print("="*70)
    
    print("\n--- Pattern 1: Load -> Process -> Report ---")
    print()
    
    print("def load_data():")
    print("    '''Load and prepare data.'''")
    print("    return [...data...]")
    print()
    print("def process_data(data):")
    print("    '''Apply business logic to data.'''")
    print("    return [...results...]")
    print()
    print("def report_results(results):")
    print("    '''Display or save results.'''")
    print("    print(...)")
    print()
    print("if __name__ == '__main__':")
    print("    data = load_data()")
    print("    results = process_data(data)")
    print("    report_results(results)")
    print()
    print("FLOW: Input -> Transform -> Output")
    print("BENEFIT: Clear pipeline, each step is independent")
    
    print("\n--- Pattern 2: Setup -> Validate -> Execute ---")
    print()
    
    print("def setup_configuration():")
    print("    '''Initialize config and settings.'''")
    print("    return {...config...}")
    print()
    print("def validate_inputs(config):")
    print("    '''Check that inputs are valid.'''")
    print("    return config_is_valid")
    print()
    print("def execute_main_logic(config):")
    print("    '''Run the main business logic.'''")
    print("    return result")
    print()
    print("if __name__ == '__main__':")
    print("    config = setup_configuration()")
    print("    if validate_inputs(config):")
    print("        result = execute_main_logic(config)")
    print("    else:")
    print("        print('Invalid config')")
    print()
    print("FLOW: Initialize -> Verify -> Execute")
    print("BENEFIT: Fail fast on invalid config, clear guard clause")
    
    print("\n--- Pattern 3: Helper Functions + Main Handler ---")
    print()
    
    print("def validate_email(email):")
    print("    '''Helper: check email validity.'''")
    print("    return '@' in email")
    print()
    print("def format_user_info(user):")
    print("    '''Helper: format user for display.'''")
    print("    return f\"{user['name']} ({user['email']})\"")
    print()
    print("def handle_user(user):")
    print("    '''Main handler: validate and format user.'''")
    print("    if validate_email(user['email']):")
    print("        return format_user_info(user)")
    print("    return None")
    print()
    print("FLOW: Small helpers -> Medium handler -> Use in main")
    print("BENEFIT: Composable, testable, reusable")
    
    print("\n--- Pattern 4: Configuration + Business Logic + Reporting ---")
    print()
    
    print("# CONFIG")
    print("RETRY_ATTEMPTS = 3")
    print("TIMEOUT_SECONDS = 30")
    print()
    print("# HELPERS")
    print("def attempt_operation(data):")
    print("    '''Try operation with retries.'''")
    print("    for attempt in range(RETRY_ATTEMPTS):")
    print("        try:")
    print("            return process(data)")
    print("        except Exception:")
    print("            if attempt == RETRY_ATTEMPTS - 1:")
    print("                raise")
    print()
    print("# REPORTING")
    print("def show_completion_status(success, errors):")
    print("    '''Display completion status.'''")
    print("    print(...)")
    print()
    print("FLOW: Config -> Logic -> Report")
    print("BENEFIT: Config separated, logic isolated, reporting clean")


# =====================================================================
# SECTION 5: SINGLE RESPONSIBILITY PRINCIPLE
# =====================================================================

def demonstrate_single_responsibility():
    """
    Show how each function should have one clear purpose.
    """
    print("\n" + "="*70)
    print("SECTION 5: SINGLE RESPONSIBILITY PRINCIPLE")
    print("="*70)
    
    print("\n--- MULTIPLE RESPONSIBILITIES (BAD) ---")
    print("One function trying to do everything:")
    print()
    
    print("def process_user_order(user, order):")
    print("    # Validate user (responsibility 1)")
    print("    if not user['email'] or '@' not in user['email']:")
    print("        return False")
    print("    ")
    print("    # Calculate total (responsibility 2)")
    print("    total = sum(item['price'] for item in order['items'])")
    print("    tax = total * 0.1")
    print("    final = total + tax")
    print("    ")
    print("    # Send notification (responsibility 3)")
    print("    print(f\"Order {order['id']} for {user['name']}: ${final}\")")
    print("    ")
    print("    # Save to database (responsibility 4)")
    print("    # database.save(...)")
    print("    ")
    print("    return True")
    print()
    print("PROBLEMS:")
    print("  - Testing: Can't test validation without side effects")
    print("  - Reuse: Can't reuse calculation without notification")
    print("  - Maintenance: Bug in notification breaks validation")
    print("  - Understanding: Hard to see what function really does")
    print("  - Change control: Changing notification affects everything")
    
    print("\n--- SINGLE RESPONSIBILITY (GOOD) ---")
    print("Each function does ONE thing well:")
    print()
    
    print("def is_valid_user(user):")
    print("    '''Validate user data (ONE responsibility).'''")
    print("    return user.get('email') and '@' in user['email']")
    print()
    print("def calculate_order_total(order):")
    print("    '''Calculate order total with tax (ONE responsibility).'''")
    print("    subtotal = sum(item['price'] for item in order['items'])")
    print("    return subtotal * 1.1  # 10% tax")
    print()
    print("def send_order_notification(order, user, total):")
    print("    '''Send order notification (ONE responsibility).'''")
    print("    print(f\"Order {order['id']} for {user['name']}: ${total}\")")
    print()
    print("def save_order_to_database(order):")
    print("    '''Save order to database (ONE responsibility).'''")
    print("    # database.save(order)")
    print("    pass")
    print()
    print("def process_user_order(user, order):")
    print("    '''Orchestrate order processing (ONE responsibility: coordination).'''")
    print("    if not is_valid_user(user):")
    print("        return False")
    print("    ")
    print("    total = calculate_order_total(order)")
    print("    send_order_notification(order, user, total)")
    print("    save_order_to_database(order)")
    print("    return True")
    print()
    print("BENEFITS:")
    print("  - Test validation independently")
    print("  - Reuse calculation elsewhere")
    print("  - Change notification without affecting logic")
    print("  - Each function is clearly understandable")
    print("  - Easy to change one responsibility without cascade")
    
    print("\n--- Single Responsibility Test ---")
    print()
    print("Ask yourself: 'If this function needed to change,")
    print("how many reasons could cause that change?'")
    print()
    print("MULTIPLE reasons = Multiple responsibilities (refactor!)")
    print("ONE reason = Single responsibility (good!)")


# =====================================================================
# SECTION 6: DATA FLOW THROUGH ORGANIZED FUNCTIONS
# =====================================================================

def demonstrate_data_flow():
    """
    Show how data flows through a well-organized system.
    """
    print("\n" + "="*70)
    print("SECTION 6: DATA FLOW THROUGH ORGANIZED FUNCTIONS")
    print("="*70)
    
    print("\n--- Example: Student Grade Processing System ---")
    print()
    
    print("# STEP 1: Validate raw data")
    print("def validate_student_record(record):")
    print("    '''Validate that record has required fields.'''")
    print("    required = ['name', 'grade', 'subject']")
    print("    return all(field in record for field in required)")
    print()
    
    print("# STEP 2: Transform/normalize")
    print("def normalize_grade(grade_raw):")
    print("    '''Convert grade to standard format.'''")
    print("    grade_numeric = float(grade_raw)")
    print("    return max(0, min(100, grade_numeric))  # Clamp to 0-100")
    print()
    
    print("# STEP 3: Apply business logic")
    print("def calculate_letter_grade(numeric_grade):")
    print("    '''Convert numeric grade to letter grade.'''")
    print("    if numeric_grade >= 90:")
    print("        return 'A'")
    print("    elif numeric_grade >= 80:")
    print("        return 'B'")
    print("    # ... etc")
    print()
    
    print("# STEP 4: Aggregate/report")
    print("def create_report_entry(record, letter_grade):")
    print("    '''Create formatted report entry.'''")
    print("    return {")
    print("        'name': record['name'],")
    print("        'subject': record['subject'],")
    print("        'grade': letter_grade,")
    print("    }")
    print()
    
    print("# STEP 5: Process all")
    print("def process_all_records(records):")
    print("    '''Process all records through pipeline.'''")
    print("    results = []")
    print("    for record in records:")
    print("        if not validate_student_record(record):")
    print("            continue  # Skip invalid")
    print("        ")
    print("        normalized = normalize_grade(record['grade'])")
    print("        letter = calculate_letter_grade(normalized)")
    print("        entry = create_report_entry(record, letter)")
    print("        results.append(entry)")
    print("    ")
    print("    return results")
    print()
    
    print("# DATA FLOW DIAGRAM:")
    print()
    print("RAW DATA")
    print("  |")
    print("  v")
    print("validate_student_record() -> FILTERED")
    print("  |")
    print("  v")
    print("normalize_grade() -> NORMALIZED")
    print("  |")
    print("  v")
    print("calculate_letter_grade() -> TRANSFORMED")
    print("  |")
    print("  v")
    print("create_report_entry() -> FORMATTED")
    print("  |")
    print("  v")
    print("REPORT RESULTS")
    print()
    print("Each step:")
    print("  - Takes input")
    print("  - Does ONE thing")
    print("  - Returns output for next step")
    print("  - Can be tested independently")
    print("  - Can be reused elsewhere")


# =====================================================================
# SECTION 7: EXECUTION FLOW AND ENTRY POINTS
# =====================================================================

def demonstrate_execution_flow():
    """
    Show the importance of clear execution flow and main entry points.
    """
    print("\n" + "="*70)
    print("SECTION 7: EXECUTION FLOW AND ENTRY POINTS")
    print("="*70)
    
    print("\n--- THE __main__ GUARD CLAUSE ---")
    print()
    
    print("Why use: if __name__ == '__main__': ?")
    print()
    print("When you run a Python file directly:")
    print("  python my_script.py")
    print("  __name__ is set to '__main__'")
    print()
    print("When you import it as a module:")
    print("  from my_script import some_function")
    print("  __name__ is set to 'my_script'")
    print()
    print("BENEFIT: Same file can be used as script OR library!")
    print()
    
    print("--- Bad Practice: No Guard Clause ---")
    print()
    print("# my_data_processor.py")
    print("data = load_data()  # Runs immediately when imported!")
    print("result = process(data)")
    print("print(result)")
    print()
    print("When you import:")
    print("  from my_data_processor import load_data")
    print("PROBLEM: load_data() is called immediately!")
    print("         Side effects happen when you just wanted to import")
    print()
    
    print("--- Good Practice: With Guard Clause ---")
    print()
    print("# my_data_processor.py")
    print("def load_data():")
    print("    ...")
    print()
    print("def main():")
    print("    data = load_data()")
    print("    result = process(data)")
    print("    print(result)")
    print()
    print("if __name__ == '__main__':")
    print("    main()")
    print()
    print("When you import:")
    print("  from my_data_processor import load_data")
    print("BENEFIT: Only load_data is available, main() doesn't run!")
    print()
    
    print("--- Entry Point Design ---")
    print()
    print("Good main() function:")
    print()
    print("def main():")
    print("    '''Script entry point. Coordinate high-level flow.'''")
    print("    config = load_configuration()")
    print("    ")
    print("    if not validate_config(config):")
    print("        print('Error: Invalid configuration')")
    print("        return")
    print("    ")
    print("    data = load_data(config)")
    print("    results = process_data(data)")
    print("    save_results(results)")
    print("    print('Success')")
    print()
    print("BENEFITS:")
    print("  - main() is easy to understand (big picture)")
    print("  - Error handling at top level")
    print("  - Can modify flow easily")
    print("  - Functions below are all reusable")


# =====================================================================
# SECTION 8: COMMON STRUCTURAL MISTAKES
# =====================================================================

def demonstrate_common_mistakes():
    """
    Show common code organization mistakes and their fixes.
    """
    print("\n" + "="*70)
    print("SECTION 8: COMMON STRUCTURAL MISTAKES")
    print("="*70)
    
    print("\n--- Mistake 1: No Separation of Imports and Code ---")
    print()
    
    print("BAD:")
    print("import json")
    print("data = json.loads(...)")
    print("import pandas  # Import in middle of code!")
    print("df = pandas.read_csv(...)")
    print()
    print("GOOD:")
    print("import json")
    print("import pandas")
    print("")
    print("data = json.loads(...)")
    print("df = pandas.read_csv(...)")
    print()
    print("WHY: All imports at top make dependencies clear upfront")
    
    print("\n--- Mistake 2: Global State Modified Everywhere ---")
    print()
    
    print("BAD:")
    print("results = []  # Global variable")
    print("")
    print("def process_record(record):")
    print("    results.append(...)  # Modifies global - hard to track")
    print("")
    print("def filter_results():")
    print("    results[:] = [r for r in results if r['valid']]  # Modifies again")
    print("    # Where was it modified? Hard to debug")
    print()
    print("GOOD:")
    print("def process_record(record):")
    print("    return {...processed...}  # Returns value don't modify global")
    print("")
    print("def filter_results(results):")
    print("    return [r for r in results if r['valid']]  # Returns new list")
    print("")
    print("if __name__ == '__main__':")
    print("    results = []")
    print("    results.append(process_record(...))")
    print("    results = filter_results(results)")
    print()
    print("WHY: Data flow is explicit and testable")
    
    print("\n--- Mistake 3: One Huge Function Doing Everything ---")
    print()
    
    print("BAD:")
    print("def do_everything():")
    print("    # Validation (10 lines)")
    print("    # Data transformation (15 lines)")
    print("    # Calculation (20 lines)")
    print("    # Error handling (10 lines)")
    print("    # Reporting (10 lines)")
    print("    # = 65 line function that's impossible to understand")
    print()
    print("GOOD:")
    print("def validate_data(data):")
    print("    ...")
    print("")
    print("def transform_data(data):")
    print("    ...")
    print("")
    print("def calculate_results(data):")
    print("    ...")
    print("")
    print("def handle_errors(func, data):")
    print("    ...")
    print("")
    print("def report_results(results):")
    print("    ...")
    print("")
    print("def main():")
    print("    data = load_data()")
    print("    data = validate_data(data)")
    print("    data = transform_data(data)")
    print("    results = calculate_results(data)")
    print("    report_results(results)")
    print()
    print("WHY: Each function is understandable; main() shows flow")
    
    print("\n--- Mistake 4: No Comments on Complex Sections ---")
    print()
    
    print("BAD:")
    print("def calculate_price(base, customer_type, quantity):")
    print("    if customer_type == 'A':")
    print("        m = 0.1")
    print("    elif customer_type == 'B':")
    print("        m = 0.05")
    print("    else:")
    print("        m = 0")
    print("    p = base * (1 - m)")
    print("    if quantity > 100:")
    print("        p *= 0.95")
    print("    return p")
    print()
    print("GOOD:")
    print("def calculate_price(base, customer_type, quantity):")
    print("    # Customer loyalty discount")
    print("    if customer_type == 'A':")
    print("        discount = 0.1  # Premium: 10%")
    print("    elif customer_type == 'B':")
    print("        discount = 0.05  # Standard: 5%")
    print("    else:")
    print("        discount = 0  # New: 0%")
    print("    ")
    print("    discounted_price = base * (1 - discount)")
    print("    ")
    print("    # Bulk discount: orders over 100 units get 5% additional")
    print("    if quantity > 100:")
    print("        discounted_price *= 0.95")
    print("    ")
    print("    return discounted_price")
    print()
    print("WHY: Or better: extract helper functions to remove need for comments")


# =====================================================================
# SECTION 9: BEST PRACTICES FOR CODE ORGANIZATION
# =====================================================================

def demonstrate_best_practices():
    """
    Summary of best practices for well-structured code.
    """
    print("\n" + "="*70)
    print("SECTION 9: BEST PRACTICES FOR CODE ORGANIZATION")
    print("="*70)
    
    print("\n--- Golden Rules for Code Structure ---")
    print()
    
    rules = [
        ("Organize like a newspaper",
         "Most important stuff first, details later\nReader should understand scope immediately"),
        
        ("One reason to change = one function",
         "Single Responsibility Principle\nEach function has ONE and only ONE job"),
        
        ("Functions should be small",
         "Aim for 5-15 lines\nIf it's over 30 lines, probably needs to split"),
        
        ("Data flows in and out",
         "Functions should take parameters and return values\nAvoid global state when possible"),
        
        ("Use guard clauses early",
         "if not valid: return early\nReduces nesting and makes flow clearer"),
        
        ("DRY: Don't Repeat Yourself",
         "Write once, reuse many times\nIf code appears twice, extract to function"),
        
        ("Make the implicit explicit",
         "Use descriptive names and comments\nCode is read far more than written"),
        
        ("Test-friendly structure",
         "Organize code so functions can be tested\nIf untestable, probably poorly structured"),
        
        ("Imports at top, code below",
         "Dependencies clear upfront\nEasy to see what modules are needed"),
        
        ("Main entry point is obvious",
         "Use if __name__ == '__main__': and main()\nReader knows where script starts"),
    ]
    
    for i, (rule, explanation) in enumerate(rules, 1):
        print(f"  {i}. {rule}")
        print(f"     {explanation}")
        print()


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "MILESTONE 8: STRUCTURING CODE FOR READABILITY & REUSE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    demonstrate_monolithic_vs_structured()
    demonstrate_section_organization()
    demonstrate_function_extraction()
    demonstrate_organization_patterns()
    demonstrate_single_responsibility()
    demonstrate_data_flow()
    demonstrate_execution_flow()
    demonstrate_common_mistakes()
    demonstrate_best_practices()
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Organize code: imports, constants, helpers, main, execution")
    print("  • Extract functions to avoid duplication")
    print("  • Each function should have single, clear responsibility")
    print("  • Data flows through functions: input -> process -> output")
    print("  • Use if __name__ == '__main__': for clear entry point")
    print("  • Well-structured code is easier to understand and reuse")
    print("  • Maintainability is as important as correctness")
    print("\n")
