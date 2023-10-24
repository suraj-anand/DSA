def isPrime(number):
    count = 0

    # O (n)
    # for i in range(2, number):
    #     if number % i == 0:
    #         count += 1

    # # O ( sqrt(n) )
    i = 2
    while i * i <= number:
        if number % i == 0:
            count += 1
            if number // i != i:
                count += 1
        i += 1
    return count == 0


number = int(input("Enter a number: "))
if isPrime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
