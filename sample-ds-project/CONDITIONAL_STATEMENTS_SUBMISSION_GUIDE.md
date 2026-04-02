# Milestone: Python Conditional Statements Submission Guide

## Part A: Pull Request Submission

### What's Included in Your Script: `conditional_statements_demonstration.py`

Your script demonstrates all required elements across 7 comprehensive sections:

#### ✅ **1. Basic If Statements**

Single condition with no alternative:
```python
if age >= 18:
    print("You are an adult")
# If condition is False, nothing happens
```

**Examples shown:**
- Numeric comparison: `if age >= 18`
- String comparison: `if status == "active"`
- Membership testing: `if "admin" in permissions`

#### ✅ **2. If-Else Decision Branches (Two Paths)**

Two alternative branches—one always executes:
```python
if score >= 60:
    print("PASS")
else:
    print("FAIL")
```

**Examples shown:**
- Numeric if-else: Pass/Fail decision
- String if-else: Admin vs standard user
- Boolean if-else: Authenticated vs not

#### ✅ **3. If-Elif-Else (Multiple Conditions)**

Multiple branches—only first True condition executes:
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

**Examples shown:**
- Grade classification (A through F)
- Membership discount levels (gold, silver, bronze)
- Order of conditions matters!

#### ✅ **4. Logical Operators (AND, OR, NOT)**

Combining multiple conditions:

**AND operator** (both conditions must be True):
```python
if age >= 18 and has_license:
    print("Can drive")
```

**OR operator** (at least one condition must be True):
```python
if is_weekend or is_holiday:
    print("Day off!")
```

**NOT operator** (negates condition):
```python
if not is_available:
    print("Item unavailable")
```

**Complex combinations:**
```python
if age >= 21 and (income >= 30000 or credit_score >= 700):
    print("Loan approved")
```

#### ✅ **5. Data Type Considerations (Common Pitfalls)**

- String vs integer comparison (TypeError prevention)
- Case sensitivity in strings ("Active" vs "active")
- Whitespace in strings ("Alice " vs "Alice")
- Falsy values: False, 0, '', [], None
- Operator precedence: `if x < y < z`

#### ✅ **6. Practical Scenarios**

Real-world applications combining all concepts:
- E-commerce order validation
- User access control
- Product eligibility checks

#### ✅ **7. Debugging: "My Condition Is Always False!"**

Common mistakes and solutions:
- Using `=` instead of `==`
- Type mismatches
- Case sensitivity
- Incorrect condition order (specific before general)
- Logical operator confusion
- How to debug with print() statements

### PR Submission Steps

1. **Commit the script:**
   ```bash
   git add sample-ds-project/scripts/conditional_statements_demonstration.py
   git commit -m "feat: Add Python conditional statements demonstration"
   ```

2. **Create a Pull Request** with:
   - **Title:** "feat: Python Conditional Statements Demonstration"
   - **Description:**
     ```
     This PR demonstrates comprehensive understanding of conditional logic.
     
     **Demonstrates:**
     - Basic if statements for single conditions
     - if-else for two-branch decisions
     - if-elif-else for multiple conditions
     - Logical operators: and, or, not
     - Data type considerations in comparisons
     - Practical scenarios: validation, access control
     - Debugging techniques for condition issues
     
     **Key Concepts Shown:**
     - At least 10 different if/elif/else patterns
     - Multiple logical operator combinations
     - Real-world validation examples
     - Common pitfalls and debugging strategies
     ```

---

## Part B: Video Walkthrough Script (~2 Minutes)

### What to Show in Your Video

**Setup (10 seconds):**
- Open the file in VS Code
- Maximize text for clarity
- Have terminal ready

**Section 1: Basic If Statements (20 seconds)**

1. Scroll to `demonstrate_basic_if()` section
2. Explain:
   - "Here's a simple if statement"
   - "It checks if age is >= 18"
   - "When condition is True, code inside executes"
   - "When condition is False, nothing happens"
3. Show three examples:
   - Numeric comparison
   - String comparison
   - Membership testing (in operator)

**Section 2: If-Else Branching (20 seconds)**

1. Scroll to `demonstrate_if_else()` section
2. Explain:
   - "If-else gives us two paths"
   - "One branch always executes"
   - Show score example: "Above 60 passes, otherwise fails"
   - Show admin example: "Different logic for different roles"
3. Demonstrate:
   - What happens when true (pass branch)
   - What happens when false (fail branch)

**Section 3: If-Elif-Else (20 seconds)**

1. Scroll to `demonstrate_if_elif_else()` section
2. Explain:
   - "This handles multiple branches"
   - "Python tests each condition in order"
   - "Only the FIRST True condition executes"
   - Show grade classification: "A, B, C, D, or F"
3. Key point: "Order matters! Check specific conditions first"

**Section 4: Logical Operators (25 seconds)**

1. Scroll to `demonstrate_logical_operators()` section
2. Explain AND:
   - "AND means BOTH conditions must be True"
   - "Example: age >= 18 AND has_license to drive"
   - "If either is False, whole condition is False"
3. Explain OR:
   - "OR means AT LEAST ONE must be True"
   - "Example: is_weekend OR is_holiday to have day off"
   - "Only if BOTH are False does condition fail"
4. Explain NOT:
   - "NOT reverses/inverts the condition"
   - "Example: NOT is_available means item is unavailable"

**Section 5: Data Type Pitfalls (15 seconds)**

1. Scroll to `demonstrate_data_type_considerations()` section
2. Show:
   - String "25" vs integer 25 (can't compare directly)
   - Case sensitivity: "Active" != "active"
   - Whitespace: "Alice " != "Alice"
   - Falsy values: 0, "", [], False all act like False in conditions

**Section 6: Debugging Scenario (MANDATORY) (~30 seconds)**

This MUST be answered verbally in your video. Answer this question:

**"A condition in your code always evaluates to False, even when you expect it to be True. What common mistakes could cause this, and how would you debug and fix the issue?"**

Your answer should address:
1. **Comparison operators:** Using `=` instead of `==` (assignment vs comparison)
2. **Data types:** String "100" vs integer 100 won't compare the same way
3. **Logical operators:** Using `or` when you meant `and` changes the logic
4. **Indentation:** Python uses indentation to define code blocks
5. **Condition order:** First matching `if` executes, so order in if-elif-else matters

**Example answers you could include:**
- "I might be comparing different data types—a string to a number"
- "I might have used = (assignment) instead of == (comparison)"
- "I could use print() to debug: print the variable and the condition result"
- "I might have my if-elif conditions in wrong order"
- "The condition might have a logical operator I didn't think through"

**Practical debugging example to walk through:**
```python
# WRONG: Always False
value = "25"
if value > 18:  # TypeError!

# FIXED: Convert first
if int(value) > 18:  # True now!
```

---

## Video Recording Tips

### Technical Setup
1. Use OBS Studio or Windows built-in screen capture (Win + Shift + S)
2. Record at 1080p
3. Close unnecessary windows
4. Maximize VS Code text (Ctrl + Plus)

### Execution Tips
1. **Before recording:** Run script once to preview output
2. **During recording:**
   - Point at code with cursor
   - Scroll slowly through sections
   - Highlight important logic
   - Speak clearly and at moderate pace
3. **Pacing:** Aim for 2-2:30 minutes total

### Script Checklist
- [ ] Show basic if statement and explain when it executes
- [ ] Show if-else and explain both paths
- [ ] Show if-elif-else with multiple branches
- [ ] Demonstrate AND operator (both must be true)
- [ ] Demonstrate OR operator (one must be true)
- [ ] Demonstrate NOT operator (inverts)
- [ ] Show at least one data type pitfall
- [ ] **VERBALLY ANSWER the debugging scenario question**
- [ ] Reference comparison operators in your answer
- [ ] Reference data types in your answer
- [ ] Reference logical operators in your answer
- [ ] Mention debugging techniques (like print())

---

## Submission Checklist

- [ ] Script created: `conditional_statements_demonstration.py`
- [ ] Script runs without errors
- [ ] Basic if statements shown and explained
- [ ] If-else branching shown and explained
- [ ] If-elif-else with 3+ conditions shown
- [ ] AND operator demonstrated with example
- [ ] OR operator demonstrated with example
- [ ] NOT operator demonstrated with example
- [ ] Data type pitfalls section completed
- [ ] Pull Request created with description
- [ ] Video recorded (~2-2:30 minutes)
- [ ] Video covers all required sections
- [ ] **Video includes verbal answer to debugging scenario**
- [ ] Debugging answer references comparison operators
- [ ] Debugging answer references data types
- [ ] Debugging answer references logical operators
- [ ] Both PR and video links submitted

---

## Common Questions Answered

**Q: What's the difference between `=` and `==`?**
A: `=` assigns a value, `==` compares values. Conditionals need `==`.

**Q: Can I use `if` without `else`?**
A: Yes! `if` alone is valid. `else` is optional.

**Q: What's the difference between `elif` and `else if`?**
A: Python uses `elif`, not `else if`. Must use correct spelling.

**Q: Does `and` execute both conditions?**
A: No, Python stops when it finds the result (short-circuit evaluation).

**Q: Will the video be graded on production quality?**
A: No—focus on clear explanation and correct answers.

**Q: Can I use the script's examples in my video?**
A: Yes! The script is designed for walkthrough in a video.

---

## Next Steps

1. Run the script to understand all examples
2. Record your ~2 minute video (be sure to answer the debugging scenario)
3. Create the feature branch and push to GitHub
4. Create a Pull Request
5. Submit PR and video links for grading
