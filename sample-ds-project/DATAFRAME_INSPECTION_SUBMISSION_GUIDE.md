# Milestone 17: Inspecting DataFrames Using head(), info(), and describe() - Submission Guide

## Overview
This milestone evaluates your ability to **inspect Pandas DataFrames** using three critical methods: `head()`, `info()`, and `describe()`. The focus is on understanding dataset structure, data types, and basic statistics **before any cleaning or analysis**.

**Key Focus:** Correct inspection, identification of data quality issues, and understanding what each method reveals about your data.

---

## Part A: What This Milestone Demonstrates

### Section 1: Introduction to DataFrame Inspection
- **Concept:** Inspection = Understanding your data BEFORE analysis
- **Three methods:** head() (preview), info() (structure), describe() (statistics)
- **Why essential:** Catch loading errors, understand structure, identify quality issues
- **When:** ALWAYS immediately after loading

### Section 2: Using head() for Data Preview
- **Purpose:** Quick visual check of actual data rows (default: first 5 rows)
- **What to look for:** Column names, value reasonableness, weird characters, apparent errors
- **Variations:** head(3) for fewer rows, head(0) for just column names, head(-2) for all except last 2
- **Also:** tail() for last rows, sample() for random rows

### Section 3: Variations of head() and tail()
- **tail():** Shows last N rows (compare to first rows for consistency)
- **Combining:** head(1) + tail(1) to check bookends
- **iloc/loc:** Access specific rows as Series for detailed inspection
- **sample():** Random rows with reproducibility via random_state

### Section 4: Using info() for Structure Inspection
- **Purpose:** Display DataFrame structure and metadata
- **Shows:** Columns, data types (dtypes), non-null counts, memory usage
- **THE CRITICAL METHOD:** Most important for catching data quality issues
- **Output components:** RangeIndex, data columns list, dtype summary

### Section 5: Understanding Data Types (dtypes)
- **Key types:**
  - int64, float64: Numeric (can do math)
  - object: Strings or mixed (cannot do math)
  - bool: True/False
  - datetime64: Dates/times
  - category: Categorical data
- **Why concern:** object when should be int64 = silent error
- **Detection:** info() dtypes column or df.dtypes directly

### Section 6: Using describe() for Statistical Summary
- **Purpose:** Statistical summary of numeric columns only
- **Shows:** count, mean, std, min, 25%, 50%, 75%, max
- **Why important:** Understand data ranges, distributions, and spot outliers
- **With include='all':** Describes all columns (adds unique, top, freq for non-numeric)

### Section 7: Comparing Inspection Methods
- **head():** Use when need actual data rows (spot-check content)
- **info():** Use when need structure (find wrong types, missing values)
- **describe():** Use when need statistics (understand ranges, distributions)
- **Workflow order:** 1) head() → 2) info() → 3) describe()

### Section 8: The Scenario - Detecting Misloaded Data Types (CRITICAL)
**Scenario:** You begin analysis and discover numeric column was loaded as string (object).

**How info() prevents this:**
1. After loading, run df.info()
2. Check each column's expected dtype
3. If dtype doesn't match expectation → RED FLAG
4. Example: Age should be int64, but info() shows object
5. Cause: Non-numeric value like 'twenty-one' in Age column

**Why early inspection saves time:**
- Without inspection: Load → Analyze → Error at df['Age'].mean() → Debug for hours
- With inspection: Load → info() → See Age is object → Find 'twenty-one' → Fix → 5 minutes total

### Section 9: Complete Inspection Workflow
**Standard 3-Step Workflow (40 seconds total):**

1. **Step 1: head()** (15 seconds)
   - Ask: Does this look like real data?
   - Check for obvious errors, weird formats

2. **Step 2: info()** (15 seconds) - THE CRITICAL STEP
   - Ask: Are column types correct?
   - Check for object columns that should be numeric
   - Verify non-null counts indicate missing data

3. **Step 3: describe()** (10 seconds)
   - Ask: Do values make sense?
   - Check for unexpected ranges, outliers

**Result:** Confidence that data is trustworthy before analysis

### Section 10: Common Inspection Patterns
- **Pattern 1:** Column shows 7 non-null in 8 rows → 1 missing value
- **Pattern 2:** Column dtype is object when should be int64 → Data entry error or loading issue
- **Pattern 3:** Unexpected column name like 'Unnamed: 7' → CSV formatting issue
- **Pattern 4:** Date column is object, not datetime64 → Need parse_dates parameter
- **Pattern 5:** describe() shows max >> mean → Possible outliers

### Section 11: Best Practices for Data Inspection
1. **Always inspect immediately** after loading (never skip)
2. **Make it reflex:** Develop automatic habit
3. **Document expectations** before loading
4. **Check specific columns** when suspicious: unique(), value_counts(), isna().sum()
5. **Use verbose info()** for detailed output
6. **Create inspection summary** document
7. **Compare head() and tail()** for consistency
8. **Automate inspection** with a reusable function
9. **Question everything:** Never assume data is correct
10. **Document findings:** Data quality assessment, issues, actions taken

---

## Part B: Video Script (~2 Minutes)

### Opening (15 seconds)
"In this milestone, we're learning the three essential methods for inspecting Pandas DataFrames: head(), info(), and describe(). These aren't optional—they're foundational. In just 40 seconds of inspection, you can catch data quality issues that would otherwise waste hours of debugging. Let's see how."

### Section 1: Using head() (20 seconds)
"First, let's preview the data with head(). [Show head() output] This shows me the first 5 rows by default. I can immediately see if values look reasonable. Column names look good. The data appears to be student records. Notice the mixed data types—StudentID is numeric, Name is text, Enrolled is True/False. This visual check is quick but powerful."

### Section 2: Using info() - THE CRITICAL STEP (35 seconds)
"Now the most important step: info(). [Show info() output] This tells me the complete structure:
- 8 rows total
- 7 columns with their data types
- All columns have 8 non-null values (no missing data)
- StudentID is int64 (numeric)
- Name is str (string)
- Age is int64 (numeric) - this is important
- Enrolled is bool (True/False)

Here's why this matters: If Age showed up as 'object' instead of 'int64', I'd know something went wrong during loading. An object type for a numeric column means corrupted data. With info(), I catch this immediately."

### Section 3: Using describe() (20 seconds)
"Finally, describe() shows statistics for numeric columns. [Show describe() output]
- Age ranges from 19 to 23 (reasonable for students)
- GPA ranges from 2.9 to 3.9 (realistic GPA range)
- ExamScore ranges from 79 to 95 (reasonable test scores)
- Mean GPA is 3.5, which is a solid average

This tells me the data looks reasonable. No unexpected outliers. No suspicious ranges."

### Section 4: The Scenario (35 seconds)
"Now here's the critical scenario: What if during analysis, I discovered that Age was loaded as a string instead of a number? [Show problem file with 'twenty-one' mixed in]

This would break my analysis—any math operation on Age would fail. But how could info() have prevented this?

When I run info() on this problematic data, it immediately shows Age dtype as 'object' instead of 'int64'. That's the RED FLAG. [Show info() output] I see Age is object type when it should be numeric. I then:

1. Open the CSV file directly
2. Find the culprit: 'twenty-one' mixed in with numbers
3. Either clean the data or reload with dtype={'Age': 'int64'} to force an error
4. Fix the issue BEFORE analysis

Without early inspection: Hours of debugging
With early inspection: 5 minutes to fix

The inspection workflow catches this immediately."

### Section 5: Key Takeaways (15 seconds)
"Remember: 40 seconds of inspection saves hours of debugging. Always run:
1. head() - to see the data
2. info() - to check types
3. describe() - to verify values

Make this automatic. Every single time. It's the difference between professional data work and wasted time."

### Closing (5 seconds)
"You now have the tools to safely inspect any DataFrame!"

---

## Part C: Scenario-Based Reasoning (MANDATORY in Video)

### Scenario Question
**"You begin analysis and later discover that a numeric column was actually loaded as a string (object type). How could using info() earlier have helped prevent this issue, and what would you look for during inspection?"**

### Expected Answer (Include ALL Points)

**Point 1: info() Shows the Problem Immediately**
"The moment I run df.info(), I would see the data types for all columns. If a column I expected to be int64 or float64 shows up as 'object', that's an immediate red flag. For example, if Age shows dtype='object' instead of dtype='int64', I know something is wrong."

**Point 2: What to Look For During Inspection**
"When inspecting with info(), I specifically ask for each numeric column:
- Is this column dtype int64 or float64? (If yes, good)
- Or is it object? (If yes, problem detected!)
- If object, why? It must contain non-numeric values somewhere

I would never skip this check. It takes 15 seconds and prevents hours of debugging."

**Point 3: The Detection Workflow**
"Here's what happens:
1. Load data: df = pd.read_csv('file.csv')
2. Run info(): df.info()
3. Scan dtypes column: Age shows 'object' - ALERT!
4. Next steps: Check the actual values
5. Find the problem: Maybe one row has 'twenty-one' instead of 21
6. Fix it: Either clean the data or use dtype parameter during loading"

**Point 4: Prevention with dtype Parameter**
"The best approach is to specify expected data types during loading:
```python
df = pd.read_csv('file.csv', dtype={'Age': 'int64'})
```
This forces an error if Age contains non-numeric values—catching the problem at load time instead of during analysis."

**Point 5: Why This Saves Time**
"Without early inspection the workflow is:
- Load data → Begin analysis → df['Age'].mean() → TypeError
- Now I must debug: 'Why is this failing?'
- Opens file, finds the problem, re-loads, repeats analysis
- Wasted time: 2-3 hours

With early inspection the workflow is:
- Load data → df.info() → See Age is object
- Immediately fix the data or reload with dtype
- Analysis proceeds without errors
- Time spent: ~5 minutes"

**Point 6: info() vs Other Methods**
"Why is info() the most important?
- head() shows actual data but doesn't reveal dtype issues if they're subtle
- info() directly shows data types—no ambiguity
- describe() is for statistics but won't catch the root cause
- Only info() catches 'numeric column loaded as string'"

**Point 7: Non-Null Counts in info()**
"info() also shows non-null counts. If I see:
- Age: 7 non-null (out of 8 rows)
- This means 1 missing value

This is another quality check. Early detection means I can decide how to handle missing data before analysis."

**Point 8: The Professional Standard**
"This is what professional data scientists do:
1. Load data
2. Immediately run head(), info(), describe()
3. Review the output carefully
4. Only proceed if everything looks right
5. If problems found, fix before proceeding

Skipping inspection is like building a house on sand. The more complex your analysis, the worse the disaster when bad data causes silent errors."

---

## Part D: Pull Request Template

```markdown
# Pull Request: Milestone 17 - Inspecting DataFrames Using head(), info(), and describe()

## Description
This PR demonstrates safe DataFrame inspection using three critical methods (head(), info(), describe()) to understand dataset structure, identify data type errors, and verify data quality before analysis.

## Changes
- Created `dataframe_inspection_demonstration.py` showcasing:
  - 11 comprehensive sections covering all inspection aspects
  - The critical 3-step inspection workflow (head → info → describe)
  - head() variations: tail(), sample(), iloc/loc access
  - info() output interpretation and dtype detection (THE CRITICAL METHOD)
  - describe() statistical summaries and outlier detection
  - The scenario: detecting numeric column loaded as string
  - Common inspection patterns and how to recognize them
  - Best practices for professional data inspection
  - 40-second workflow verification checklist

## Testing
- Script executes without errors (exit code 0)
- All 11 demonstration sections run successfully
- Shows head(), info(), describe() outputs
- Demonstrates problem detection workflow
- All code examples tested and verified working

## Verification Checklist
- [x] head() method with variations (default, custom count, negative indexing)
- [x] tail() method for last rows comparison
- [x] info() output interpretation (RangeIndex, dtype, non-null counts)
- [x] dtypes inspection (int64 vs object, float64 vs object)
- [x] describe() statistical summaries
- [x] Comparing all three methods
- [x] The scenario: detecting type mismatch
- [x] Complete 3-step inspection workflow (40 seconds)
- [x] Common inspection patterns (missing data, wrong types, outliers)
- [x] Best practices and automation
- [x] Script runs without errors

## Key Learnings
1. **head() method:** Quick visual preview of first N rows (default 5)
2. **info() method (CRITICAL):** Only way to catch wrong data types
3. **describe() method:** Statistical summary for numeric columns
4. **The 3-step workflow:** head() → info() → describe() takes ~40 seconds
5. **The scenario:** Numeric column as object = silent data corruption risk
6. **Prevention:** Use info() immediately after load, check dtypes match expectations
7. **Professional standard:** Never skip inspection—make it reflexive habit
8. **Time savings:** 40 seconds inspection vs hours of debugging
9. **Red flags:** object dtype for numeric column, non-null count < total rows
10. **Automation:** Create inspection function for reusable workflow

## Related Issues
Milestone 17 in DS Sprint 4

## Related Video
[Link to recorded video walkthrough] - Shows all three inspection methods with scenario-based example

---
**Reviewer Notes:**
- Verify all three methods demonstrated clearly
- Check scenario answer is comprehensive
- Confirm 3-step workflow is well-explained
- Ensure best practices section is thorough
```

---

## Part E: FAQ (Frequently Asked Questions)

### head() Method
**Q1: What's the default for head()?**
A: head() with no arguments returns the first 5 rows. head(3) returns first 3, head(10) returns first 10.

**Q2: What's the difference between head() and tail()?**
A: head() shows first N rows, tail() shows last N rows. Use both to check bookends of your data.

**Q3: What does head(0) do?**
A: Returns just the column names with empty DataFrame. Useful to see structure without any data rows.

**Q4: Can I use head(-2)?**
A: Yes—head(-2) returns all rows EXCEPT the last 2. Similarly, tail(-2) returns all rows EXCEPT the first 2.

### info() Method (THE CRITICAL ONE)
**Q5: What's info() and why is it so important?**
A: info() shows DataFrame structure: columns, data types, non-null counts, memory. It's the ONLY way to catch numeric columns loaded as object (string) type.

**Q6: What does "int64" mean in info() output?**
A: int64 = 64-bit integer (numeric, can do math). Other numeric types: float64 (decimals), uint8, uint16, etc.

**Q7: What does "object" type mean?**
A: object = Unknown/mixed types, usually strings. If numeric column shows object, it means non-numeric values loaded in that column.

**Q8: How do I spot missing data in info()?**
A: If "Non-Null Count" < total rows, that column has missing data. Example: Column shows "7 non-null" in 8-row DataFrame = 1 missing value.

**Q9: What does memory usage mean?**
A: Memory usage shows how much RAM this DataFrame uses in memory. float64 columns use more than int32 columns. Useful for large datasets.

**Q10: Should I run info() before or after head()?**
A: Run head() first (quick visual), then info() second (structure check). Order: head() → info() → describe().

### describe() Method
**Q11: What does describe() show?**
A: Statistical summary of numeric columns: count, mean, std (standard deviation), min, 25%, 50% (median), 75%, max.

**Q12: What if I want describe() for non-numeric columns too?**
A: Use describe(include='all'). This adds 'unique', 'top', 'freq' for object/string columns.

**Q13: What does the "25%" row mean in describe()?**
A: That's the 25th percentile—the value where 25% of data falls below it. Similarly, 50% is median, 75% is 75th percentile.

**Q14: How do I interpret std (standard deviation) in describe()?**
A: High std = data spread out widely. Low std = data clustered tightly around the mean.

**Q15: Can I customize percentiles in describe()?**
A: Yes: df.describe(percentiles=[0.1, 0.5, 0.9]) shows 10th, 50th, 90th percentiles instead of defaults.

### The Critical Scenario
**Q16: Why would a numeric column load as object?**
A: Usually one non-numeric value in that column (like 'twenty-one' mixed with numbers, or symbols like '$1000' in a price column).

**Q17: How does info() catch the misloaded type?**
A: When you look at the dtypes column in info() output, you expect Age to show int64. If it shows object instead, that's the red flag that something went wrong.

**Q18: What should I do if info() shows wrong dtype?**
A: 1) Open the CSV file directly to see what's there
2) Find the problematic values
3) Either clean the data or reload with dtype={'Age': 'int64'} to catch the error at load time

**Q19: Can I change dtype after loading?**
A: Yes: df['Age'] = df['Age'].astype('int64'). But this fails if column contains non-numeric values. Better to fix at load time.

**Q20: Why is catching this early so important?**
A: Because numerical operations will silently fail or produce wrong results. df['Age'].sum() would crash with TypeError instead of returning a number.

### Inspection Workflow
**Q21: How long should inspection take?**
A: About 40 seconds: head() (15 sec) + info() (15 sec) + describe() (10 sec). Fast but critical.

**Q22: Should I inspect every DataFrame?**
A: YES. Without exception. Even if you created it yourself from scratch. Make it automatic habit.

**Q23: What's the complete inspection workflow?**
A: 1) df.head() → Check visual appearance
2) df.info() → Check dtypes and nulls
3) df.describe() → Check statistics
4) Ask: "Does this look right?" If not, investigate before proceeding.

**Q24: What common problems does inspection reveal?**
A: Wrong dtypes (numeric as object), missing values (non-null count < total), unexpected columns, unusual value ranges, encoding issues.

**Q25: How do I create an automated inspection function?**
A:
```python
def inspect(df, name='DataFrame'):
    print(f"\n=== {name} Inspection ===")
    print(f"Shape: {df.shape}")
    print(f"Missing: {df.isna().sum().sum()}")
    df.info()
    print(df.describe())
    
inspect(df, 'Student Data')
```

---

## Summary

**Milestone Completion Checklist:**
- ✅ Load DataFrame (from CSV or create)
- ✅ Use head() to preview rows
- ✅ Use info() to inspect structure and data types (CRITICAL)
- ✅ Use describe() to summarize numeric columns
- ✅ Explain inspection results clearly in video
- ✅ Answer scenario about detecting misloaded data type
- ✅ No data cleaning or analysis performed
- ✅ Focus purely on inspection and verification

**Submission Requirements:**
1. Pull Request with the demonstration script
2. Video walkthrough (~2 minutes) including scenario answer
3. All three methods demonstrated with examples
4. Clear explanation of what each method reveals

**The 3-Step Inspection Workflow (40 seconds):**
```
Load → head() → info() → describe() → Decide → Proceed or Fix
```

**Key Rules:**
1. **Never skip inspection:** Make it automatic
2. **Check info() FIRST for dtypes:** This is the critical step
3. **Match expectations:** If dtype ≠ expected, investigate
4. **Red flags:** object type for numeric column, non-null count < rows
5. **Prevention:** Use dtype parameter during loading, not after

**Why This Matters:**
Inspection is not optional. It's professional data science practice. 40 seconds of inspection can save 40 hours of debugging. A numeric column loaded as a string will cause silent data corruption. Only info() catches this immediately. Never skip this step.
