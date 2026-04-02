"""
=====================================================================
MILESTONE 6: PASSING DATA INTO FUNCTIONS AND RETURNING RESULTS
=====================================================================

This script demonstrates:
1. Function parameters (positional, keyword, default values)
2. Passing arguments into functions
3. Return statements and returning values
4. Storing and reusing returned values
5. Multiple return values
6. The problem with printing vs returning
7. Data flow visualization
8. Practical examples of parameter passing and return values
9. Best practices for function data flow

Focus: Clean data flow through functions - not complex logic.
=====================================================================
"""

# =====================================================================
# SECTION 1: BASIC FUNCTION PARAMETERS AND PASSING ARGUMENTS
# =====================================================================

def demonstrate_basic_parameters():
    """
    Show how functions accept parameters and how arguments are passed.
    """
    print("\n" + "="*70)
    print("SECTION 1: BASIC FUNCTION PARAMETERS AND PASSING ARGUMENTS")
    print("="*70)
    
    # Define a simple function with a parameter
    def greet(name):
        """Function that accepts one parameter."""
        message = f"Hello, {name}!"
        return message
    
    print("\n--- Function Definition ---")
    print("def greet(name):")
    print("    message = f'Hello, {name}!'")
    print("    return message")
    
    print("\n--- Calling Function and Passing Arguments ---")
    result1 = greet("Alice")
    print(f"greet('Alice') returned: {result1}")
    
    result2 = greet("Bob")
    print(f"greet('Bob') returned: {result2}")
    
    # Function with multiple parameters
    def calculate_total(price, quantity):
        """Function that accepts multiple parameters."""
        total = price * quantity
        return total
    
    print("\n--- Multiple Parameters ---")
    print("def calculate_total(price, quantity):")
    print("    total = price * quantity")
    print("    return total")
    
    price = 29.99
    quantity = 5
    total = calculate_total(price, quantity)
    print(f"\ncalculate_total({price}, {quantity}) returned: ${total:.2f}")
    
    # Data flow visualization
    print("\n--- Data Flow Visualization ---")
    print("INPUT: price=29.99, quantity=5")
    print("  |")
    print("  v")
    print("calculate_total(price, quantity)")
    print("  |")
    print("  |-- total = 29.99 * 5")
    print("  |-- total = 149.95")
    print("  |")
    print("  v")
    print("RETURN: 149.95")
    print("  |")
    print("  v")
    print("STORE: total = 149.95")


# =====================================================================
# SECTION 2: KEYWORD ARGUMENTS AND DEFAULT PARAMETERS
# =====================================================================

def demonstrate_keyword_arguments():
    """
    Show keyword arguments and default parameter values.
    """
    print("\n" + "="*70)
    print("SECTION 2: KEYWORD ARGUMENTS AND DEFAULT PARAMETERS")
    print("="*70)
    
    def format_person_info(name, age, city="Unknown", occupation="Not specified"):
        """
        Function with default parameters.
        Parameters without defaults: name, age
        Parameters with defaults: city, occupation
        """
        info = f"{name} (Age: {age}) from {city}, {occupation}"
        return info
    
    print("\n--- Function with Default Parameters ---")
    print("def format_person_info(name, age, city='Unknown', occupation='Not specified'):")
    print("    info = f'{name} (Age: {age}) from {city}, {occupation}'")
    print("    return info")
    
    print("\n--- Positional Arguments Only ---")
    result1 = format_person_info("Alice", 28)
    print(f"format_person_info('Alice', 28)")
    print(f"  -> Returned: {result1}")
    
    print("\n--- Providing All Arguments (Positional) ---")
    result2 = format_person_info("Bob", 35, "New York", "Engineer")
    print(f"format_person_info('Bob', 35, 'New York', 'Engineer')")
    print(f"  -> Returned: {result2}")
    
    print("\n--- Using Keyword Arguments ---")
    result3 = format_person_info(
        name="Charlie",
        age=42,
        occupation="Manager",
        city="Boston"
    )
    print(f"format_person_info(name='Charlie', age=42, occupation='Manager', city='Boston')")
    print(f"  -> Returned: {result3}")
    
    print("\n--- Mixing Positional and Keyword ---")
    result4 = format_person_info("Diana", 31, occupation="Doctor")
    print(f"format_person_info('Diana', 31, occupation='Doctor')")
    print(f"  -> Returned: {result4}")
    
    print("\n--- Why Default Parameters Help ---")
    print("[OK] Reduces required arguments when defaults are acceptable")
    print("[OK] Backwards compatible - old code still works")
    print("[OK] Makes functions flexible and reusable")


# =====================================================================
# SECTION 3: STORING AND REUSING RETURNED VALUES
# =====================================================================

def demonstrate_storing_returned_values():
    """
    Show how to capture and reuse returned values outside functions.
    """
    print("\n" + "="*70)
    print("SECTION 3: STORING AND REUSING RETURNED VALUES")
    print("="*70)
    
    def calculate_invoice_total(subtotal, tax_rate=0.08, discount=0):
        """Calculate invoice total with tax and discount."""
        after_discount = subtotal - discount
        tax = after_discount * tax_rate
        total = after_discount + tax
        return total
    
    print("\n--- Calling a Function and Storing the Result ---")
    print("def calculate_invoice_total(subtotal, tax_rate=0.08, discount=0):")
    print("    after_discount = subtotal - discount")
    print("    tax = after_discount * tax_rate")
    print("    total = after_discount + tax")
    print("    return total")
    
    subtotal = 100.00
    discount = 10.00
    
    print(f"\nsubtotal = {subtotal}")
    print(f"discount = {discount}")
    print(f"invoice_total = calculate_invoice_total({subtotal}, discount={discount})")
    
    invoice_total = calculate_invoice_total(subtotal, discount=discount)
    
    print(f"\nReturned value stored in: invoice_total = {invoice_total:.2f}")
    
    print("\n--- Using Returned Value for Further Calculations ---")
    print(f"Now we REUSE this value:")
    print(f"  invoice_total = {invoice_total:.2f}")
    
    final_amount = invoice_total
    print(f"  final_amount = invoice_total = {final_amount:.2f}")
    
    num_items = 5
    cost_per_item = final_amount / num_items
    print(f"  cost_per_item = {final_amount:.2f} / {num_items} = {cost_per_item:.2f}")
    
    print("\n--- Chaining Function Calls ---")
    print("We can use returned values directly as arguments to other functions:")
    
    def apply_shipping(total, shipping_fee=5.00):
        """Add shipping to total."""
        return total + shipping_fee
    
    print("\ndef apply_shipping(total, shipping_fee=5.00):")
    print("    return total + shipping_fee")
    
    print(f"\nfinal_price = apply_shipping(calculate_invoice_total({subtotal}, discount={discount}))")
    final_price = apply_shipping(calculate_invoice_total(subtotal, discount=discount))
    print(f"  -> final_price = {final_price:.2f}")
    
    print("\nData Flow:")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"    |")
    print(f"    v")
    print(f"  calculate_invoice_total() -> ${invoice_total:.2f}")
    print(f"    |")
    print(f"    v")
    print(f"  apply_shipping() -> ${final_price:.2f}")


# =====================================================================
# SECTION 4: MULTIPLE RETURN VALUES
# =====================================================================

def demonstrate_multiple_returns():
    """
    Show returning multiple values as tuple or dictionary.
    """
    print("\n" + "="*70)
    print("SECTION 4: MULTIPLE RETURN VALUES")
    print("="*70)
    
    print("\n--- Returning Multiple Values as Tuple ---")
    
    def calculate_statistics(numbers):
        """Return multiple statistics about a list of numbers."""
        if not numbers:
            return 0, 0, 0
        
        total = sum(numbers)
        average = total / len(numbers)
        maximum = max(numbers)
        
        return total, average, maximum
    
    print("def calculate_statistics(numbers):")
    print("    total = sum(numbers)")
    print("    average = total / len(numbers)")
    print("    maximum = max(numbers)")
    print("    return total, average, maximum")
    
    print("\ndata = [10, 20, 15, 30, 25]")
    data = [10, 20, 15, 30, 25]
    
    print("total, average, maximum = calculate_statistics(data)")
    total, average, maximum = calculate_statistics(data)
    
    print(f"\nReturned values unpacked:")
    print(f"  total = {total}")
    print(f"  average = {average}")
    print(f"  maximum = {maximum}")
    
    print("\n--- Returning Multiple Values as Dictionary ---")
    
    def analyze_text(text):
        """Return multiple text statistics as dictionary."""
        word_count = len(text.split())
        char_count = len(text)
        line_count = text.count('\n') + 1
        
        return {
            'words': word_count,
            'characters': char_count,
            'lines': line_count
        }
    
    print("def analyze_text(text):")
    print("    word_count = len(text.split())")
    print("    char_count = len(text)")
    print("    line_count = text.count('\\n') + 1")
    print("    return {'words': word_count, 'characters': char_count, 'lines': line_count}")
    
    sample_text = "Python is great.\nFunctions are powerful.\nData flow matters."
    print(f"\ntext = {repr(sample_text)}")
    
    print("stats = analyze_text(text)")
    stats = analyze_text(sample_text)
    
    print(f"\nReturned dictionary:")
    print(f"  stats = {stats}")
    print(f"\nAccessing individual values:")
    print(f"  stats['words'] = {stats['words']}")
    print(f"  stats['characters'] = {stats['characters']}")
    print(f"  stats['lines'] = {stats['lines']}")


# =====================================================================
# SECTION 5: PRINT VS RETURN - THE CRITICAL PROBLEM
# =====================================================================

def demonstrate_print_vs_return():
    """
    Show why returning is better than printing.
    This addresses the scenario: Function prints result instead of returning it.
    """
    print("\n" + "="*70)
    print("SECTION 5: PRINT VS RETURN - THE CRITICAL PROBLEM")
    print("="*70)
    
    print("\n--- The Problem Function (Using print) ---")
    
    def calculate_discount_price_WRONG(original_price, discount_percent):
        """Function that PRINTS instead of RETURNS (PROBLEMATIC)."""
        discount_amount = original_price * (discount_percent / 100)
        discounted_price = original_price - discount_amount
        print(f"Discounted price: ${discounted_price:.2f}")
        # PROBLEM: No return statement!
    
    print("def calculate_discount_price_WRONG(original_price, discount_percent):")
    print("    discount_amount = original_price * (discount_percent / 100)")
    print("    discounted_price = original_price - discount_amount")
    print("    print(f'Discounted price: ${discounted_price:.2f}')")
    print("    # NO RETURN STATEMENT!")
    
    print("\n--- Calling the WRONG function ---")
    print("result = calculate_discount_price_WRONG(100, 20)")
    print("print(f'Returned value: {result}')")
    result = calculate_discount_price_WRONG(100, 20)
    print(f"Returned value: {result}")  # This will be None!
    
    print("\n[OUTPUT ANALYSIS]")
    print("[FAIL] Function printed to console, but returned None")
    print("[FAIL] We cannot REUSE the output (result = None)")
    print("[FAIL] We cannot do calculations with the result")
    print("[FAIL] We cannot pass it to another function")
    
    print("\n--- The Solution Function (Using return) ---")
    
    def calculate_discount_price_CORRECT(original_price, discount_percent):
        """Function that RETURNS the result (CORRECT)."""
        discount_amount = original_price * (discount_percent / 100)
        discounted_price = original_price - discount_amount
        return discounted_price
    
    print("def calculate_discount_price_CORRECT(original_price, discount_percent):")
    print("    discount_amount = original_price * (discount_percent / 100)")
    print("    discounted_price = original_price - discount_amount")
    print("    return discounted_price")
    
    print("\n--- Calling the CORRECT function ---")
    print("result = calculate_discount_price_CORRECT(100, 20)")
    print("print(f'Returned value: {result}')")
    result = calculate_discount_price_CORRECT(100, 20)
    print(f"Returned value: {result}")
    
    print("\n[OUTPUT ANALYSIS]")
    print("[OK] Function returned an actual value (80.0)")
    print("[OK] We CAN REUSE the returned value")
    print("[OK] We CAN do calculations with the result")
    print("[OK] We CAN pass it to other functions")
    
    print("\n--- Why This Matters: Reusability ---")
    print("With RETURN, we can:")
    print()
    
    # Store and reuse
    print("1. Store and reuse the value:")
    discounted = calculate_discount_price_CORRECT(100, 20)
    print(f"   discounted = calculate_discount_price_CORRECT(100, 20)")
    print(f"   print(f'Item costs: ${discounted}')")
    print(f"   Item costs: ${discounted}")
    
    # Chain calculations
    print("\n2. Chain calculations:")
    original = 100
    after_discount = calculate_discount_price_CORRECT(original, 20)
    after_tax = after_discount * 1.08
    print(f"   original = 100")
    print(f"   after_discount = calculate_discount_price_CORRECT(original, 20)")
    print(f"   -> {after_discount}")
    print(f"   after_tax = after_discount * 1.08")
    print(f"   -> {after_tax}")
    
    # Pass to other functions
    print("\n3. Pass to other functions:")
    def apply_loyalty_bonus(price, loyalty_percent):
        bonus = price * (loyalty_percent / 100)
        return bonus
    
    final_discount = apply_loyalty_bonus(discounted, 5)
    print(f"   final_discount = apply_loyalty_bonus(after_discount, 5)")
    print(f"   -> {final_discount:.2f}")
    final_price = discounted - final_discount
    print(f"   final_price = after_discount - final_discount")
    print(f"   -> {final_price:.2f}")
    
    # Use in conditional
    print("\n4. Use in conditional logic:")
    threshold = 75
    print(f"   if after_discount > {threshold}:")
    if after_discount > threshold:
        print(f"       print('Price is too high')")
        print(f"       Price is too high")
    else:
        print(f"       print('Price is acceptable')")
    
    print("\n--- Summary: Print vs Return ---")
    print("PRINT:")
    print("  • Shows output to user (console)")
    print("  • Returns None to the program")
    print("  • Data CANNOT be reused by code")
    print("  • Only useful for displaying final results")
    print()
    print("RETURN:")
    print("  • Gives data back to the program")
    print("  • Enables reuse and chaining")
    print("  • Allows calculations and transformations")
    print("  • Makes functions composable and modular")


# =====================================================================
# SECTION 6: DATA FLOW WITH PARAMETER PASSING
# =====================================================================

def demonstrate_data_flow_visualization():
    """
    Show clear data flow through multiple function calls.
    """
    print("\n" + "="*70)
    print("SECTION 6: DATA FLOW WITH PARAMETER PASSING")
    print("="*70)
    
    def get_input_values():
        """Simulate getting input data."""
        return 500, 0.15, 50
    
    def calculate_salary_after_tax(gross_salary, tax_rate):
        """Calculate net salary after tax."""
        taxes = gross_salary * tax_rate
        net = gross_salary - taxes
        return net
    
    def calculate_pension_contribution(net_salary, pension_rate=0.05):
        """Calculate pension contribution."""
        contribution = net_salary * pension_rate
        return contribution
    
    def display_payslip(gross, taxes, pension, net_after_all):
        """Display the complete payslip."""
        print("\n--- PAYSLIP ---")
        print(f"Gross Salary:        ${gross:>10.2f}")
        print(f"Taxes:               ${taxes:>10.2f}")
        print(f"Pension:             ${pension:>10.2f}")
        print(f"Net After All:       ${net_after_all:>10.2f}")
    
    print("\n--- Scenario: Calculate employee payslip ---")
    print("Step 1: Get input values")
    
    gross_salary, tax_rate, pension_rate = get_input_values()
    print(f"  gross_salary = {gross_salary}")
    print(f"  tax_rate = {tax_rate}")
    print(f"  pension_rate = {pension_rate}")
    
    print("\nStep 2: Calculate net salary after tax")
    net_after_tax = calculate_salary_after_tax(gross_salary, tax_rate)
    taxes = gross_salary * tax_rate
    print(f"  net_after_tax = calculate_salary_after_tax({gross_salary}, {tax_rate})")
    print(f"  -> {net_after_tax}")
    
    print("\nStep 3: Calculate pension contribution")
    pension_amount = calculate_pension_contribution(net_after_tax, pension_rate)
    print(f"  pension_amount = calculate_pension_contribution({net_after_tax}, {pension_rate})")
    print(f"  -> {pension_amount}")
    
    print("\nStep 4: Calculate final net")
    final_net = net_after_tax - pension_amount
    print(f"  final_net = {net_after_tax} - {pension_amount}")
    print(f"  -> {final_net}")
    
    print("\nStep 5: Display payslip")
    display_payslip(gross_salary, taxes, pension_amount, final_net)
    
    print("\n--- Complete Data Flow Diagram ---")
    print("INPUT: gross=500, tax_rate=0.15, pension_rate=0.05")
    print("  |")
    print("  v")
    print("get_input_values() -> (500, 0.15, 0.05)")
    print("  |")
    print("  v")
    print("calculate_salary_after_tax(500, 0.15) -> 425")
    print("  |")
    print("  v")
    print("calculate_pension_contribution(425, 0.05) -> 21.25")
    print("  |")
    print("  v")
    print("final_net = 425 - 21.25 -> 403.75")
    print("  |")
    print("  v")
    print("display_payslip(500, 75, 21.25, 403.75)")


# =====================================================================
# SECTION 7: PRACTICE EXERCISES - PARAMETER PASSING & RETURNS
# =====================================================================

def demonstrate_practice_exercises():
    """
    Practical exercises showing parameter passing and returns.
    """
    print("\n" + "="*70)
    print("SECTION 7: PRACTICE EXERCISES")
    print("="*70)
    
    print("\n--- Exercise 1: Temperature Converter ---")
    
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    print("def celsius_to_fahrenheit(celsius):")
    print("    fahrenheit = (celsius * 9/5) + 32")
    print("    return fahrenheit")
    
    temps_celsius = [0, 10, 20, 30, 100]
    print(f"\nConvert temperatures: {temps_celsius}")
    
    print("\nResults:")
    for c_temp in temps_celsius:
        f_temp = celsius_to_fahrenheit(c_temp)
        print(f"  {c_temp}°C = {f_temp:.1f}°F")
    
    print("\n--- Exercise 2: String Processor ---")
    
    def process_name(first, last):
        """Process name and return formatted version."""
        full_name = f"{first.capitalize()} {last.capitalize()}"
        initials = f"{first[0].upper()}.{last[0].upper()}."
        return full_name, initials
    
    print("def process_name(first, last):")
    print("    full_name = f'{first.capitalize()} {last.capitalize()}'")
    print("    initials = f'{first[0].upper()}.{last[0].upper()}.'")
    print("    return full_name, initials")
    
    print("\nProcessing names:")
    names = [("john", "doe"), ("alice", "smith"), ("bob", "johnson")]
    
    for first, last in names:
        full, init = process_name(first, last)
        print(f"  {first}, {last} -> Full: '{full}', Initials: '{init}'")
    
    print("\n--- Exercise 3: List Analysis ---")
    
    def summarize_list(items):
        """Return summary of list contents."""
        return {
            'count': len(items),
            'sum': sum(items),
            'average': sum(items) / len(items) if items else 0,
            'max': max(items) if items else None,
            'min': min(items) if items else None
        }
    
    print("def summarize_list(items):")
    print("    return {'count': ..., 'sum': ..., 'average': ..., 'max': ..., 'min': ...}")
    
    test_list = [5, 10, 15, 20, 25]
    print(f"\nAnalyzing list: {test_list}")
    
    summary = summarize_list(test_list)
    print(f"Results:")
    print(f"  Count: {summary['count']}")
    print(f"  Sum: {summary['sum']}")
    print(f"  Average: {summary['average']:.1f}")
    print(f"  Max: {summary['max']}")
    print(f"  Min: {summary['min']}")


# =====================================================================
# SECTION 8: COMMON MISTAKES AND HOW TO FIX THEM
# =====================================================================

def demonstrate_common_mistakes():
    """
    Show common mistakes with parameters and returns.
    """
    print("\n" + "="*70)
    print("SECTION 8: COMMON MISTAKES AND HOW TO FIX THEM")
    print("="*70)
    
    print("\n--- Mistake 1: Forgetting to Return ---")
    
    def add_numbers_WRONG(a, b):
        """Forgot to return the result."""
        result = a + b
        print(f"Sum is {result}")
        # Missing: return result
    
    print("WRONG:")
    print("def add_numbers_WRONG(a, b):")
    print("    result = a + b")
    print("    print(f'Sum is {result}')")
    print("    # Missing return statement!")
    
    print("\nCalling: x = add_numbers_WRONG(5, 3)")
    x = add_numbers_WRONG(5, 3)
    print(f"Value stored in x: {x}")
    print("PROBLEM: x is None, cannot use it!")
    
    def add_numbers_RIGHT(a, b):
        """Correctly returns the result."""
        result = a + b
        return result
    
    print("\n\nRIGHT:")
    print("def add_numbers_RIGHT(a, b):")
    print("    result = a + b")
    print("    return result")
    
    print("\nCalling: x = add_numbers_RIGHT(5, 3)")
    x = add_numbers_RIGHT(5, 3)
    print(f"Value stored in x: {x}")
    print("SUCCESS: x = 8, can be reused!")
    
    print("\n--- Mistake 2: Not Using Returned Values ---")
    
    def calculate_area(radius):
        """Calculate circle area."""
        area = 3.14159 * radius * radius
        return area
    
    print("def calculate_area(radius):")
    print("    area = 3.14159 * radius * radius")
    print("    return area")
    
    print("\nWRONG way - ignoring return value:")
    print("calculate_area(5)  # Returns value but doesn't store it")
    calculate_area(5)
    print("PROBLEM: Value is lost, cannot use it!")
    
    print("\nRIGHT way - storing returned value:")
    print("area = calculate_area(5)")
    area = calculate_area(5)
    print(f"area = {area:.2f}")
    print("SUCCESS: Can now use the area value!")
    
    print("\n--- Mistake 3: Parameter Name Confusion ---")
    
    def multiply(x, y):
        """Multiply two numbers."""
        result = x * y
        return result
    
    print("Function defined:")
    print("def multiply(x, y):")
    print("    result = x * y")
    print("    return result")
    
    print("\n[Call 1 - Correct]")
    print("result = multiply(3, 4)")
    result = multiply(3, 4)
    print(f"result = {result}")
    print("[OK] Parameter names (x, y) don't have to match (they're local to the function)")
    
    a = 10
    b = 5
    print("\n[Call 2 - Also Correct]")
    print("a = 10")
    print("b = 5")
    print("result = multiply(a, b)")
    result = multiply(a, b)
    print(f"result = {result}")
    print("[OK] Variables passed can have different names than parameters")


# =====================================================================
# SECTION 9: BEST PRACTICES FOR FUNCTION DATA FLOW
# =====================================================================

def demonstrate_best_practices():
    """
    Show best practices for clean function data flow.
    """
    print("\n" + "="*70)
    print("SECTION 9: BEST PRACTICES FOR FUNCTION DATA FLOW")
    print("="*70)
    
    print("\n--- Best Practice 1: Clear Parameter Names ---")
    print("[OK] GOOD: def calculate_monthly_payment(principal, annual_rate, months):")
    print("[FAIL] BAD:  def calc(p, r, m):")
    print("Reason: Clear names show what data is expected")
    
    print("\n--- Best Practice 2: Always Return Values (Not Print) ---")
    print("[OK] GOOD: return calculated_value")
    print("[FAIL] BAD:  print(calculated_value)")
    print("Reason: Enables reuse and composition")
    
    print("\n--- Best Practice 3: Consistent Parameter Types ---")
    
    def price_with_tax(amount, tax_rate=0.08):
        """Amount should always be numeric."""
        return amount * (1 + tax_rate)
    
    print("def price_with_tax(amount, tax_rate=0.08):")
    print("    return amount * (1 + tax_rate)")
    print("\nExpect: amount = number, tax_rate = number")
    print("Use consistently:")
    print(f"  price_with_tax(100) = {price_with_tax(100):.2f}")
    print(f"  price_with_tax(50.50) = {price_with_tax(50.50):.2f}")
    
    print("\n--- Best Practice 4: Return Early on Errors ---")
    
    def safe_divide(a, b):
        """Divide with error handling using returns."""
        if b == 0:
            return None  # Return early on error
        return a / b
    
    print("def safe_divide(a, b):")
    print("    if b == 0:")
    print("        return None")
    print("    return a / b")
    
    print("\nUsage:")
    print(f"  safe_divide(10, 2) = {safe_divide(10, 2)}")
    print(f"  safe_divide(10, 0) = {safe_divide(10, 0)}")
    print("Reason: Caller can check for None and handle appropriately")
    
    print("\n--- Best Practice 5: Document Parameters and Returns ---")
    
    def calculate_discount(price, discount_percent=10):
        """
        Calculate the discount amount from a price.
        
        Parameters:
            price (float): Original price
            discount_percent (float): Discount percentage (default 10)
        
        Returns:
            float: Discount amount
        """
        return price * (discount_percent / 100)
    
    print("def calculate_discount(price, discount_percent=10):")
    print('    """')
    print("    Calculate the discount amount from a price.")
    print("    ")
    print("    Parameters:")
    print("        price (float): Original price")
    print("        discount_percent (float): Discount percentage (default 10)")
    print("    ")
    print("    Returns:")
    print("        float: Discount amount")
    print('    """')
    print("    return price * (discount_percent / 100)")
    
    print("\nReason: Helps users understand what parameters to pass")
    print(f"Example: calculate_discount(100) = {calculate_discount(100):.2f}")


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "MILESTONE 6: FUNCTION DATA FLOW DEMONSTRATION".center(68) + "*")
    print("*" + "(Parameters and Return Values)".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    
    demonstrate_basic_parameters()
    demonstrate_keyword_arguments()
    demonstrate_storing_returned_values()
    demonstrate_multiple_returns()
    demonstrate_print_vs_return()
    demonstrate_data_flow_visualization()
    demonstrate_practice_exercises()
    demonstrate_common_mistakes()
    demonstrate_best_practices()
    
    print("\n" + "*"*70)
    print("*" + " " * 68 + "*")
    print("*" + "ALL DEMONSTRATIONS COMPLETE".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*"*70)
    print("\nKey Takeaways:")
    print("  • Functions accept data through PARAMETERS")
    print("  • Functions return data using the RETURN statement")
    print("  • RETURN enables reuse; print() does not")
    print("  • Multiple values can be returned as tuple or dict")
    print("  • Clear data flow makes code modular and composable")
    print("\n")
