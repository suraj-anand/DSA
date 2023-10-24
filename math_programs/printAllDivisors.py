number = int(input("Enter a number: "))

print(f"Divisors of {number}")

# O(n)
for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# O(sqrt(n))
i = 1
while i * i <= number:
    if number % i == 0:
        print(i)
        if number // i != i:
            print(number // i)
    i += 1
