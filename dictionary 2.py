# Simple Python dictionary example

# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Bengaluru"
}

# Access a value by key
print("Name:", person["name"])

# Add a new key-value pair
person["profession"] = "Engineer"

# Update an existing value
person["age"] = 26

# Delete a key-value pair safely
person.pop("city", None)  # 'None' avoids error if key doesn't exist

# Loop through dictionary
print("\nDictionary contents:")
for key, value in person.items():
    print(f"{key}: {value}")
