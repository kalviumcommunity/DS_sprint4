"""
Python Functions: Definition and Calling Demonstration

This script demonstrates core understanding of:
- Defining functions using def
- Function parameters and arguments
- Calling functions from code
- Return values
- Function organization and code reuse
- Design principles: DRY (Don't Repeat Yourself)
"""


def demonstrate_basic_function_definition():
    """
    Demonstrate basic function definition and calling.
    """
    print("\n" + "=" * 60)
    print("1. BASIC FUNCTION DEFINITION AND CALLING")
    print("=" * 60)

    # Define a simple function (no parameters)
    print("\n--- Define Function (No Parameters) ---")
    print("Code:")
    print("  def greet():")
    print("      print('Hello, World!')")
    print("      print('Welcome to Python functions')")

    def greet():
        """A simple function that prints a greeting."""
        print("  Hello, World!")
        print("  Welcome to Python functions")

    # Call the function
    print("\nCalling: greet()")
    print("Output:")
    greet()

    # Function is reusable
    print("\nCalling again: greet()")
    print("Output:")
    greet()
    print("(Same function, called twice - code reuse!)")

    # Define function with single parameter
    print("\n--- Define Function (One Parameter) ---")
    print("Code:")
    print("  def greet_person(name):")
    print("      print(f'Hello, {name}!')")

    def greet_person(name):
        """Greet a specific person."""
        print(f"  Hello, {name}!")

    print("\nCalling: greet_person('Alice')")
    print("Output:")
    greet_person("Alice")

    print("\nCalling: greet_person('Bob')")
    print("Output:")
    greet_person("Bob")


def demonstrate_function_parameters():
    """
    Demonstrate functions with various parameter patterns.
    """
    print("\n" + "=" * 60)
    print("2. FUNCTION PARAMETERS")
    print("=" * 60)

    # Multiple parameters
    print("\n--- Multiple Parameters ---")
    print("Code:")
    print("  def add(a, b):")
    print("      result = a + b")
    print("      print(f'{a} + {b} = {result}')")

    def add(a, b):
        """Add two numbers and print result."""
        result = a + b
        print(f"  {a} + {b} = {result}")

    print("\nCalling: add(5, 3)")
    add(5, 3)

    print("\nCalling: add(100, 25)")
    add(100, 25)

    # Order of parameters matters
    print("\n--- Parameter Order Matters ---")
    print("Code:")
    print("  def subtract(a, b):")
    print("      result = a - b")
    print("      print(f'{a} - {b} = {result}')")

    def subtract(a, b):
        """Subtract b from a."""
        result = a - b
        print(f"  {a} - {b} = {result}")

    print("\nCalling: subtract(10, 3)")
    subtract(10, 3)

    print("\nCalling: subtract(3, 10)  [reversed order]")
    subtract(3, 10)
    print("(Different result because order changed!)")

    # Named parameters (keyword arguments)
    print("\n--- Named Parameters (Keyword Arguments) ---")
    print("Code:")
    print("  def describe_person(name, age, city):")
    print("      print(f'{name}, age {age}, from {city}')")

    def describe_person(name, age, city):
        """Describe a person with name, age, and city."""
        print(f"  {name}, age {age}, from {city}")

    print("\nCalling with positional: describe_person('Alice', 25, 'Boston')")
    describe_person("Alice", 25, "Boston")

    print("\nCalling with named: describe_person(name='Bob', city='NYC', age=30)")
    describe_person(name="Bob", city="NYC", age=30)
    print("(Order doesn't matter with named parameters)")

    # Default parameters
    print("\n--- Default Parameters ---")
    print("Code:")
    print("  def greet_with_default(name, greeting='Hello'):")
    print("      print(f'{greeting}, {name}!')")

    def greet_with_default(name, greeting="Hello"):
        """Greet with optional greeting message."""
        print(f"  {greeting}, {name}!")

    print("\nCalling: greet_with_default('Alice')")
    greet_with_default("Alice")

    print("\nCalling: greet_with_default('Bob', 'Hi')")
    greet_with_default("Bob", "Hi")

    print("\nCalling: greet_with_default('Charlie', 'Hey there')")
    greet_with_default("Charlie", "Hey there")


def demonstrate_function_return_values():
    """
    Demonstrate functions that return values.
    """
    print("\n" + "=" * 60)
    print("3. FUNCTION RETURN VALUES")
    print("=" * 60)

    # Function returning a value
    print("\n--- Simple Return ---")
    print("Code:")
    print("  def multiply(a, b):")
    print("      return a * b")
    print("  result = multiply(4, 5)")
    print("  print(f'Result: {result}')")

    def multiply(a, b):
        """Multiply two numbers and return result."""
        return a * b

    result = multiply(4, 5)
    print("\nOutput:")
    print(f"  Result: {result}")

    # Function returning string
    print("\n--- Return String ---")
    print("Code:")
    print("  def get_status(score):")
    print("      if score >= 90:")
    print("          return 'Excellent'")
    print("      elif score >= 70:")
    print("          return 'Good'")
    print("      else:")
    print("          return 'Needs Improvement'")

    def get_status(score):
        """Return status based on score."""
        if score >= 90:
            return "Excellent"
        elif score >= 70:
            return "Good"
        else:
            return "Needs Improvement"

    print("\nCalling with different scores:")
    print(f"  Score 95: {get_status(95)}")
    print(f"  Score 80: {get_status(80)}")
    print(f"  Score 60: {get_status(60)}")

    # Function returning multiple values
    print("\n--- Return Multiple Values ---")
    print("Code:")
    print("  def get_min_max(numbers):")
    print("      return min(numbers), max(numbers)")
    print("  smallest, largest = get_min_max([5, 2, 8, 1, 9])")

    def get_min_max(numbers):
        """Return minimum and maximum from list."""
        return min(numbers), max(numbers)

    print("\nOutput:")
    smallest, largest = get_min_max([5, 2, 8, 1, 9])
    print(f"  Smallest: {smallest}, Largest: {largest}")

    # Function returning dictionary
    print("\n--- Return Dictionary ---")
    print("Code:")
    print("  def calculate_stats(numbers):")
    print("      return {")
    print("          'sum': sum(numbers),")
    print("          'average': sum(numbers) / len(numbers),")
    print("          'count': len(numbers)")
    print("      }")

    def calculate_stats(numbers):
        """Calculate and return statistics."""
        return {
            "sum": sum(numbers),
            "average": sum(numbers) / len(numbers),
            "count": len(numbers)
        }

    print("\nOutput:")
    stats = calculate_stats([10, 20, 30, 40])
    print(f"  Stats: {stats}")


def demonstrate_execution_flow():
    """
    Demonstrate how execution flows between function and caller.
    """
    print("\n" + "=" * 60)
    print("4. EXECUTION FLOW: HOW FUNCTIONS ARE CALLED")
    print("=" * 60)

    print("\n--- Execution Flow Step by Step ---")
    print("Code:")
    print("  def process_value(x):")
    print("      print(f'[Inside function] Received: {x}')")
    print("      result = x * 2")
    print("      print(f'[Inside function] Calculated: {result}')")
    print("      return result")
    print("")
    print("  print('[Main] Calling function')")
    print("  output = process_value(5)")
    print("  print(f'[Main] Got back: {output}')")

    def process_value(x):
        """Process a value and return it doubled."""
        print(f"  [Inside function] Received: {x}")
        result = x * 2
        print(f"  [Inside function] Calculated: {result}")
        return result

    print("\nExecution:")
    print("  [Main] Calling function")
    output = process_value(5)
    print(f"  [Main] Got back: {output}")

    # Nested function calls
    print("\n--- Nested Function Calls ---")
    print("Code:")
    print("  def double(x):")
    print("      return x * 2")
    print("  def quadruple(x):")
    print("      return double(double(x))  # Call double twice")
    print("  result = quadruple(3)")

    def double(x):
        """Double a number."""
        return x * 2

    def quadruple(x):
        """Quadruple a number by calling double twice."""
        return double(double(x))

    print("\nOutput:")
    result = quadruple(3)
    print(f"  quadruple(3) = {result}")


def demonstrate_dry_principle():
    """
    Demonstrate DRY (Don't Repeat Yourself) principle.
    """
    print("\n" + "=" * 60)
    print("5. DRY PRINCIPLE: AVOIDING CODE DUPLICATION")
    print("=" * 60)

    # Without functions (repetitive code)
    print("\n--- PROBLEM: Repeated Code (No Functions) ---")
    print("Code WITHOUT functions:")
    print("  # Calculate price for item 1")
    print("  price1 = 10")
    print("  tax1 = price1 * 0.08")
    print("  total1 = price1 + tax1")
    print("  print(f'Item 1: ${total1:.2f}')")
    print("")
    print("  # Calculate price for item 2")
    print("  price2 = 25")
    print("  tax2 = price2 * 0.08")
    print("  total2 = price2 + tax2")
    print("  print(f'Item 2: ${total2:.2f}')")
    print("")
    print("  # Calculate price for item 3")
    print("  price3 = 15")
    print("  tax3 = price3 * 0.08")
    print("  total3 = price3 + tax3")
    print("  print(f'Item 3: ${total3:.2f}')")
    print("\n  [Problem: Same code repeated 3 times!]")

    # With functions (DRY)
    print("\n--- SOLUTION: Extract to Function (DRY) ---")
    print("Code WITH function:")
    print("  def calculate_with_tax(price, tax_rate=0.08):")
    print("      total = price + (price * tax_rate)")
    print("      return total")
    print("")
    print("  prices = [10, 25, 15]")
    print("  for i, price in enumerate(prices, 1):")
    print("      total = calculate_with_tax(price)")
    print("      print(f'Item {i}: ${total:.2f}')")

    def calculate_with_tax(price, tax_rate=0.08):
        """Calculate total with tax."""
        total = price + (price * tax_rate)
        return total

    print("\nOutput:")
    prices = [10, 25, 15]
    for i, price in enumerate(prices, 1):
        total = calculate_with_tax(price)
        print(f"  Item {i}: ${total:.2f}")

    print("\nBenefits of DRY:")
    print("  - Code is shorter and cleaner")
    print("  - Easier to update (change once, not 3 times)")
    print("  - Easier to debug (test in one place)")
    print("  - Functions can be reused elsewhere")


def demonstrate_practical_functions():
    """
    Demonstrate practical function examples.
    """
    print("\n" + "=" * 60)
    print("6. PRACTICAL FUNCTION EXAMPLES")
    print("=" * 60)

    # Data validation function
    print("\n--- Validation Function ---")
    print("Code:")
    print("  def is_valid_email(email):")
    print("      return '@' in email and '.' in email")
    print("  def is_valid_age(age):")
    print("      return isinstance(age, int) and 0 < age < 150")

    def is_valid_email(email):
        """Check if email has @ and dot."""
        return "@" in email and "." in email

    def is_valid_age(age):
        """Check if age is a reasonable number."""
        return isinstance(age, int) and 0 < age < 150

    print("\nTesting:")
    print(f"  is_valid_email('user@example.com'): {is_valid_email('user@example.com')}")
    print(f"  is_valid_email('invalid-email'): {is_valid_email('invalid-email')}")
    print(f"  is_valid_age(25): {is_valid_age(25)}")
    print(f"  is_valid_age(200): {is_valid_age(200)}")

    # Data transformation function
    print("\n--- Transformation Function ---")
    print("Code:")
    print("  def format_name(first, last):")
    print("      return f'{first.capitalize()} {last.capitalize()}'")

    def format_name(first, last):
        """Format name with proper capitalization."""
        return f"{first.capitalize()} {last.capitalize()}"

    print("\nUsage:")
    print(f"  format_name('alice', 'johnson'): {format_name('alice', 'johnson')}")
    print(f"  format_name('bob', 'smith'): {format_name('bob', 'smith')}")

    # Data aggregation function
    print("\n--- Aggregation Function ---")
    print("Code:")
    print("  def summarize_data(numbers):")
    print("      if not numbers:")
    print("          return None")
    print("      return {")
    print("          'count': len(numbers),")
    print("          'total': sum(numbers),")
    print("          'average': sum(numbers) / len(numbers),")
    print("          'min': min(numbers),")
    print("          'max': max(numbers)")
    print("      }")

    def summarize_data(numbers):
        """Summarize a list of numbers."""
        if not numbers:
            return None
        return {
            "count": len(numbers),
            "total": sum(numbers),
            "average": sum(numbers) / len(numbers),
            "min": min(numbers),
            "max": max(numbers)
        }

    print("\nUsage:")
    data = [10, 20, 30, 40, 50]
    summary = summarize_data(data)
    print(f"  Data: {data}")
    print(f"  Summary: {summary}")


def demonstrate_function_organization():
    """
    Demonstrate organizing code with functions.
    """
    print("\n" + "=" * 60)
    print("7. FUNCTION ORGANIZATION & DESIGN PRINCIPLES")
    print("=" * 60)

    print("\n--- Single Responsibility Principle ---")
    print("Each function should do ONE thing well")
    print("")

    # Bad: Function does too much
    print("NOT GOOD (Function does multiple things):")
    print("  def process_order(items):")
    print("      total = sum(item['price'] for item in items)")
    print("      tax = total * 0.08")
    print("      final = total + tax")
    print("      send_email(f'Total: {final}')")
    print("      save_to_database(final)")
    print("      print(final)")
    print("      return final")

    # Good: Separate functions
    print("\nGOOD (Each function has one responsibility):")
    print("  def calculate_total(items):")
    print("      return sum(item['price'] for item in items)")
    print("  def add_tax(amount):")
    print("      return amount * 1.08")
    print("  def notify_customer(total):")
    print("      send_email(f'Total: {total}')")
    print("  def save_order(total):")
    print("      save_to_database(total)")

    # Function naming
    print("\n--- Clear Function Names ---")
    print("GOOD names describe what function DOES:")
    print("  [OK] calculate_total()")
    print("  [OK] is_valid_email()")
    print("  [OK] get_user_by_id()")
    print("  [OK] send_notification()")
    print("")
    print("BAD names don't describe purpose:")
    print("  [BAD] process()")
    print("  [BAD] do_stuff()")
    print("  [BAD] x()")

    # Documentation
    print("\n--- Function Documentation ---")
    print("Always include docstrings!")
    print("")
    print("Code:")
    print("  def calculate_discount(price, discount_percent):")
    print("      \"\"\"")
    print("      Calculate discounted price.")
    print("      ")
    print("      Args:")
    print("          price: Original price")
    print("          discount_percent: Discount as percentage (0-100)")
    print("      Returns:")
    print("          Discounted price")
    print("      \"\"\"")
    print("      return price * (1 - discount_percent / 100)")


def demonstrate_code_without_functions():
    """
    Show code WITHOUT functions (problematic).
    """
    print("\n" + "=" * 60)
    print("8. REFACTORING: FROM REPETITIVE CODE TO FUNCTIONS")
    print("=" * 60)

    print("\n--- BEFORE: Repetitive Code ---")
    print("Imagine we need to format user data multiple times:")
    print("")
    print("user1_first = 'alice'")
    print("user1_last = 'johnson'")
    print("user1_name = user1_first.capitalize() + ' ' + user1_last.capitalize()")
    print("print(f'User: {user1_name}')")
    print("")
    print("user2_first = 'bob'")
    print("user2_last = 'smith'")
    print("user2_name = user2_first.capitalize() + ' ' + user2_last.capitalize()")
    print("print(f'User: {user2_name}')")
    print("")
    print("user3_first = 'charlie'")
    print("user3_last = 'brown'")
    print("user3_name = user3_first.capitalize() + ' ' + user3_last.capitalize()")
    print("print(f'User: {user3_name}')")
    print("")
    print("[Problem: Same code repeated!]")

    print("\n--- AFTER: Using Functions (DRY) ---")
    print("Define once, use many times:")
    print("")
    print("def format_user(first, last):")
    print("    return f'{first.capitalize()} {last.capitalize()}'")
    print("")
    print("users = [")
    print("    ('alice', 'johnson'),")
    print("    ('bob', 'smith'),")
    print("    ('charlie', 'brown')")
    print("]")
    print("")
    print("for first, last in users:")
    print("    name = format_user(first, last)")
    print("    print(f'User: {name}')")
    print("")
    print("[Solution: Code is cleaner and easier to maintain!]")

    # Show it in action
    print("\nActual execution:")
    def format_user(first, last):
        return f"{first.capitalize()} {last.capitalize()}"

    users = [
        ("alice", "johnson"),
        ("bob", "smith"),
        ("charlie", "brown")
    ]

    for first, last in users:
        name = format_user(first, last)
        print(f"  User: {name}")


def demonstrate_function_best_practices():
    """
    Demonstrate best practices for functions.
    """
    print("\n" + "=" * 60)
    print("9. FUNCTION BEST PRACTICES")
    print("=" * 60)

    print("\n--- Best Practice 1: Use Meaningful Function Names ---")
    print("[GOOD] def calculate_total_price(items):")
    print("[BAD]  def calc(x):")

    print("\n--- Best Practice 2: Keep Functions Small ---")
    print("[GOOD] Functions that do one thing (5-15 lines)")
    print("[BAD]  Functions that do everything (100+ lines)")

    print("\n--- Best Practice 3: Clear Parameters ---")
    print("[GOOD] def add_tax(price, tax_rate):")
    print("[BAD]  def calc(x, y, z):")

    print("\n--- Best Practice 4: Handle Edge Cases ---")
    print("Code:")
    print("  def divide(a, b):")
    print("      if b == 0:")
    print("          print('Cannot divide by zero')")
    print("          return None")
    print("      return a / b")

    def divide(a, b):
        """Safely divide with error handling."""
        if b == 0:
            print("  Cannot divide by zero")
            return None
        return a / b

    print("\nUsage:")
    print(f"  divide(10, 2) = {divide(10, 2)}")
    print(f"  divide(10, 0) = {divide(10, 0)}")

    print("\n--- Best Practice 5: Use Default Parameters ---")
    print("[GOOD] def send_email(to, cc=None, bcc=None):")
    print("[BAD]  def send_email(to, cc, bcc):")
    print("(Defaults make function more flexible)")


if __name__ == "__main__":
    print("\n" + "*" * 60)
    print("PYTHON FUNCTIONS: DEFINITION AND CALLING")
    print("*" * 60)

    demonstrate_basic_function_definition()
    demonstrate_function_parameters()
    demonstrate_function_return_values()
    demonstrate_execution_flow()
    demonstrate_dry_principle()
    demonstrate_practical_functions()
    demonstrate_function_organization()
    demonstrate_code_without_functions()
    demonstrate_function_best_practices()

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("[OK] def: Define functions to organize code")
    print("[OK] parameters: Functions take input via parameters")
    print("[OK] call: Use function_name() to execute")
    print("[OK] return: Functions can return values")
    print("[OK] DRY: Use functions to avoid code repetition")
    print("[OK] reuse: Call same function multiple times")
    print("[OK] maintainability: Update logic in one place")
    print("[OK] readability: Functions make code clearer")
    print("[OK] single responsibility: Each function does one thing")
    print("[OK] naming: Use descriptive function names")
    print("\n")
