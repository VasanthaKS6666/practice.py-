# Example 1: Positive, Negative, or Zero
try:
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
