# Define the list
items = ["pen", "book", "milk"]

# Print the entire list
print(items)  # ['pen', 'book', 'milk']

# Print the first item
print(items[0])  # pen

# Print the last item
print(items[-1])  # milk

# Print items from index 0 to 2 (exclusive of index 3)
print(items[0:3])  # ['pen', 'book', 'milk']

# Remove the last item
items.pop()  # removes 'milk'

# Remove the first item
items.pop(0)  # removes 'pen'

# Add a new item to the end
items.append("laptop")

# Print the updated list
print(items)  # ['book', 'laptop']
