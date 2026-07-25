# Example: Modifying elements in a Python list

# Initial list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Modify a single element by index
numbers[1] = 25  # Change 20 to 25

# Modify multiple elements using slicing
numbers[2:4] = [35, 45]  # Change 30, 40 to 35, 45

# Append a new element
numbers.append(60)

# Remove an element
if 10 in numbers:
    numbers.remove(10)

print("Modified list:", numbers)
