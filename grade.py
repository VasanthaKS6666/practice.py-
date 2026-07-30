# Example 2: Grade classification
try:
    marks = float(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: F")
except ValueError:
    print("Invalid input. Please enter a number.")
