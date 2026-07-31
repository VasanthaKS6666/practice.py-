# 1. Create a dictionary
person = {"name": "Alice", "age": 25, "city": "Bengaluru"}
print("Dictionary:", person)

# 2. Access a value by key
print("Name:", person["name"])

# 3. Use get() to avoid KeyError
print("Country:", person.get("country", "Not specified"))

# 4. Add a new key-value pair
person["country"] = "India"
print("After adding country:", person)

# 5. Update an existing value
person["age"] = 26
print("After updating age:", person)

# 6. Delete a key-value pair
removed_value = person.pop("city", None)
print("Removed city:", removed_value)
print("After deletion:", person)

# 7. Loop through keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# 8. Dictionary comprehension (square of numbers)
squares = {x: x**2 for x in range(1, 6)}
print("Squares dict:", squares)

# 9. Merge two dictionaries (Python 3.9+)
extra_info = {"hobby": "Reading", "language": "Python"}
merged = person | extra_info
print("Merged dictionary:", merged)

# 10. Count frequency of characters in a string
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("Character frequency:", freq)
