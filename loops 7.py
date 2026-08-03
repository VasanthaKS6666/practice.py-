
secret = 7
guess = None
while guess != secret:
    try:
        guess = int(input("Guess the number (1-10): "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("Correct!")
