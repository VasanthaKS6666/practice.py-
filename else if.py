# Simple if-else example: Check if a number is positive or negative

# Get user input
try:
    num = float(input("Enter a number: "))

    if num >= 0:
        print("The number is positive or zero.")
    else:
        print("The number is negative.")

except ValueError:
    print("Invalid input! Please enter a numeric value.")
