n = 15
result = [""] * n

for i in range(1, len(result)+1):
    if i % 3 == 0 and i % 5 == 0:
        result[i-1] = "FizzBuzz"
    elif i % 3 == 0:
        result[i-1] = "Fizz"
    elif i % 5 == 0:
        result[i-1] = "Buzz"
    else:
        result[i - 1] = i
print(f"Result: {result}")