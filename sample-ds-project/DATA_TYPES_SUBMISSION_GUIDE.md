# Milestone: Python Data Types Submission Guide

## Part A: Pull Request Submission

### What's Included in Your Script: `data_types_demonstration.py`

Your script demonstrates all required elements:

#### ✅ **Integer Variables**
```python
age = 28
product_count = 150
discount_percentage = 15
```

#### ✅ **Floating-Point Variables**
```python
price_per_unit = 29.99
tax_rate = 0.08
average_rating = 4.5
```

#### ✅ **Arithmetic Operations**
- Multiplication: `total_price = price_per_unit * product_count`
- Division: `average_price = total_price / product_count`
- Modulo & Integer Division: `remaining_items = product_count % 10`
- Compound operations with floats

#### ✅ **String Variables & Manipulation**
```python
first_name = "Alice"
last_name = "Johnson"
product_name = "Wireless Headphones"
```

#### ✅ **String Concatenation & Formatting**
- Concatenation: `full_name = first_name + " " + last_name`
- F-string formatting: `f"You purchased {quantity} units of {product_name}"`
- Multi-line strings with mixed types

#### ✅ **Type Mismatch & Explicit Conversion**
```python
# Problem: Type mismatch
item_price = 19.99  # float
quantity_as_string = "5"  # string
# total = item_price * quantity_as_string  # TypeError!

# Solution: Explicit conversion
quantity_as_int = int(quantity_as_string)
total = item_price * quantity_as_int  # ✓ Works!
```

### PR Submission Steps

1. **Commit the script:**
   ```bash
   git add sample-ds-project/scripts/data_types_demonstration.py
   git commit -m "feat: Add Python numeric and string data types demonstration"
   ```

2. **Create a Pull Request** with:
   - **Title:** "feat: Python Data Types Demonstration"
   - **Description:**
     ```
     This PR demonstrates comprehensive understanding of Python data types.
     
     **Demonstrates:**
     - Integer and float numeric variables
     - Basic arithmetic operations (multiply, divide, modulo)
     - String variables and concatenation
     - F-string formatting with mixed types
     - Type mismatch detection and explicit type conversion
     
     **Key Concepts Shown:**
     - Type() function to identify variable types
     - Implicit type behavior in operations
     - Explicit casting (int(), float(), str())
     - Real-world example: Invoice calculation
     ```

---

## Part B: Video Walkthrough Script (~2 minutes)

### What to Show in Your Video

**Setup (10 seconds):**
- Show the file in VS Code: `sample-ds-project/scripts/data_types_demonstration.py`
- Open terminal and navigate to the scripts directory

**Section 1: Numeric Data Types (25 seconds)**

1. Scroll to `demonstrate_numeric_types()` section
2. Point out:
   - Integer variables: age, product_count, discount_percentage
   - Float variables: price_per_unit, tax_rate, average_rating
   - Show that each has `type: int` or `type: float`
3. Highlight arithmetic operations:
   - "See how we multiply floats: 29.99 × 150 = 4498.5"
   - "Division always produces a float: 4498.5 / 150 = 29.99"
   - "Integer division with // gives us whole numbers"

**Section 2: String Data Types (25 seconds)**

1. Scroll to `demonstrate_string_types()` section
2. Point out string variables with meaningful values
3. Show string concatenation:
   - "Here we join strings with the + operator"
   - "All values must be strings for concatenation to work"
4. Show f-string formatting:
   - "F-strings let us embed variables inside strings"
   - "Notice how we can mix numbers and text cleanly"
5. Mention string methods: `.lower()`, `.upper()`, `len()`

**Section 3: Type Behavior & Conversion (35 seconds)**

1. Scroll to `demonstrate_type_behavior_and_conversion()` section
2. Explain the problem:
   - "Look here: we have a float price and a string quantity"
   - "If we try to multiply them directly... Python throws a TypeError"
   - "This is the TYPE MISMATCH problem"
3. Show the solution:
   - "We use int() to convert the string to an integer"
   - "Now the multiplication works: 19.99 × 5 = 99.95"
4. Show multiple conversion examples:
   - `int('25')` → integer
   - `float('5.9')` → float
   - `str(2026)` → string
   - Note that `int(29.99)` truncates the decimal

**Section 4: Practical Example (20 seconds)**

1. Run the script: `python data_types_demonstration.py`
2. Show the practical invoice output
3. Point out:
   - "Customer name is a string"
   - "Prices are floats with 2 decimal places"
   - "Quantity is an integer"
   - "All mixed together in one formatted output"

**Conclusion (5 seconds)**

- Summarize key takeaway: "Type matters in Python—integers, floats, and strings behave differently, and we must convert between them carefully"

---

## Video Recording Tips

### Technical Setup
1. Use OBS Studio or Windows built-in screen capture (Win + Shift + S → Video)
2. Record at 1080p minimum
3. Ensure clear audio (no background noise)
4. Speak clearly and at a moderate pace

### Execution Tips
1. **Before recording:** Run the script once to see the output
2. **During recording:**
   - Maximize text in VS Code (Ctrl + Plus sign)
   - Scroll slowly through code sections
   - Read the code comments aloud to explain logic
   - Point at specific lines with cursor or highlight text
3. **Pacing:** Take 2 minutes, not 1 minute—gives you room to explain clearly

### Script Talking Points
- "This section shows integer variables..."
- "Notice the type is 'int'..."
- "When we multiply floats, the result stays a float..."
- "This is where type conversion comes in..."
- "The int() function forces the string into an integer..."

---

## Submission Checklist

- [ ] Script is created: `data_types_demonstration.py`
- [ ] Script runs without errors
- [ ] Script demonstrates integers and floats
- [ ] Script demonstrates string operations
- [ ] Script shows type mismatch and conversion
- [ ] Pull Request is created with clear description
- [ ] Video is recorded (~2 minutes)
- [ ] Video explains all key concepts clearly
- [ ] Video demonstrates running the script
- [ ] Both PR and video link are submitted

---

## Common Questions Answered

**Q: Should the script be complex?**
A: No. Keep it simple and focused on showing data types clearly. The invoice example is enough complexity.

**Q: Do I need to load actual data?**
A: No. All data is hardcoded as sample values. That's fine for this milestone.

**Q: What if my video goes over 2 minutes?**
A: Aim for 2-3 minutes. Don't worry if you hit 2:15—focus on clarity over speed.

**Q: Should I edit the video?**
A: No editing needed. A simple screen recording is perfect.

---

## Next Steps

1. Submit the PR to your repository
2. Record and upload the video
3. Submit both the PR link and video link for grading
