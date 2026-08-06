def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

print("8. Sum of Digits:", sum_of_digits(12345))


