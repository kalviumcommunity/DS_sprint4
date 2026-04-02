"""
Python Loops for Iterative Data Processing Demonstration

This script demonstrates core understanding of:
- for loops: iterating over sequences and ranges
- while loops: condition-based iteration
- Loop variable updates and control flow
- break and continue statements
- Common pitfalls and debugging techniques
"""


def demonstrate_for_loops_range():
    """
    Demonstrate for loops iterating over ranges.
    """
    print("\n" + "=" * 60)
    print("1. FOR LOOPS: ITERATING OVER RANGES")
    print("=" * 60)

    # Basic for loop with range
    print("\n--- Basic For Loop: range(5) ---")
    print("Code: for i in range(5):")
    print("      print(i)")
    print("\nOutput:")
    for i in range(5):
        print(f"  i = {i}")

    # For loop with start and stop
    print("\n--- For Loop: range(2, 6) ---")
    print("Code: for i in range(2, 6):")
    print("      print(i)")
    print("\nOutput:")
    for i in range(2, 6):
        print(f"  i = {i}")

    # For loop with step
    print("\n--- For Loop: range(0, 10, 2) ---")
    print("Code: for i in range(0, 10, 2):  # step=2")
    print("      print(i)")
    print("\nOutput:")
    for i in range(0, 10, 2):
        print(f"  i = {i}")

    # Reverse iteration with negative step
    print("\n--- For Loop: range(5, 0, -1) ---")
    print("Code: for i in range(5, 0, -1):  # count down")
    print("      print(i)")
    print("\nOutput:")
    for i in range(5, 0, -1):
        print(f"  i = {i}")

    # Accumulation with for loop
    print("\n--- Accumulation: Sum Numbers 1 to 5 ---")
    print("Code:")
    print("  total = 0")
    print("  for i in range(1, 6):")
    print("      total += i")
    print("      print(f'i={i}, total={total}')")
    print("\nOutput:")
    total = 0
    for i in range(1, 6):
        total += i
        print(f"  i={i}, total={total}")
    print(f"Final total: {total}")


def demonstrate_for_loops_sequences():
    """
    Demonstrate for loops iterating over sequences.
    """
    print("\n" + "=" * 60)
    print("2. FOR LOOPS: ITERATING OVER SEQUENCES")
    print("=" * 60)

    # For loop over list
    print("\n--- For Loop Over List ---")
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"fruits = {fruits}")
    print("Code: for fruit in fruits:")
    print("      print(fruit)")
    print("\nOutput:")
    for fruit in fruits:
        print(f"  {fruit}")

    # For loop with index using enumerate
    print("\n--- For Loop With Index: enumerate() ---")
    print(f"fruits = {fruits}")
    print("Code: for index, fruit in enumerate(fruits):")
    print("      print(f'Index {index}: {fruit}')")
    print("\nOutput:")
    for index, fruit in enumerate(fruits):
        print(f"  Index {index}: {fruit}")

    # For loop over string (strings are sequences)
    print("\n--- For Loop Over String ---")
    word = "LOOP"
    print(f'word = "{word}"')
    print("Code: for letter in word:")
    print("      print(letter)")
    print("\nOutput:")
    for letter in word:
        print(f"  {letter}")

    # For loop over tuple
    print("\n--- For Loop Over Tuple ---")
    dimensions = (10, 20, 30)
    print(f"dimensions = {dimensions}")
    print("Code: for dim in dimensions:")
    print("      print(dim)")
    print("\nOutput:")
    for dim in dimensions:
        print(f"  {dim}")

    # For loop over dictionary
    print("\n--- For Loop Over Dictionary ---")
    person = {"name": "Alice", "age": 25, "city": "Boston"}
    print(f"person = {person}")
    print("Code: for key, value in person.items():")
    print("      print(f'{key}: {value}')")
    print("\nOutput:")
    for key, value in person.items():
        print(f"  {key}: {value}")


def demonstrate_while_loops():
    """
    Demonstrate while loops with conditions.
    """
    print("\n" + "=" * 60)
    print("3. WHILE LOOPS: CONDITION-BASED ITERATION")
    print("=" * 60)

    # Basic while loop
    print("\n--- Basic While Loop ---")
    print("Code:")
    print("  count = 0")
    print("  while count < 3:")
    print("      print(f'count = {count}')")
    print("      count += 1")
    print("\nOutput:")
    count = 0
    while count < 3:
        print(f"  count = {count}")
        count += 1

    # While loop with user-like input simulation
    print("\n--- While Loop: Countdown ---")
    print("Code:")
    print("  countdown = 5")
    print("  while countdown > 0:")
    print("      print(f'Launching in {countdown}...')")
    print("      countdown -= 1")
    print("  print('Blastoff!')")
    print("\nOutput:")
    countdown = 5
    while countdown > 0:
        print(f"  Launching in {countdown}...")
        countdown -= 1
    print("  Blastoff!")

    # While loop accumulating values
    print("\n--- While Loop: Accumulate Until Threshold ---")
    print("Code:")
    print("  total = 0")
    print("  value = 10")
    print("  while total < 50:")
    print("      total += value")
    print("      print(f'total = {total}')")
    print("\nOutput:")
    total = 0
    value = 10
    iteration = 0
    while total < 50:
        total += value
        print(f"  total = {total}")
        iteration += 1

    # While loop with multiple conditions
    print("\n--- While Loop: Multiple Conditions ---")
    print("Code:")
    print("  balance = 100")
    print("  withdrawal = 20")
    print("  withdrawals = 0")
    print("  while balance >= withdrawal and withdrawals < 3:")
    print("      balance -= withdrawal")
    print("      withdrawals += 1")
    print("      print(f'After withdrawal {withdrawals}: ${balance}')")
    print("\nOutput:")
    balance = 100
    withdrawal = 20
    withdrawals = 0
    while balance >= withdrawal and withdrawals < 3:
        balance -= withdrawal
        withdrawals += 1
        print(f"  After withdrawal {withdrawals}: ${balance}")


def demonstrate_break_continue():
    """
    Demonstrate break and continue statements.
    """
    print("\n" + "=" * 60)
    print("4. LOOP CONTROL: BREAK AND CONTINUE")
    print("=" * 60)

    # Break statement
    print("\n--- Break: Exit Loop Early ---")
    print("Code: for i in range(10):")
    print("      if i == 3:")
    print("          print(f'Found {i}! Breaking...')")
    print("          break")
    print("      print(i)")
    print("\nOutput:")
    for i in range(10):
        if i == 3:
            print(f"  Found {i}! Breaking...")
            break
        print(f"  {i}")
    print("(Loop ended early)")

    # Break in while loop
    print("\n--- Break in While: Search Example ---")
    print("Code:")
    print("  numbers = [2, 4, 6, 8, 10, 3, 12]")
    print("  search_value = 3")
    print("  found = False")
    print("  i = 0")
    print("  while i < len(numbers):")
    print("      if numbers[i] == search_value:")
    print("          print(f'Found {search_value} at index {i}')")
    print("          found = True")
    print("          break")
    print("      i += 1")
    print("\nOutput:")
    numbers = [2, 4, 6, 8, 10, 3, 12]
    search_value = 3
    found = False
    i = 0
    while i < len(numbers):
        if numbers[i] == search_value:
            print(f"  Found {search_value} at index {i}")
            found = True
            break
        i += 1

    # Continue statement
    print("\n--- Continue: Skip to Next Iteration ---")
    print("Code: for i in range(6):")
    print("      if i == 2 or i == 4:")
    print("          print(f'Skipping {i}')")
    print("          continue")
    print("      print(f'Processing {i}')")
    print("\nOutput:")
    for i in range(6):
        if i == 2 or i == 4:
            print(f"  Skipping {i}")
            continue
        print(f"  Processing {i}")

    # Continue in while loop
    print("\n--- Continue: Skip Even Numbers ---")
    print("Code:")
    print("  count = 0")
    print("  while count < 6:")
    print("      if count % 2 == 0:")
    print("          print(f'{count} is even, skipping')")
    print("          count += 1")
    print("          continue")
    print("      print(f'{count} is odd')")
    print("      count += 1")
    print("\nOutput:")
    count = 0
    while count < 6:
        if count % 2 == 0:
            print(f"  {count} is even, skipping")
            count += 1
            continue
        print(f"  {count} is odd")
        count += 1


def demonstrate_loop_variable_updates():
    """
    Demonstrate proper loop variable updates.
    """
    print("\n" + "=" * 60)
    print("5. LOOP VARIABLE UPDATES")
    print("=" * 60)

    # Important: Understanding when variables update
    print("\n--- Variable Update: Accumulation ---")
    print("Code: result = 0")
    print("      for i in range(1, 4):")
    print("          result += i * 10")
    print("          print(f'i={i}, result={result}')")
    print("\nOutput:")
    result = 0
    for i in range(1, 4):
        result += i * 10
        print(f"  i={i}, result={result}")

    # Multiple variable updates
    print("\n--- Multiple Variable Updates ---")
    print("Code:")
    print("  for i in range(1, 4):")
    print("      doubled = i * 2")
    print("      squared = i ** 2")
    print("      print(f'i={i}, doubled={doubled}, squared={squared}')")
    print("\nOutput:")
    for i in range(1, 4):
        doubled = i * 2
        squared = i ** 2
        print(f"  i={i}, doubled={doubled}, squared={squared}")

    # Variables outside loop accessible after
    print("\n--- Variables Persist After Loop ---")
    print("Code:")
    print("  for i in range(3):")
    print("      value = i * 100")
    print("  print(f'Loop ended. Last value: {value}, Last i: {i}')")
    print("\nOutput:")
    for i in range(3):
        value = i * 100
    print(f"  Loop ended. Last value: {value}, Last i: {i}")


def demonstrate_practical_loops():
    """
    Demonstrate practical loop scenarios.
    """
    print("\n" + "=" * 60)
    print("6. PRACTICAL LOOP SCENARIOS")
    print("=" * 60)

    # Data processing: summing values
    print("\n--- Scenario 1: Sum and Average ---")
    print("Goal: Calculate sum and average of grades")
    print("Code:")
    print("  grades = [85, 92, 78, 95, 88]")
    print("  total = 0")
    print("  for grade in grades:")
    print("      total += grade")
    print("  average = total / len(grades)")
    print("\nOutput:")
    grades = [85, 92, 78, 95, 88]
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print(f"  Grades: {grades}")
    print(f"  Total: {total}")
    print(f"  Average: {average:.2f}")

    # Data processing: filtering with continue
    print("\n--- Scenario 2: Process Only Valid Data (continue) ---")
    print("Goal: Process positive numbers only")
    print("Code:")
    print("  numbers = [5, -2, 8, -1, 3, -7, 6]")
    print("  for num in numbers:")
    print("      if num < 0:")
    print("          continue")
    print("      print(f'Processing: {num}')")
    print("\nOutput:")
    numbers = [5, -2, 8, -1, 3, -7, 6]
    for num in numbers:
        if num < 0:
            continue
        print(f"  Processing: {num}")

    # Data processing: early termination with break
    print("\n--- Scenario 3: Stop Processing (break) ---")
    print("Goal: Process until we find a specific value")
    print("Code:")
    print("  items = ['apple', 'banana', 'cherry', 'date', 'fig']")
    print("  for item in items:")
    print("      if item == 'cherry':")
    print("          print(f'Found target: {item}')")
    print("          break")
    print("      print(f'Checking: {item}')")
    print("\nOutput:")
    items = ['apple', 'banana', 'cherry', 'date', 'fig']
    for item in items:
        if item == 'cherry':
            print(f"  Found target: {item}")
            break
        print(f"  Checking: {item}")

    # Nested loops
    print("\n--- Scenario 4: Nested Loops (Multiplication Table) ---")
    print("Goal: Print a small multiplication table")
    print("Code:")
    print("  for i in range(1, 4):")
    print("      for j in range(1, 4):")
    print("          print(f'{i}x{j}={i*j}', end='  ')")
    print("      print()  # new line")
    print("\nOutput:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"  {i}x{j}={i*j}", end="  ")
        print()

    # While loop for user-like input
    print("\n--- Scenario 5: While Loop: Repeat Until Valid ---")
    print("Goal: Keep repeating until condition met")
    print("Code:")
    print("  attempts = 0")
    print("  max_attempts = 3")
    print("  while attempts < max_attempts:")
    print("      attempts += 1")
    print("      print(f'Attempt {attempts}')")
    print("  print('Process complete')")
    print("\nOutput:")
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        attempts += 1
        print(f"  Attempt {attempts}")
    print("  Process complete")


def demonstrate_infinite_loop_mistakes():
    """
    Demonstrate common infinite loop mistakes and how to debug them.
    """
    print("\n" + "=" * 60)
    print("7. DEBUGGING: INFINITE LOOPS")
    print("=" * 60)

    print("\n--- Common Mistake 1: Forgetting to Update Loop Variable ---")
    print("[ERROR] Code:")
    print("  count = 0")
    print("  while count < 3:")
    print("      print(count)  # count never changes!")
    print("      # Missing: count += 1")
    print("\n[PROBLEM] This creates an infinite loop!")
    print("[FIX] Add: count += 1")

    print("\n--- Common Mistake 2: Wrong Loop Condition ---")
    print("[ERROR] Code:")
    print("  count = 5")
    print("  while count > 0:")
    print("      print(count)")
    print("      count += 1  # Incrementing instead of decrementing!")
    print("\n[PROBLEM] count keeps getting larger, never becomes <= 0")
    print("[FIX] Change to: count -= 1")

    print("\n--- Common Mistake 3: Never-False Condition ---")
    print("[ERROR] Code:")
    print("  while True:")
    print("      x = 5")
    print("      if x == 6:")
    print("          break")
    print("\n[PROBLEM] x is always 5, never becomes 6")
    print("[FIX] Ensure break condition can actually be reached")

    print("\n--- Safe While Loop Pattern ---")
    print("[SAFE] Template:")
    print("  counter = 0")
    print("  max_iterations = 100  # Safety limit")
    print("  while counter < max_iterations:")
    print("      # Do something")
    print("      counter += 1  # Always update!")
    print("      if some_condition:")
    print("          break")

    print("\n--- Debugging Technique: Add Print Statements ---")
    print("[SAFE] Code with debugging:")
    print("  count = 0")
    print("  max_count = 3")
    print("  while count < max_count:")
    print("      print(f'[DEBUG] count={count}, max_count={max_count}')")
    print("      count += 1")
    print("  print('Loop completed')")
    print("\nOutput with debug info:")
    count = 0
    max_count = 3
    while count < max_count:
        print(f"  [DEBUG] count={count}, max_count={max_count}")
        count += 1
    print("  Loop completed")


def demonstrate_loop_best_practices():
    """
    Demonstrate best practices for loops.
    """
    print("\n" + "=" * 60)
    print("8. LOOP BEST PRACTICES")
    print("=" * 60)

    print("\n--- Best Practice 1: Use for with range() for Simple Counting ---")
    print("[GOOD] for i in range(5):")
    print("           process(i)")
    print("\n[NOT AS GOOD] count = 0")
    print("             while count < 5:")
    print("                 process(count)")
    print("                 count += 1")
    print("(for loops are cleaner for simple counting)")

    print("\n--- Best Practice 2: Use for to Iterate Over Collections ---")
    print("[GOOD] for item in items:")
    print("           print(item)")
    print("\n[NOT AS GOOD] i = 0")
    print("             while i < len(items):")
    print("                 print(items[i])")
    print("                 i += 1")
    print("(Direct iteration is cleaner)")

    print("\n--- Best Practice 3: Use while for Complex Conditions ---")
    print("[GOOD] while balance > 0 and not quit:")
    print("           # complex logic")
    print("\n[OK BUT LESS CLEAR] for _ in range(1000):")
    print("                       if not (balance > 0 and not quit):")
    print("                           break")
    print("(while is clearer for complex conditions)")

    print("\n--- Best Practice 4: Avoid Magic Numbers ---")
    print("[GOOD] max_attempts = 5")
    print("       for attempt in range(max_attempts):")
    print("           try_something()")
    print("\n[NOT GOOD] for attempt in range(5):  # What does 5 mean?")
    print("               try_something()")

    print("\n--- Best Practice 5: Use Meaningful Loop Variables ---")
    print("[GOOD] for student in students:")
    print("           print(student.name)")
    print("\n[NOT AS CLEAR] for s in students:")
    print("                   print(s.name)")
    print("(Clear names make code readable)")


if __name__ == "__main__":
    print("\n" + "*" * 60)
    print("PYTHON LOOPS FOR ITERATIVE DATA PROCESSING")
    print("*" * 60)

    demonstrate_for_loops_range()
    demonstrate_for_loops_sequences()
    demonstrate_while_loops()
    demonstrate_break_continue()
    demonstrate_loop_variable_updates()
    demonstrate_practical_loops()
    demonstrate_infinite_loop_mistakes()
    demonstrate_loop_best_practices()

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("[OK] for loops: Use for known number of iterations")
    print("[OK] for loop: Clean way to iterate over sequences")
    print("[OK] while loops: Use for complex conditions")
    print("[OK] while loops: Always update loop variables!")
    print("[OK] break: Exit loop immediately")
    print("[OK] continue: Skip to next iteration")
    print("[OK] Infinite loops happen when condition never becomes false")
    print("[OK] Debug loops with print() statements")
    print("[OK] Safe while loops have update logic AND clear exit conditions")
    print("\n")
