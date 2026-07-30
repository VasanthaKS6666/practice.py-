time = input("What is the time (HH:MM)? ")

try:
    hour = int(time.split(":")[0])  # Extract hour part
    if hour == 8:
        print("It's breakfast time")
    elif hour == 13:
        print("It's lunch time")
    else:
        print("It's not a meal time")
except ValueError:
    print("Invalid time format. Use HH:MM")
