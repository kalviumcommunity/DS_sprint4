# MILESTONE 6 SUBMISSION GUIDE
## Passing Data into Functions and Returning Results

---

## Part A: Pull Request Submission

### GitHub PR URL
Once you push your feature branch, create a PR at:
```
https://github.com/kalviumcommunity/DS_sprint4/pull/new/feature/milestone-function-data-flow
```

### PR Description Template
Copy and paste this into your PR description:

```markdown
## Milestone 6: Passing Data into Functions and Returning Results

**Objective:** Demonstrate how to pass data into Python functions via parameters 
and retrieve results using return statements.

### What This PR Demonstrates

This script showcases 9 comprehensive sections:

1. **Basic Function Parameters & Passing Arguments**
   - Simple functions with one parameter
   - Functions with multiple parameters
   - Data flow visualization

2. **Keyword Arguments & Default Parameters**
   - Default parameter values
   - Positional vs keyword arguments
   - Flexibility through defaults

3. **Storing & Reusing Returned Values**
   - Capturing return values in variables
   - Chaining function calls
   - Using returned values in calculations

4. **Multiple Return Values**
   - Returning tuples
   - Returning dictionaries
   - Unpacking multiple return values

5. **Print vs Return: The Critical Problem**
   - Why printing doesn't enable reuse
   - Why returning enables modularity
   - Comparing WRONG vs CORRECT approaches

6. **Data Flow with Parameter Passing**
   - Multi-step function composition
   - Real-world payslip calculation example
   - Clear data flow visualization

7. **Practice Exercises**
   - Temperature converter
   - String processor
   - List analyzer

8. **Common Mistakes & How to Fix Them**
   - Forgetting to return
   - Not using returned values
   - Parameter name confusion

9. **Best Practices for Function Data Flow**
   - Clear parameter names
   - Always return (not print)
   - Consistent parameter types
   - Return early on errors
   - Document parameters & returns

### Key Concepts Demonstrated

- Function parameters (positional, keyword, default)
- Passing arguments correctly
- Return statements and return values
- Storing returned values in variables
- Reusing returned data
- Multiple return values (tuple/dict)
- Data flow from input → function → output
- Why returning enables code reuse

### Code Quality

- All 9 sections produce clear, readable output
- Each section includes explanations and examples
- Demonstrates both correct and incorrect patterns
- Practical, real-world scenarios

### Files Included

- `scripts/function_data_flow_demonstration.py` - Complete demonstration script

---

## Part B: Video Walkthrough (~2 Minutes)

### Video Checklist

Your video should include these sections (in order):

- [ ] **Introduction (~15 seconds)**
  - "This is Milestone 6: Passing Data into Functions and Returning Results"
  - Brief overview of what the script demonstrates

- [ ] **Passing Data into Functions (~30 seconds)**
  - Show function parameter definitions
  - Show how arguments are passed in function calls
  - Run examples with different arguments
  - Explain: "Parameters are variables that receive data when the function is called"

- [ ] **Return Statements (~30 seconds)**
  - Show return statements in function definitions
  - Run example functions and capture output
  - Show storing returned values in variables
  - Explain: "Return gives data back to the program, not just to the console"

- [ ] **Using Returned Data (~30 seconds)**
  - Show using returned value in another statement
  - Demonstrate chaining function calls
  - Show passing returned values to other functions
  - Explain: "Returning values lets us reuse and transform data"

- [ ] **Scenario-Based Reasoning (~15 seconds MANDATORY)**
  - **READ THIS SCENARIO ALOUD:**
  
    > "A function prints its result instead of returning it, making it difficult to 
    > reuse the output elsewhere in the program. Why is this a problem, and how does 
    > returning values fix it?"
  
  - **YOUR ANSWER MUST INCLUDE:**
    - Difference between printing and returning
    - Why printing breaks reusability
    - How returning enables modularity
    - Example of what you CAN'T do with print
    - Example of what you CAN do with return

### Sample Video Script (Use This as Your Template)

---

## VIDEO SCRIPT

**[0:00-0:15] Introduction**

"Hi, I'm demonstrating Milestone 6: Passing Data into Functions and Returning Results. 
This script shows how functions accept input through parameters and give results back 
through return statements. Let me walk you through the key concepts."

**[0:15-0:45] Passing Data into Functions**

"First, let's look at how data flows into functions. Here's a simple function that 
accepts a parameter called `name`. When we call the function with `greet('Alice')`, 
we're passing the string 'Alice' as the argument. This argument becomes the value of 
the `name` parameter inside the function.

Here's a function with multiple parameters: `calculate_total` accepts `price` and `quantity`. 
When we call it with `calculate_total(29.99, 5)`, both values flow into the function. 
Inside the function, we multiply them to get 149.95. But this result hasn't left the 
function yet.

The key point: parameters are placeholders that receive data from outside the function."

**[0:45-1:15] Return Statements**

"Now, how do we get data back out of a function? That's where the `return` statement 
comes in. In this example, the function uses `return` to send the calculated value 
back to the program. 

When we write `result = calculate_total(29.99, 5)`, the returned value gets stored 
in the variable `result`. Now result equals 149.95, and we can do whatever we want 
with it. The crucial difference: if the function only printed the value instead of 
returning it, we wouldn't be able to store it or reuse it.

We can also return multiple values as a tuple or dictionary, giving the caller 
multiple pieces of information at once."

**[1:15-1:45] Using Returned Data**

"Here's where returning values really shines. Once we have a returned value, we can 
use it in all sorts of ways. Look at this example: I'm passing the returned value 
from one function directly to another function as an argument. The result flows:

- Calculate invoice total: returns 80
- That 80 is used to calculate a loyalty bonus: returns 4
- That 4 is subtracted to get the final price: 76

This composition is only possible because we're returning values, not just printing them. 
If the first function printed instead of returning, there would be no way for the 
second function to receive that data.

This is what modularity means: functions that take in data and give out data, which 
other functions can then use."

**[1:45-2:00] Scenario Question & Answer**

"Now, let me answer the scenario question:

**Scenario:** A function prints its result instead of returning it, making it difficult 
to reuse the output elsewhere in the program. Why is this a problem, and how does 
returning values fix it?

**My Answer:**

When a function prints its result, the data only appears on the console—it's not 
available to the rest of the program. The function returns `None`, which means there's 
nothing the program can store or pass along. This breaks code reuse.

[Show the WRONG function - prints only]
Here's the problematic version. It prints the result, but the program gets back None.

[Show the CORRECT function - returns value]
Here's the correct version. It returns the value, and now we can:
1. Store it in a variable
2. Pass it to another function
3. Use it in calculations
4. Include it in conditionals

Returning values enables modularity and composition. Functions become like building 
blocks that fit together. Without returning, functions are isolated—they can only print 
to the console. With returning, functions are reusable components of larger systems.

That's the fundamental difference between printing and returning."

---

## Submission Checklist

- [ ] Python script created: `scripts/function_data_flow_demonstration.py`
- [ ] Script tested and runs without errors
- [ ] Feature branch created: `feature/milestone-function-data-flow`
- [ ] Code committed with conventional commit message
- [ ] Branch pushed to GitHub with upstream tracking
- [ ] Pull Request created using the template above
- [ ] Video recorded (~2 minutes)
- [ ] Video includes all 5 required sections
- [ ] Video includes mandatory scenario answer with references to:
  - [ ] Difference between print and return
  - [ ] Function reusability and modularity
  - [ ] Examples of what you can't do with print
  - [ ] Examples of what you can do with return
- [ ] PR link submitted
- [ ] Video link submitted

---

## Key Learning Outcomes

After completing this milestone, you should understand:

1. **Parameters**: Variables that receive data passed into functions
2. **Arguments**: Actual values passed when calling functions
3. **Return Values**: Data that functions give back to the program
4. **Data Flow**: How information moves into functions and back out
5. **Reusability**: Why returning enables functions to be composed and reused
6. **Modularity**: How small functions with clear inputs/outputs create larger systems
7. **Print vs Return**: Why returning is essential for clean code design

---

## Common Questions

**Q: Can a function print AND return?**
A: Yes! A function can do both. It's fine to print intermediate results for debugging, 
but you should always return the final value if other code needs to use it.

**Q: What if I need to return nothing?**
A: You can just `return` with no value, or return `None` explicitly. The caller will 
get `None`.

**Q: Can I return multiple values?**
A: Yes! Return them as a tuple (like `return total, count`) and unpack them with 
`total, count = my_function()`. Or return a dictionary with named values.

**Q: Why use parameters instead of global variables?**
A: Parameters make functions portable and testable. A function that uses global 
variables is harder to reuse in different contexts and harder to test.

---

**All set! Record your video and submit your PR link and video link.**
