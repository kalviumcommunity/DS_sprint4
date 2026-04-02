"""
Python Collections Data Structures Demonstration

This script demonstrates core understanding of:
- Lists: mutable, ordered collections
- Tuples: immutable, ordered collections
- Dictionaries: mutable, key-value collections
- Indexing and key access patterns
- Modification behavior and immutability
"""


def demonstrate_lists():
    """
    Demonstrate Python lists: mutable, ordered collections of elements.
    """
    print("\n" + "=" * 60)
    print("1. LISTS DEMONSTRATION")
    print("=" * 60)

    # List creation with multiple values
    print("\n--- List Creation & Access ---")
    fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"Original list: {fruit_list}")
    print(f"List type: {type(fruit_list).__name__}")
    print(f"List length: {len(fruit_list)}")

    # Indexed access (0-based)
    print("\n--- Indexed Access ---")
    print(f"First element (index 0): {fruit_list[0]}")
    print(f"Second element (index 1): {fruit_list[1]}")
    print(f"Last element (index -1): {fruit_list[-1]}")
    print(f"Second-to-last (index -2): {fruit_list[-2]}")

    # Slicing
    print("\n--- List Slicing ---")
    print(f"Elements from index 1 to 3: {fruit_list[1:4]}")
    print(f"First three elements: {fruit_list[:3]}")
    print(f"Last three elements: {fruit_list[-3:]}")

    # List modification - adding elements
    print("\n--- Modifying Lists: Adding Elements ---")
    print(f"Before append: {fruit_list}")
    fruit_list.append("fig")
    print(f"After append('fig'): {fruit_list}")

    fruit_list.insert(2, "blueberry")
    print(f"After insert(2, 'blueberry'): {fruit_list}")

    more_fruits = ["grape", "honeydew"]
    fruit_list.extend(more_fruits)
    print(f"After extend(['grape', 'honeydew']): {fruit_list}")

    # List modification - removing elements
    print("\n--- Modifying Lists: Removing Elements ---")
    removed = fruit_list.pop()
    print(f"After pop(): removed '{removed}'")
    print(f"List is now: {fruit_list}")

    fruit_list.remove("blueberry")
    print(f"After remove('blueberry'): {fruit_list}")

    # List modification - changing elements
    print("\n--- Modifying Lists: Changing Elements ---")
    fruit_list[0] = "apricot"
    print(f"After changing index 0 to 'apricot': {fruit_list}")

    fruit_list[2:4] = ["cantaloupe", "dragonfruit"]
    print(f"After changing indices 2-3: {fruit_list}")

    # List operations
    print("\n--- List Operations ---")
    numbers = [5, 2, 8, 1, 9, 3]
    print(f"Original numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")

    numbers_sorted = sorted(numbers)
    print(f"Sorted: {numbers_sorted}")
    print(f"Original (unchanged): {numbers}")

    numbers.sort()
    print(f"After .sort() (in-place): {numbers}")

    print(f"Index of 8: {numbers.index(8)}")
    print(f"Count of 3: {numbers.count(3)}")

    # List iteration
    print("\n--- List Iteration ---")
    print("Iterating over fruit list:")
    for idx, fruit in enumerate(fruit_list):
        print(f"  Index {idx}: {fruit}")


def demonstrate_tuples():
    """
    Demonstrate Python tuples: immutable, ordered collections.
    """
    print("\n" + "=" * 60)
    print("2. TUPLES DEMONSTRATION")
    print("=" * 60)

    # Tuple creation
    print("\n--- Tuple Creation & Access ---")
    coordinates = (40.7128, -74.0060)
    print(f"Tuple: {coordinates}")
    print(f"Tuple type: {type(coordinates).__name__}")

    color_tuple = ("red", "green", "blue")
    print(f"Color tuple: {color_tuple}")

    # Single-element tuple (requires trailing comma)
    single_tuple = ("only_one",)
    print(f"Single-element tuple: {single_tuple}")
    print(f"Without comma: {('not_a_tuple')} is type {type(('not_a_tuple')).__name__}")

    # Indexed access (0-based, same as lists)
    print("\n--- Indexed Access ---")
    print(f"First coordinate: {coordinates[0]}")
    print(f"Second coordinate: {coordinates[1]}")
    print(f"Last element: {coordinates[-1]}")

    city_info = ("New York", 8000000, 302.6)
    print(f"\nCity info tuple: {city_info}")
    print(f"City name: {city_info[0]}")
    print(f"Population: {city_info[1]}")
    print(f"Area (sq miles): {city_info[2]}")

    # Tuple slicing (same as lists)
    print("\n--- Tuple Slicing ---")
    colors = ("red", "green", "blue", "yellow", "orange")
    print(f"All colors: {colors}")
    print(f"First three: {colors[:3]}")
    print(f"Last two: {colors[-2:]}")
    print(f"Colors from index 1 to 3: {colors[1:4]}")

    # Immutability demonstration
    print("\n--- Immutability: Tuples Cannot Be Modified ---")
    numbers_tuple = (10, 20, 30)
    print(f"Original tuple: {numbers_tuple}")

    # Try to modify (will cause error)
    try:
        print("Attempting: numbers_tuple[0] = 100")
        numbers_tuple[0] = 100
    except TypeError as e:
        print(f"❌ Error: {e}")
        print("   Tuples are immutable—cannot change elements!")

    # Try to append
    try:
        print("\nAttempting: numbers_tuple.append(40)")
        numbers_tuple.append(40)
    except AttributeError as e:
        print(f"❌ Error: Tuples have no append method")
        print("   Tuples don't have modification methods!")

    # But you can create a new tuple
    print("\n✓ Creating new tuple from existing tuple:")
    new_numbers = numbers_tuple + (40,)
    print(f"Original: {numbers_tuple}")
    print(f"Original (unchanged): {numbers_tuple}")
    print(f"New tuple: {new_numbers}")

    # Tuple unpacking
    print("\n--- Tuple Unpacking ---")
    point = (5, 10)
    x, y = point
    print(f"Tuple: {point}")
    print(f"Unpacked: x={x}, y={y}")

    person = ("Alice", 28, "Engineer")
    name, age, job = person
    print(f"\nTuple: {person}")
    print(f"Unpacked: name='{name}', age={age}, job='{job}'")

    # Tuple operations
    print("\n--- Tuple Operations ---")
    mixed_tuple = (1, 2, 2, 3, 2, 4)
    print(f"Tuple: {mixed_tuple}")
    print(f"Count of 2: {mixed_tuple.count(2)}")
    print(f"Index of 3: {mixed_tuple.index(3)}")
    print(f"Length: {len(mixed_tuple)}")
    print(f"Sum: {sum(mixed_tuple)}")
    print(f"Max: {max(mixed_tuple)}")
    print(f"Min: {min(mixed_tuple)}")


def demonstrate_dictionaries():
    """
    Demonstrate Python dictionaries: mutable key-value collections.
    """
    print("\n" + "=" * 60)
    print("3. DICTIONARIES DEMONSTRATION")
    print("=" * 60)

    # Dictionary creation with meaningful key-value pairs
    print("\n--- Dictionary Creation & Access ---")
    student = {
        "name": "Bob",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "enrolled": True
    }
    print(f"Student dictionary: {student}")
    print(f"Dictionary type: {type(student).__name__}")

    # Accessing values by key
    print("\n--- Accessing Values by Key ---")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}")
    print(f"GPA: {student['gpa']}")

    # Safe access with .get()
    print("\n--- Safe Access with .get() ---")
    print(f"Using .get('name'): {student.get('name')}")
    print(f"Using .get('city'): {student.get('city')}")  # Returns None if key doesn't exist
    print(f"Using .get('city', 'Unknown'): {student.get('city', 'Unknown')}")

    # Modifying dictionary values
    print("\n--- Modifying Dictionary Values ---")
    print(f"Before: age = {student['age']}")
    student['age'] = 21
    print(f"After: age = {student['age']}")

    student['gpa'] = 3.9
    print(f"Updated GPA: {student['gpa']}")

    # Adding new key-value pairs
    print("\n--- Adding New Key-Value Pairs ---")
    print(f"Before adding 'city': {student}")
    student['city'] = "Boston"
    print(f"After adding 'city': {student}")

    student['phone'] = "555-1234"
    print(f"After adding 'phone': {student}")

    # Dictionary with various data types
    print("\n--- Dictionary with Mixed Data Types ---")
    product = {
        "id": 101,
        "name": "Wireless Mouse",
        "price": 29.99,
        "in_stock": True,
        "colors": ["black", "white", "silver"],
        "specs": {
            "battery": "2 AA",
            "range": "30 feet",
            "dpi": 1600
        }
    }
    print(f"Product: {product}")
    print(f"\nAccessing nested values:")
    print(f"Product name: {product['name']}")
    print(f"Price: ${product['price']}")
    print(f"Available colors: {product['colors']}")
    print(f"First color: {product['colors'][0]}")
    print(f"Battery type: {product['specs']['battery']}")
    print(f"DPI: {product['specs']['dpi']}")

    # Dictionary methods
    print("\n--- Dictionary Methods ---")
    inventory = {"apples": 50, "bananas": 30, "oranges": 45}
    print(f"Inventory: {inventory}")

    print(f"\nKeys: {list(inventory.keys())}")
    print(f"Values: {list(inventory.values())}")
    print(f"Items: {list(inventory.items())}")

    # Removing items
    print("\n--- Removing Items ---")
    print(f"Before: {inventory}")
    removed_value = inventory.pop("oranges")
    print(f"After pop('oranges'): {inventory}")
    print(f"Removed value: {removed_value}")

    inventory.pop("bananas", None)
    print(f"After pop('bananas', None): {inventory}")

    # Checking key existence
    print("\n--- Checking Key Existence ---")
    print(f"'apples' in inventory: {'apples' in inventory}")
    print(f"'oranges' in inventory: {'oranges' in inventory}")
    print(f"'grapes' in inventory: {'grapes' in inventory}")

    # Dictionary iteration
    print("\n--- Iterating Over Dictionary ---")
    grades = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 88}
    print(f"Grades: {grades}\n")

    print("Iterating over keys:")
    for student_name in grades:
        print(f"  {student_name}")

    print("\nIterating over items (key-value pairs):")
    for name, grade in grades.items():
        print(f"  {name}: {grade}")

    print("\nIterating with status:")
    for name, grade in grades.items():
        status = "Excellent" if grade >= 90 else "Good" if grade >= 85 else "Needs Improvement"
        print(f"  {name}: {grade} ({status})")

    # Dictionary update and clear
    print("\n--- Updating Dictionary ---")
    settings = {"theme": "dark", "language": "en"}
    print(f"Original settings: {settings}")

    new_settings = {"theme": "light", "font_size": 14}
    settings.update(new_settings)
    print(f"After update: {settings}")

    # Creating dictionary from lists
    print("\n--- Creating Dictionary from Lists ---")
    keys = ["x", "y", "z"]
    values = [10, 20, 30]
    coord_dict = dict(zip(keys, values))
    print(f"Keys: {keys}")
    print(f"Values: {values}")
    print(f"Dictionary: {coord_dict}")


def demonstrate_collection_comparison():
    """
    Compare and contrast lists, tuples, and dictionaries.
    """
    print("\n" + "=" * 60)
    print("4. COLLECTION COMPARISON")
    print("=" * 60)

    print("\n--- Data Type Characteristics ---")
    comparison_table = """
    ┌───────────────┬──────────────┬──────────────┬──────────────┐
    │ Characteristic│     List     │     Tuple    │  Dictionary  │
    ├───────────────┼──────────────┼──────────────┼──────────────┤
    │ Mutable       │      ✓       │      ✗       │      ✓       │
    │ Ordered       │      ✓       │      ✓       │      ✓*      │
    │ Indexed       │      ✓       │      ✓       │    By Key    │
    │ Duplicates    │      ✓       │      ✓       │   Keys Only  │
    │ Performance   │    Medium    │     Fast     │     Fast     │
    └───────────────┴──────────────┴──────────────┴──────────────┘
    * In Python 3.7+, dictionaries maintain insertion order
    """
    print(comparison_table)

    # When to use what
    print("\n--- When to Use Each Collection ---")
    print("\nLISTS are best for:")
    print("  • Ordered collections that need modification")
    print("  • When you'll add, remove, or change items frequently")
    print("  • Example: shopping list, todo items, processing pipeline")

    print("\nTUPLES are best for:")
    print("  • Fixed, immutable collections")
    print("  • Using as dictionary keys (lists can't be keys)")
    print("  • Function return values with multiple values")
    print("  • Example: coordinates, RGB colors, readonly data")

    print("\nDICTIONARIES are best for:")
    print("  • Key-value associations")
    print("  • Looking up values by meaningful names")
    print("  • Structured data records")
    print("  • Example: student records, product info, settings")


def demonstrate_practical_example():
    """
    Practical example combining all collection types.
    """
    print("\n" + "=" * 60)
    print("5. PRACTICAL EXAMPLE: STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)

    # Using all collection types together
    students_data = {
        "S001": {
            "name": "Alice Johnson",
            "grades": [95, 87, 92, 88],
            "courses": ("Math", "Physics", "Chemistry"),
            "contact": ("alice@school.edu", "555-0101")
        },
        "S002": {
            "name": "Bob Smith",
            "grades": [85, 88, 90, 86],
            "courses": ("Math", "Biology", "Chemistry"),
            "contact": ("bob@school.edu", "555-0102")
        },
        "S003": {
            "name": "Charlie Brown",
            "grades": [92, 95, 94, 96],
            "courses": ("Math", "Physics", "English"),
            "contact": ("charlie@school.edu", "555-0103")
        }
    }

    print("\n--- Student Records Structure ---")
    print("Dictionary (students) → Dictionary (student info) → Lists & Tuples")
    print()

    for student_id, info in students_data.items():
        print(f"\n{student_id}: {info['name']}")
        print(f"  Email: {info['contact'][0]}")
        print(f"  Phone: {info['contact'][1]}")
        print(f"  Courses: {', '.join(info['courses'])}")
        print(f"  Grades: {info['grades']}")
        avg_grade = sum(info['grades']) / len(info['grades'])
        print(f"  Average: {avg_grade:.2f}")

    # Analyzing data with collections
    print("\n--- Analysis Using Collections ---")
    all_grades = []
    for student_id, info in students_data.items():
        all_grades.extend(info['grades'])

    print(f"Total grades recorded: {len(all_grades)}")
    print(f"Average grade across all students: {sum(all_grades) / len(all_grades):.2f}")
    print(f"Highest grade: {max(all_grades)}")
    print(f"Lowest grade: {min(all_grades)}")

    # Modifying the data
    print("\n--- Modifying Student Records ---")
    print("Adding new grade for Alice...")
    students_data["S001"]["grades"].append(91)
    print(f"Alice's updated grades: {students_data['S001']['grades']}")

    print("\nAdding new student...")
    students_data["S004"] = {
        "name": "Diana Prince",
        "grades": [88, 93, 89, 91],
        "courses": ("Math", "English", "History"),
        "contact": ("diana@school.edu", "555-0104")
    }
    print(f"Total students: {len(students_data)}")


if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("PYTHON COLLECTIONS DEMONSTRATION")
    print("█" * 60)

    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_collection_comparison()
    demonstrate_practical_example()

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("✓ Lists are mutable ordered collections with indexed access")
    print("✓ Tuples are immutable ordered collections (safer, faster)")
    print("✓ Dictionaries are mutable key-value collections")
    print("✓ All three support iteration but with different patterns")
    print("✓ Tuples can be used as dictionary keys—lists cannot")
    print("✓ Choose the right collection type for your use case")
    print("\n")
