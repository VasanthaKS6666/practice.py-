# Example 4: Temperature category
try:
    temp = float(input("Enter temperature in °C: "))
    if temp < 0:
        print("Freezing cold")
    elif temp < 20:
        print("Cool")
    elif temp < 35:
        print("Warm")
    else:
        print("Hot")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
