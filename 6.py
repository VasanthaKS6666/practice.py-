
students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}
print("Bob's Marks:", students.get("102", {}).get("marks", "Not Found"))
