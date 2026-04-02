"""
Python Numeric and String Data Types Demonstration

This script demonstrates core understanding of:
- Integer and floating-point numeric data types
- String data types and manipulation
- Arithmetic operations on numeric types
- String concatenation and formatting
- Type mismatches and explicit type conversion
"""


def demonstrate_numeric_types():
    """
    Demonstrate integer and floating-point numeric variables and operations.
    """
    print("\n" + "=" * 60)
    print("1. NUMERIC DATA TYPES DEMONSTRATION")
    print("=" * 60)

    # Integer variables
    print("\n--- Integer Variables ---")
    age = 28
    product_count = 150
    discount_percentage = 15

    print(f"age: {age} (type: {type(age).__name__})")
    print(f"product_count: {product_count} (type: {type(product_count).__name__})")
    print(f"discount_percentage: {discount_percentage} (type: {type(discount_percentage).__name__})")

    # Floating-point variables
    print("\n--- Floating-point Variables ---")
    price_per_unit = 29.99
    tax_rate = 0.08
    average_rating = 4.5

    print(f"price_per_unit: {price_per_unit} (type: {type(price_per_unit).__name__})")
    print(f"tax_rate: {tax_rate} (type: {type(tax_rate).__name__})")
    print(f"average_rating: {average_rating} (type: {type(average_rating).__name__})")

    # Arithmetic operations on numeric types
    print("\n--- Arithmetic Operations ---")
    total_price = price_per_unit * product_count
    print(f"Total price (price × quantity): {price_per_unit} × {product_count} = {total_price}")

    discounted_price = total_price * (1 - discount_percentage / 100)
    print(f"Discounted price (15% off): {total_price} * 0.85 = {discounted_price:.2f}")

    final_with_tax = discounted_price * (1 + tax_rate)
    print(f"Final price with tax: {discounted_price:.2f} * 1.08 = {final_with_tax:.2f}")

    # Division operations showing float results
    average_price = total_price / product_count
    print(f"\nAverage price per unit: {total_price} / {product_count} = {average_price}")

    # Integer division vs regular division
    remaining_items = product_count % 10
    complete_boxes = product_count // 10
    print(f"\nInteger division and modulo:")
    print(f"  {product_count} items ÷ 10 = {complete_boxes} complete boxes (with {remaining_items} remainder)")


def demonstrate_string_types():
    """
    Demonstrate string variables and string operations.
    """
    print("\n" + "=" * 60)
    print("2. STRING DATA TYPES DEMONSTRATION")
    print("=" * 60)

    # String variables with meaningful values
    print("\n--- String Variables ---")
    first_name = "Alice"
    last_name = "Johnson"
    product_name = "Wireless Headphones"
    company = "TechStore"

    print(f"first_name: '{first_name}' (type: {type(first_name).__name__})")
    print(f"last_name: '{last_name}' (type: {type(last_name).__name__})")
    print(f"product_name: '{product_name}' (type: {type(product_name).__name__})")

    # String concatenation
    print("\n--- String Concatenation ---")
    full_name = first_name + " " + last_name
    print(f"Concatenation: '{first_name}' + ' ' + '{last_name}' = '{full_name}'")

    welcome_message = company + " welcomes " + full_name + "!"
    print(f"Complex concatenation: '{welcome_message}'")

    # String formatting (f-strings)
    print("\n--- String Formatting with f-strings ---")
    price = 49.99
    quantity = 3
    formatted_message = f"You purchased {quantity} units of {product_name} at ${price} each."
    print(f"f-string: {formatted_message}")

    total = price * quantity
    formatted_invoice = f"""
    Receipt for {full_name}
    Product: {product_name}
    Quantity: {quantity}
    Unit Price: ${price}
    Total: ${total}
    """
    print(formatted_invoice)

    # String methods
    print("\n--- String Methods ---")
    lowercase = product_name.lower()
    uppercase = product_name.upper()
    character_count = len(product_name)

    print(f"Original: '{product_name}'")
    print(f"Lowercase: '{lowercase}'")
    print(f"Uppercase: '{uppercase}'")
    print(f"Length: {character_count} characters")


def demonstrate_type_behavior_and_conversion():
    """
    Demonstrate type mismatches and explicit type conversion.
    """
    print("\n" + "=" * 60)
    print("3. TYPE MISMATCH AND CONVERSION DEMONSTRATION")
    print("=" * 60)

    # Type mismatch example
    print("\n--- Type Mismatch Problem ---")
    item_price = 19.99
    quantity_as_string = "5"

    print(f"item_price: {item_price} (type: {type(item_price).__name__})")
    print(f"quantity_as_string: '{quantity_as_string}' (type: {type(quantity_as_string).__name__})")

    # This would cause an error if uncommented:
    # total = item_price * quantity_as_string  # TypeError!
    print("\n⚠️  Error if we try: item_price * quantity_as_string")
    print("   TypeError: can't multiply sequence by non-int of type 'float'")

    # Explicit type conversion
    print("\n--- Explicit Type Conversion (Casting) ---")
    quantity_as_int = int(quantity_as_string)
    print(f"int('{quantity_as_string}') = {quantity_as_int} (type: {type(quantity_as_int).__name__})")

    # Now the multiplication works
    total = item_price * quantity_as_int
    print(f"\n✓ Now it works: {item_price} * {quantity_as_int} = {total}")

    # More type conversions
    print("\n--- Additional Type Conversions ---")

    # String to integer
    age_string = "25"
    age_int = int(age_string)
    print(f"String to int: int('{age_string}') = {age_int}")

    # String to float
    height_string = "5.9"
    height_float = float(height_string)
    print(f"String to float: float('{height_string}') = {height_float}")

    # Integer to string
    year = 2026
    year_string = str(year)
    print(f"Integer to string: str({year}) = '{year_string}'")

    # Float to integer (truncates decimal)
    price = 29.99
    price_int = int(price)
    print(f"Float to int: int({price}) = {price_int} (decimal truncated)")

    # Float to string
    rating = 4.7
    rating_string = str(rating)
    print(f"Float to string: str({rating}) = '{rating_string}'")

    # Combining different types in strings (implicit conversion with f-strings)
    print("\n--- Type Mixing in String Formatting ---")
    product_id = 12345
    rating = 4.8
    stock_count = 47
    summary = f"Product ID: {product_id}, Rating: {rating}/5, In Stock: {stock_count} units"
    print(f"Mixed types in f-string: {summary}")


def demonstrate_practical_example():
    """
    Practical example combining all data type concepts.
    """
    print("\n" + "=" * 60)
    print("4. PRACTICAL EXAMPLE: CUSTOMER INVOICE")
    print("=" * 60)

    # Customer information (strings)
    customer_name = "Bob Smith"
    product_name = "Laptop Stand"
    order_id = "ORD-2026-001"

    # Numeric values
    unit_price = 34.50
    quantity = 2  # integer
    tax_rate = 0.10  # float
    shipping_cost = 5.99

    # Calculations
    subtotal = unit_price * quantity
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount + shipping_cost

    # Type conversion example: converting order_id to uppercase for display
    order_display = order_id.upper()

    # Building the invoice string with mixed types
    invoice = f"""
    ╔═══════════════════════════════════════╗
    ║           ORDER INVOICE               ║
    ╚═══════════════════════════════════════╝
    
    Order ID: {order_display}
    Customer: {customer_name}
    
    Items:
    ─────────────────────────────────────────
    Product:      {product_name}
    Unit Price:   ${unit_price:.2f}
    Quantity:     {quantity}
    Subtotal:     ${subtotal:.2f}
    
    Tax (10%):    ${tax_amount:.2f}
    Shipping:     ${shipping_cost:.2f}
    ─────────────────────────────────────────
    TOTAL:        ${total_amount:.2f}
    
    Note: Tax rate is {int(tax_rate * 100)}%
    """

    print(invoice)


if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("PYTHON DATA TYPES DEMONSTRATION")
    print("█" * 60)

    demonstrate_numeric_types()
    demonstrate_string_types()
    demonstrate_type_behavior_and_conversion()
    demonstrate_practical_example()

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("✓ Integers are whole numbers without decimals")
    print("✓ Floats are numbers with decimal points")
    print("✓ Strings are sequences of characters in quotes")
    print("✓ Arithmetic operations work only on compatible numeric types")
    print("✓ String concatenation requires strings on both sides")
    print("✓ Explicit type conversion (casting) resolves type mismatches")
    print("✓ F-strings allow mixing different types in formatted output")
    print("\n")
