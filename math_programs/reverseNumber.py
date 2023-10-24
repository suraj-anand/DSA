number = int(input("Enter a number: "))

reverse = 0
while number > 0:
    reverse = (reverse * 10) + (number % 10)
    number //= 10

print(f"Reversed number: {reverse}")
