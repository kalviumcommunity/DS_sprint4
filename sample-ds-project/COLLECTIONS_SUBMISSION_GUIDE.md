# Milestone: Python Collections Submission Guide

## Part A: Pull Request Submission

### What's Included in Your Script: `collections_demonstration.py`

Your script demonstrates all required elements across 5 comprehensive sections:

#### ✅ **Lists: Creation, Access, and Modification**

**Creation:**
```python
fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]
```

**Access by Index:**
```python
first = fruit_list[0]       # "apple"
last = fruit_list[-1]        # "elderberry"
slice = fruit_list[1:4]      # ["banana", "cherry", "date"]
```

**Modification (Mutable):**
```python
fruit_list.append("fig")                    # Add to end
fruit_list.insert(2, "blueberry")          # Insert at index
fruit_list.remove("blueberry")             # Remove by value
fruit_list[0] = "apricot"                  # Change element
removed = fruit_list.pop()                 # Remove and return last
```

**Key Operations:**
- `len()`, `sum()`, `max()`, `min()`
- `sort()`, `index()`, `count()`
- Slicing, iteration, enumeration

#### ✅ **Tuples: Fixed Values and Immutability**

**Creation:**
```python
coordinates = (40.7128, -74.0060)
color_tuple = ("red", "green", "blue")
single_tuple = ("only_one",)  # Requires trailing comma!
```

**Access by Index:**
```python
first = coordinates[0]    # 40.7128
last = colors[-1]         # "orange"
slice = colors[1:4]       # ("green", "blue", "yellow")
```

**Immutability Demonstrated:**
```python
# This FAILS:
numbers[0] = 100  # TypeError: 'tuple' object does not support item assignment

# But you CAN create a new tuple:
new_tuple = numbers + (40,)
```

**Unpacking:**
```python
x, y = coordinates              # Unpack 2 values
name, age, job = person        # Unpack 3 values
```

**Operations:**
- `len()`, `count()`, `index()`
- `sum()`, `max()`, `min()`
- Slicing, iteration

#### ✅ **Dictionaries: Key-Value Pairs**

**Creation with Meaningful Keys:**
```python
student = {
    "name": "Bob",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "enrolled": True
}
```

**Access by Key:**
```python
name = student["name"]              # "Bob"
age = student.get("age")            # 20 (safe)
city = student.get("city", "Unknown")  # "Unknown" (provides default)
```

**Modification (Mutable):**
```python
student["age"] = 21         # Modify existing value
student["city"] = "Boston"  # Add new key-value pair
del student["enrolled"]     # Delete key-value pair
```

**Key Methods:**
```python
keys = student.keys()       # All keys
values = student.values()   # All values
items = student.items()     # Key-value pairs
```

**Key Characteristics:**
- Keys must be unique
- Keys must be immutable (strings, numbers, tuples work; lists don't)
- Values can be any data type (including other dicts!)

#### ✅ **Nested Structures**

```python
product = {
    "id": 101,
    "colors": ["black", "white", "silver"],  # List as value
    "specs": {                                # Dict as value
        "battery": "2 AA",
        "dpi": 1600
    }
}

# Access nested values:
first_color = product["colors"][0]           # "black"
battery_type = product["specs"]["battery"]   # "2 AA"
```

#### ✅ **Collection Comparison Table**

The script includes a comparison showing:
- Mutability: Lists ✓, Tuples ✗, Dicts ✓
- Ordered: Lists ✓, Tuples ✓, Dicts ✓ (Python 3.7+)
- Indexed: Lists ✓, Tuples ✓, Dicts (by key)
- Performance characteristics

#### ✅ **Practical Example: Student Management System**

Demonstrates using all three collections together:
```python
students_data = {
    "S001": {
        "name": "Alice",
        "grades": [95, 87, 92],          # List for mutable data
        "courses": ("Math", "Physics"),   # Tuple for fixed data
        "contact": ("email", "phone")     # Tuple for coordinates
    }
}
```

### PR Submission Steps

1. **Commit the script:**
   ```bash
   git add sample-ds-project/scripts/collections_demonstration.py
   git commit -m "feat: Add Python collections (lists, tuples, dicts) demonstration"
   ```

2. **Create a Pull Request** with:
   - **Title:** "feat: Python Collections Demonstration"
   - **Description:**
     ```
     This PR demonstrates comprehensive understanding of Python collections.
     
     **Demonstrates:**
     - Lists: creation, access by index, modification (mutable)
     - Tuples: creation, access, immutability constraints
     - Dictionaries: creation, key-value access, modification
     - Nested collections combining lists, tuples, and dicts
     - Practical data structure patterns
     
     **Key Concepts Shown:**
     - Indexed access vs key-based access
     - Mutable vs immutable behavior
     - When to use each collection type
     - Real-world patterns: student records, inventory, settings
     ```

---

## Part B: Video Walkthrough Script (~2 minutes)

### What to Show in Your Video

**Setup (10 seconds):**
- Open the file in VS Code: `sample-ds-project/scripts/collections_demonstration.py`
- Maximize text for clarity
- Have terminal ready to run the script

**Section 1: Lists (30 seconds)**

1. Scroll to `demonstrate_lists()` section
2. Point out:
   - **Creation:** "Here's a list with five fruits"
   - **Access:** "Lists are indexed starting at 0, so the first element is at index 0"
   - Show accessing by positive index `[0]`, negative index `[-1]`, and slicing `[1:4]`
3. **Modification Examples:**
   - `append()`: "Adding to the end"
   - `insert()`: "Inserting at a specific position"
   - Direct assignment: "Changing an element at index 0"
   - `remove()` and `pop()`: "Lists are mutable—we can remove items"
4. Highlight: "Notice we can change, add, and remove items from lists"

**Section 2: Tuples (30 seconds)**

1. Scroll to `demonstrate_tuples()` section
2. **Creation:**
   - "Tuples look similar to lists, but use parentheses"
   - Show single-element tuple with trailing comma
3. **Access (similar to lists):**
   - "Like lists, tuples use zero-based indexing"
   - "And we can slice them too"
4. **Immutability:**
   - Scroll to "Immutability" section
   - "Here's the big difference: When we try to modify a tuple, Python throws an error"
   - Point to the TypeError message
   - "Tuples can't be changed—they're immutable"
5. **Unpacking:**
   - "But tuples are great for unpacking—assigning multiple values at once"
   - Show: `x, y = coordinates`

**Section 3: Dictionaries (35 seconds)**

1. Scroll to `demonstrate_dictionaries()` section
2. **Creation:**
   - "Dictionaries use curly braces and store key-value pairs"
   - "Notice meaningful keys: 'name', 'age', 'major'"
3. **Access by Key:**
   - "Instead of index numbers, we use keys"
   - Show: `student['name']` vs `student[0]`
   - Mention `.get()` for safe access
4. **Modification:**
   - "Dictionaries are mutable—we can change values"
   - Show changing: `student['age'] = 21`
   - Show adding new keys: `student['city'] = "Boston"`
5. **Nested Data:**
   - Scroll to product example with nested dict
   - "We can put lists and even other dictionaries inside dictionaries"
   - Show accessing: `product['specs']['battery']`
6. **Iteration:**
   - "We can loop through dictionaries"
   - Show `.items()` for key-value pairs

**Section 4: Comparison Table (10 seconds)**

1. Scroll to comparison table
2. Briefly explain:
   - "Each collection is best for different purposes"
   - "Lists are best when you need to modify things"
   - "Tuples are best for fixed data and as dictionary keys"
   - "Dictionaries are best for looking up values by name"

**Section 5: Practical Example (10 seconds)**

1. Scroll to student management system
2. "Here's a real example combining all three"
3. Run the script to show the output
4. Point out how lists, tuples, and dicts work together

**Conclusion (5 seconds):**

- "The key difference: mutability determines when to use each"
- "Lists change, tuples don't, dictionaries use keys instead of indexes"

---

## Video Recording Tips

### Technical Setup
1. Use OBS Studio or Windows built-in screen capture (Win + Shift + S)
2. Record at 1080p
3. Close unnecessary windows/tabs
4. Maximize VS Code text (Ctrl + Plus to zoom in)

### Execution Tips
1. **Before recording:** Run the script once to preview output
2. **During recording:**
   - Scroll slowly through code sections
   - Point at code with cursor
   - Use color highlighting or text selection to emphasize concepts
   - Pause briefly at important sections
3. **Pacing:** Aim for 2-2:30 minutes—enough to be clear without rushing

### Talking Points Checklist
- [ ] Mention list creation and zero-based indexing
- [ ] Show at least 2 list modifications (add, remove, change)
- [ ] Explain why tuples have a trailing comma for single elements
- [ ] Demonstrate tuple immutability and the error it causes
- [ ] Show dictionary creation with meaningful keys
- [ ] Show accessing values with keys, not indexes
- [ ] Demonstrate adding a new key-value pair
- [ ] Mention when to use each collection type
- [ ] Show nested structures working together

---

## Submission Checklist

- [ ] Script is created: `collections_demonstration.py`
- [ ] Script runs without errors
- [ ] Lists section shows creation, access, and modification
- [ ] Tuples section shows creation, access, and immutability
- [ ] Dictionaries section shows creation, key access, and modification
- [ ] Nested structures combining all three types are shown
- [ ] Pull Request is created with clear description
- [ ] Video is recorded (~2 minutes)
- [ ] Video covers all three collection types
- [ ] Video shows immutability error for tuples
- [ ] Video explains when to use each type
- [ ] Both PR and video links are submitted

---

## Common Questions Answered

**Q: Can I use list as a dictionary key?**
A: No—only immutable types can be keys. Use tuples instead.

**Q: What's the difference between `.remove()` and `.pop()`?**
A: `remove()` removes a value, `pop()` removes by index and returns the value.

**Q: Why do I need a trailing comma for single-element tuples?**
A: `("one")` is a string wrapped in parentheses. `("one",)` is a tuple.

**Q: Can dictionaries be nested?**
A: Yes! You can have dicts inside dicts, lists inside dicts, etc.

**Q: Will the video be graded on production quality?**
A: No—focus on clear explanation, not polished editing.

---

## Next Steps

1. Create a new feature branch for this milestone
2. Commit the script with a proper commit message
3. Push to GitHub
4. Create a Pull Request
5. Record your ~2 minute video walkthrough
6. Submit both PR and video links for grading
