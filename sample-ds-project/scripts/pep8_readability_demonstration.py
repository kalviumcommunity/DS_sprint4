"""
=====================================================================
MILESTONE 7: WRITING READABLE VARIABLE NAMES AND COMMENTS (PEP8 BASICS)
=====================================================================

This script demonstrates:
1. Clear, descriptive variable names vs vague alternatives
2. Consistency with snake_case naming
3. Meaningful comments that explain intent
4. Avoiding redundant or misleading comments
5. PEP 8 basics for readability
6. Before/after refactoring examples
7. Code formatting and consistency
8. Variable naming for different data types
9. Comment best practices

Focus: Code readability for human understanding and collaboration.
=====================================================================
"""

# =====================================================================
# SECTION 1: VARIABLE NAMING - CLEAR VS VAGUE
# =====================================================================

def demonstrate_variable_naming_clarity():
    """
    Show the difference between clear and vague variable names.
    """
    print("\n" + "="*70)
    print("SECTION 1: VARIABLE NAMING - CLEAR VS VAGUE")
    print("="*70)
    
    print("\n--- VAGUE NAMING (BAD) ---")
    print("Code that's hard to understand:")
    print()
    
    # Bad variable names
    n = 25
    r = 0.05
    t = 12
    a = n * (1 + r) ** t
    
    print("n = 25")
    print("r = 0.05")
    print("t = 12")
    print("a = n * (1 + r) ** t")
    print(f"a = {a:.2f}")
    print()
    print("Questions a reviewer might ask:")
    print("  - What is n? A count? A price?")
    print("  - What is r? A rate? A ratio?")
    print("  - What is t? Time? Temperature?")
    print("  - What is a? An answer? An amount?")
    print("PROBLEM: Variable names don't explain their purpose.")
    
    print("\n--- CLEAR NAMING (GOOD) ---")
    print("Same code with descriptive names:")
    print()
    
    # Good variable names
    principal_amount = 25
    annual_interest_rate = 0.05
    years = 12
    future_value = principal_amount * (1 + annual_interest_rate) ** years
    
    print("principal_amount = 25")
    print("annual_interest_rate = 0.05")
    print("years = 12")
    print("future_value = principal_amount * (1 + annual_interest_rate) ** years")
    print(f"future_value = {future_value:.2f}")
    print()
    print("Now it's clear:")
    print(f"  - We're calculating compound interest")
    print(f"  - Principal: ${principal_amount}")
    print(f"  - Rate: {annual_interest_rate*100}% per year")
    print(f"  - Period: {years} years")
    print(f"  - Result: ${future_value:.2f}")
    print("BENEFIT: Names immediately explain what data represents.")
    
    print("\n--- Naming Guidelines Comparison ---")
    vague_names = [
        ("x, y, z", "Math only; unclear context"),
        ("temp", "Is it temporary or temperature?"),
        ("data", "Too generic; which data?"),
        ("val", "Abbreviated; hard to remember"),
        ("obj", "What kind of object?"),
        ("result", "Result of what?"),
    ]
    
    better_names = [
        ("price, quantity", "Context-specific; purpose clear"),
        ("temperature_celsius", "Explicit and unambiguous"),
        ("user_email_addresses", "Specific; knows the content"),
        ("customer_age", "Full word; meaning obvious"),
        ("user_account", "Type is clear from name"),
        ("calculated_total", "Explains what was calculated"),
    ]
    
    print("VAGUE -> BETTER")
    for vague, better in zip(vague_names, better_names):
        print(f"  {vague[0]:20} -> {better[0]:25} [{better[1]}]")


# =====================================================================
# SECTION 2: SNAKE_CASE VS OTHER NAMING CONVENTIONS
# =====================================================================

def demonstrate_snake_case_convention():
    """
    Show snake_case consistency as per PEP 8.
    """
    print("\n" + "="*70)
    print("SECTION 2: SNAKE_CASE VS OTHER NAMING CONVENTIONS (PEP 8)")
    print("="*70)
    
    print("\n--- PEP 8 PYTHON NAMING CONVENTIONS ---")
    print()
    print("PEP 8 specifies:")
    print("  • Variables: snake_case (lowercase with underscores)")
    print("  • Classes: PascalCase (capitalize each word)")
    print("  • Constants: UPPER_SNAKE_CASE (all uppercase with underscores)")
    print("  • Private: _prefix_underscore")
    
    print("\n--- INCONSISTENT NAMING (BAD) ---")
    print()
    
    # Bad: inconsistent styles
    userName = "alice"  # camelCase (wrong for Python)
    EmailAddress = "alice@example.com"  # PascalCase (reserved for classes)
    age = 28  # snake_case (one correct)
    Salary = 75000  # PascalCase (wrong)
    MAX_RETRIES = 3  # UPPER_SNAKE_CASE (good for constants, but mixed with others)
    
    print("userName = 'alice'              # camelCase - wrong for Python")
    print("EmailAddress = 'alice@...'      # PascalCase - reserved for classes")
    print("age = 28                         # snake_case - correct!")
    print("Salary = 75000                   # PascalCase - inconsistent")
    print("MAX_RETRIES = 3                  # UPPER_SNAKE_CASE - good for constants")
    print()
    print("PROBLEM: Inconsistent styles make code look messy and unprofessional.")
    print("         Reviewers have to focus on style instead of logic.")
    
    print("\n--- CONSISTENT NAMING (GOOD) ---")
    print()
    
    # Good: consistent styles
    user_name = "alice"
    email_address = "alice@example.com"
    user_age = 28
    user_salary = 75000
    MAX_RETRIES = 3
    
    print("user_name = 'alice'              # Snake case - variable")
    print("email_address = 'alice@...'      # Snake case - variable")
    print("user_age = 28                    # Snake case - variable")
    print("user_salary = 75000              # Snake case - variable")
    print("MAX_RETRIES = 3                  # UPPER_SNAKE_CASE - constant")
    print()
    print("BENEFIT: All Python variables follow the same pattern.")
    print("         Code looks professional and follows Python standards.")
    
    print("\n--- MORE EXAMPLES ---")
    print()
    print("Variables (snake_case):")
    print("  customer_email = '...'         # Clearly a variable")
    print("  order_total = 150.00           # Clearly a variable")
    print("  is_premium_member = True       # Boolean: 'is_' prefix is common")
    print("  process_order_id = 12345       # Clearly a variable")
    print()
    print("Constants (UPPER_SNAKE_CASE):")
    print("  DATABASE_URL = 'localhost:...' # Configuration constant")
    print("  API_KEY = 'abc123...'          # Sensitive constant")
    print("  MAX_LOGIN_ATTEMPTS = 5         # Business rule constant")
    print("  DEFAULT_TIMEOUT_SECONDS = 30   # Default configuration")
    print()
    print("Classes (PascalCase):")
    print("  class User:                    # Each word capitalized")
    print("  class PaymentProcessor:        # Each word capitalized")
    print("  class OrderValidator:          # Each word capitalized")


# =====================================================================
# SECTION 3: MEANINGFUL COMMENTS - INTENT VS REDUNDANCY
# =====================================================================

def demonstrate_comment_best_practices():
    """
    Show meaningful comments that explain why, not what.
    """
    print("\n" + "="*70)
    print("SECTION 3: MEANINGFUL COMMENTS - INTENT VS REDUNDANCY")
    print("="*70)
    
    print("\n--- REDUNDANT COMMENTS (BAD) ---")
    print("Comments that just repeat the code:")
    print()
    
    # Bad comments - they just repeat the code
    print("# BAD: Redundant comment")
    print("username = 'alice'  # Set username to alice")
    print("age = 30            # Set age to 30")
    print("total = 0           # Initialize total to zero")
    print()
    print("PROBLEM: Comments don't add information.")
    print("         Anyone reading the code already knows what's happening.")
    print("         These clutter the code without helping understanding.")
    
    print("\n--- MEANINGFUL COMMENTS (GOOD) ---")
    print("Comments that explain WHY, not WHAT:")
    print()
    
    # Good comments - they explain intent/reason
    print("# GOOD: Meaningful comment")
    print("username = 'alice'  # Default test user for development environment")
    print("age = 30            # Minimum age for premium subscription eligibility")
    print("total = 0           # Start at zero; will accumulate items from cart")
    print()
    print("BENEFIT: Comments explain reasoning and important context.")
    print("         Reviewers understand WHY code is written this way.")
    
    print("\n--- COMMENT TYPES AND WHEN TO USE THEM ---")
    print()
    
    print("1. EXPLANATION (WHY/CONTEXT)")
    print("   Use when: The reason for code is non-obvious")
    print("   Example:")
    print("   # We use index+1 because arrays are 0-indexed but users see 1-indexed")
    print("   display_position = array_index + 1")
    print()
    
    print("2. WARNING/GOTCHA")
    print("   Use when: There's a subtle gotcha developers should know")
    print("   Example:")
    print("   # WARNING: This modifies the list in-place, not creating a copy")
    print("   items.reverse()")
    print()
    
    print("3. TODO/FIXME")
    print("   Use when: Something needs work")
    print("   Example:")
    print("   # TODO: Refactor this function; currently handles 5 edge cases poorly")
    print("   if status == 'pending':")
    print("       process_order()")
    print()
    
    print("4. WORKAROUND/HACK")
    print("   Use when: Code solves problem in non-standard way")
    print("   Example:")
    print("   # Workaround for API bug: URL must be lowercase")
    print("   endpoint = base_url.lower()")
    print()
    
    print("5. BUSINESS LOGIC")
    print("   Use when: Logic implements business requirement")
    print("   Example:")
    print("   # Loyalty members get 15% discount (requirement from finance)")
    print("   if customer.is_loyalty_member:")
    print("       discount = 0.15")
    print()
    
    print("DON'T use comments for:")
    print("   - Restating obvious code (i+1 # add 1 to i)")
    print("   - Obvious loop purposes (for item in items: # loop through items)")
    print("   - Explaining built-in functions users should know")


# =====================================================================
# SECTION 4: BEFORE/AFTER REFACTORING - NAMING
# =====================================================================

def demonstrate_before_after_naming():
    """
    Show real-world before/after refactoring for names.
    """
    print("\n" + "="*70)
    print("SECTION 4: BEFORE/AFTER REFACTORING - NAMING")
    print("="*70)
    
    print("\n--- BEFORE: Vague Names ---")
    print()
    
    code_before = """
def calc(p, m, r):
    mp = p * m
    res = 0
    for i in range(m):
        res += mp * (1 + r) ** i
    return res
    """
    
    print(code_before)
    print("PROBLEMS:")
    print("  - What does calc do? Calculate what?")
    print("  - What are p, m, r? Need comments just to understand parameters")
    print("  - What is mp? Some kind of product?")
    print("  - What is res? Result of what calculation?")
    print("  - What is the loop doing?")
    print()
    
    print("--- AFTER: Clear Names ---")
    print()
    
    code_after = """
def calculate_investment_growth(principal, num_years, annual_return_rate):
    # Calculate future value with compound returns
    annual_principal_value = principal / num_years
    total_investment_value = 0
    
    for year in range(num_years):
        total_investment_value += annual_principal_value * (1 + annual_return_rate) ** year
    
    return total_investment_value
    """
    
    print(code_after)
    print("IMPROVEMENTS:")
    print("  - Function name tells us what it calculates")
    print("  - Parameter names are self-documenting")
    print("  - Variable names explain their purpose")
    print("  - Code logic is immediately understandable")
    print("  - Loop starts at year 0, increments through years (clear intent)")
    
    print("\n--- Time Comparison ---")
    print()
    print("BEFORE: Reading 'calc' function")
    print("  1. What does this do? (check name - unclear)")
    print("  2. What are p, m, r? (need documentation or context)")
    print("  3. What is mp? (think about math, or add comment)")
    print("  4. What is res? (trial and error)")
    print("  5. What is the loop doing? (trace through logic)")
    print("  Total: 10-15 minutes to understand")
    print()
    print("AFTER: Reading 'calculate_investment_growth' function")
    print("  1. Immediately know it calculates investment growth")
    print("  2. Parameters are clear from names")
    print("  3. Annual value calculation is obvious")
    print("  4. Loop clearly processes years")
    print("  5. Total value accumulation is clear")
    print("  Total: 1-2 minutes to understand")
    print()
    print("IMPACT: Clear naming reduces cognitive load dramatically.")


# =====================================================================
# SECTION 5: BEFORE/AFTER REFACTORING - COMMENTS
# =====================================================================

def demonstrate_before_after_comments():
    """
    Show real-world before/after refactoring for comments.
    """
    print("\n" + "="*70)
    print("SECTION 5: BEFORE/AFTER REFACTORING - COMMENTS")
    print("="*70)
    
    print("\n--- BEFORE: Bad Comments ---")
    print()
    
    code_before = """
def process_order(order):
    total = 0  # set total to 0
    for item in order.items:  # loop through items
        total += item.price  # add price to total
    
    if total > 100:  # if total is greater than 100
        discount = total * 0.1  # 10% discount
    else:  # otherwise
        discount = 0  # no discount
    
    final_price = total - discount  # subtract discount from total
    return final_price  # return final price
    """
    
    print(code_before)
    print()
    print("PROBLEMS:")
    print("  - Comments repeat obvious code ('set total to 0')")
    print("  - 'if total > 100' reason is unclear")
    print("  - Why 10% discount? Business requirement? Arbitrary?")
    print("  - Too many comments for simple logic")
    
    print("\n--- AFTER: Good Comments ---")
    print()
    
    code_after = """
def process_order(order):
    total = 0
    for item in order.items:
        total += item.price
    
    # Premium customers (orders over $100) get 10% loyalty discount
    if total > 100:
        discount = total * 0.1
    else:
        discount = 0
    
    final_price = total - discount
    return final_price
    """
    
    print(code_after)
    print()
    print("IMPROVEMENTS:")
    print("  - One meaningful comment explains business logic")
    print("  - Says WHAT business rule exists (orders over $100)")
    print("  - Says WHAT discount applies (10% loyalty)")
    print("  - Code is self-explanatory without comment clutter")
    print("  - Reader understands purpose, not just mechanism")
    
    print("\n--- Comment Removal Guide ---")
    print()
    print("REMOVE these redundant comments:")
    print("  x = 5        # set x to 5 (obvious from code)")
    print("  name = 'a'   # assign a to name (obvious)")
    print("  for i in range(10):  # loop 10 times (obvious)")
    print()
    print("KEEP these meaningful comments:")
    print("  x = 5        # minimum password length (explains purpose)")
    print("  name = 'a'   # default admin user for testing only (explains why)")
    print("  for i in range(10):  # retry up to 10 times per API limit (explains why)")


# =====================================================================
# SECTION 6: NAMING CONVENTIONS FOR DIFFERENT DATA TYPES
# =====================================================================

def demonstrate_naming_by_type():
    """
    Show naming conventions for different data types.
    """
    print("\n" + "="*70)
    print("SECTION 6: NAMING CONVENTIONS FOR DIFFERENT DATA TYPES")
    print("="*70)
    
    print("\n--- BOOLEANS: Use 'is_' or 'has_' prefix ---")
    print()
    
    is_active = True
    is_premium_member = False
    has_discount = True
    is_valid_email = True
    
    print(f"is_active = {is_active}              # Clearly a boolean")
    print(f"is_premium_member = {is_premium_member}          # Clearly a boolean")
    print(f"has_discount = {has_discount}             # Clearly a boolean")
    print(f"is_valid_email = {is_valid_email}         # Clearly a boolean")
    print()
    print("BENEFIT: Immediate clarity that these are boolean true/false")
    print("         Natural language reading: 'is active', 'has discount'")
    
    print("\n--- COLLECTIONS: Use plural names ---")
    print()
    
    customers = ["alice", "bob", "charlie"]
    user_ids = [1, 2, 3, 4, 5]
    email_addresses = ["alice@ex.com", "bob@ex.com"]
    
    print(f"customers = {customers}          # Plural - clearly a collection")
    print(f"user_ids = {user_ids}             # Plural - clearly a collection")
    print(f"email_addresses = {email_addresses}  # Plural - clearly a collection")
    print()
    print("BENEFIT: Plural form signals 'this is multiple items'")
    print("         Developer knows to loop or iterate")
    
    print("\n--- NUMBERS/MEASUREMENTS: Include unit in name ---")
    print()
    
    user_age = 28
    timeout_seconds = 30
    max_retries = 5
    temperature_celsius = 25
    price_usd = 99.99
    distance_km = 42
    
    print(f"user_age = {user_age}                  # What unit? Years (obvious here)")
    print(f"timeout_seconds = {timeout_seconds}            # Unit: seconds (explicit)")
    print(f"max_retries = {max_retries}                 # Count (no unit needed)")
    print(f"temperature_celsius = {temperature_celsius}        # Unit: celsius (explicit)")
    print(f"price_usd = {price_usd}                 # Currency: USD (explicit)")
    print(f"distance_km = {distance_km}                 # Unit: kilometers (explicit)")
    print()
    print("BENEFIT: Including units prevents calculation errors")
    print("         'timeout_seconds' prevents multiplying by wrong factor")
    print("         'price_usd' prevents currency confusion")
    
    print("\n--- CONTAINER TYPES: Make the type clear ---")
    print()
    
    user_dict = {"name": "alice", "age": 28}
    user_list = ["alice", "bob", "charlie"]
    user_set = {"alice", "bob"}
    
    print(f"user_dict = {user_dict}   # 'dict' suffix signals dictionary")
    print(f"user_list = {user_list}      # 'list' suffix signals list")
    print(f"user_set = {user_set}        # 'set' suffix signals set")
    print()
    print("Alternative:"
    )
    print(f"users_by_id = {{1: 'alice', 2: 'bob'}}  # 'by_id' signals lookup")
    print(f"unique_emails = {{'a@ex', 'b@ex'}}       # 'unique_' signals set")


# =====================================================================
# SECTION 7: PEP 8 BASICS - LINE LENGTH AND WHITESPACE
# =====================================================================

def demonstrate_pep8_formatting():
    """
    Show PEP 8 formatting basics.
    """
    print("\n" + "="*70)
    print("SECTION 7: PEP 8 BASICS - LINE LENGTH AND WHITESPACE")
    print("="*70)
    
    print("\n--- LINE LENGTH: 79 Characters (or 88 with modern tools) ---")
    print()
    
    print("BAD: One very long line that's hard to read")
    print()
    long_line = "calculated_price = (base_price * (1 + tax_rate) - discount_amount) * (1 + loyalty_multiplier) if customer_is_premium else base_price * (1 + tax_rate)"
    print(f"Line length: {len(long_line)} characters")
    print()
    
    print("GOOD: Broken into logical lines")
    print()
    print("if customer_is_premium:")
    print("    # Premium customers get loyalty multiplier")
    print("    tax_adjusted_price = base_price * (1 + tax_rate)")
    print("    with_discount = tax_adjusted_price - discount_amount")
    print("    calculated_price = with_discount * loyalty_multiplier")
    print("else:")
    print("    calculated_price = base_price * (1 + tax_rate)")
    print()
    print("BENEFIT: Easier to read, easier to spot bugs, fits in any editor")
    
    print("\n--- WHITESPACE: Two Blank Lines Between Functions ---")
    print()
    
    print("GOOD practice in modules:")
    print()
    print("def first_function():")
    print("    pass")
    print()
    print()
    print("def second_function():")
    print("    pass")
    print()
    print()
    print("class MyClass:")
    print("    pass")
    print()
    print("BENEFIT: Functions and classes are visually separated")
    print("         Easy to scan a module")
    
    print("\n--- SPACING: Around Operators ---")
    print()
    
    print("BAD (no spaces:")
    print("  result=value1+value2*value3")
    print()
    print("GOOD (with spaces):")
    print("  result = value1 + value2 * value3")
    print()
    print("BENEFIT: Operators stand out, formula is clear")


# =====================================================================
# SECTION 8: CODE REVIEW PERSPECTIVE - WHAT MATTERS
# =====================================================================

def demonstrate_code_review_perspective():
    """
    Show what code reviewers look for in naming and comments.
    """
    print("\n" + "="*70)
    print("SECTION 8: CODE REVIEW PERSPECTIVE - WHAT MATTERS")
    print("="*70)
    
    print("\n--- A Reviewer's Checklist ---")
    print()
    
    checklist = [
        ("Variable Names", "Are names descriptive and unambiguous?"),
        ("Naming Convention", "Do all variables use snake_case consistently?"),
        ("Comments", "Do comments explain WHY, not WHAT?"),
        ("Comment Quality", "Are redundant comments removed?"),
        ("Line Length", "Can I read each line without horizontal scrolling?"),
        ("Readability", "Could a teammate find a bug quickly?"),
        ("Type Clarity", "Can I tell if something is a list, dict, or boolean?"),
        ("Constants", "Are magic numbers explained or extracted as constants?"),
    ]
    
    print("When reviewing code, I check:")
    print()
    for category, question in checklist:
        print(f"  [{category}]")
        print(f"    - {question}")
        print()
    
    print("\n--- Red Flags That Trigger Questions ---")
    print()
    
    red_flags = [
        "d, x, temp, val (single-letter or vague names)",
        "userName, EmailAddress (inconsistent casing)",
        "# increment i (comment repeats the code)",
        "lines over 100 characters long",
        "unclear variable types (is it a list or string?)",
        "magic numbers with no explanation",
        "mixedNaming_conventions-in_one_file",
    ]
    
    for i, flag in enumerate(red_flags, 1):
        print(f"  {i}. {flag}")
    
    print("\n--- When Code Gets Question Marks in Review ---")
    print()
    print("BAD CODE (triggers review questions):")
    print()
    print("def calc(d, t, r):")
    print("    x = d * r  # was: d is principal, r is rate, t is time")
    print("    for i in range(t):")
    print("        x *= (1 + r)")
    print("    return x")
    print()
    print("Reviewer questions:")
    print("  - What does calc() do? Why no docstring?")
    print("  - What are d, t, r? Will need to add a comment?")
    print("  - What is x? Multiple conflicting calculations?")
    print("  - Why the loop? This seems like compound interest but line 2 already...")
    print()
    print("GOOD CODE (passes review quickly):")
    print()
    print("def calculate_compound_interest(principal, years, annual_rate):")
    print("    # Calculate final amount after compound interest")
    print("    return principal * (1 + annual_rate) ** years")
    print()
    print("Reviewer response:")
    print("  - Clear function name and purpose")
    print("  - Self-documenting parameters")
    print("  - Simple, correct formula")
    print("  - Approved in 30 seconds")


# =====================================================================
# SECTION 9: BEST PRACTICES FOR READABLE CODE
# =====================================================================

def demonstrate_best_practices():
    """
    Summary of best practices for readable code.
    """
    print("\n" + "="*70)
    print("SECTION 9: BEST PRACTICES FOR READABLE CODE")
    print("="*70)
    
    print("\n--- Golden Rules for Readability ---")
    print()
    
    rules = [
        ("Name Purpose, Not Implementation",
         "customer_age (good) vs age_var (bad)\nFocus on what data represents, not where it's stored"),
        
        ("Use Full Words, Not Abbreviations",
         "user_email_address (good) vs usr_em (bad)\nAvoid abbreviations that need mental translation"),
        
        ("Be Consistent",
         "All variables use snake_case, all constants use UPPER_SNAKE_CASE\nNever mix naming styles in one file"),
        
        ("Comments Explain Why, Not What",
         "# Cache bust param required for API version 2 (good)\nvs # Add random to URL (bad)\nAssume reader can read the code; explain the reasoning"),
        
        ("Make Implicit Explicit",
         "timeout_seconds = 30 (good) vs timeout = 30 (bad)\nInclude units, types, and context in names"),
        
        ("Keep Lines Readable",
         "Break long lines, indent for clarity\nAvoid horizontal scrolling at all costs"),
        
        ("Remove Dead Comments",
         "Comments are not needed on every line\nDelete comments as code evolves; keep them accurate"),
        
        ("Type Hints in Names",
         "is_valid, users_list, price_dict\nBooleans start with 'is_', collections are plural, containers show type"),
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
    print("*" + "MILESTONE 7: READABLE NAMES & COMMENTS (PEP8 BASICS)".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    demonstrate_variable_naming_clarity()
    demonstrate_snake_case_convention()
    demonstrate_comment_best_practices()
    demonstrate_before_after_naming()
    demonstrate_before_after_comments()
    demonstrate_naming_by_type()
    demonstrate_pep8_formatting()
    demonstrate_code_review_perspective()
    demonstrate_best_practices()
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Variable names should clearly describe purpose and content")
    print("  • Consistently use snake_case for variables, UPPER_SNAKE_CASE for constants")
    print("  • Comments explain WHY code exists, not WHAT it does")
    print("  • Good naming reduces need for comments")
    print("  • Code is read far more often than written")
    print("  • PEP 8 conventions make Python code feel familiar to all developers")
    print("\n")
