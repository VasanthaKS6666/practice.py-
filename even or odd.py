# Example 3: Even, Odd, or Zero
try:
    num = int(input("Enter an integer: "))
    if num == 0:
        print("Zero")
    elif num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except ValueError:
    print("Invalid input. Please enter an integer.")
