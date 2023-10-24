number = int(input("Enter a number: "))

# using log10
import math

print(f"Count of digits -> {int(math.log10(number)) + 1}")

# iterative approach
count = 0
while number != 0:
    count += 1
    number //= 10

print(f"Count of digits -> {count}")
