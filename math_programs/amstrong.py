def check_amstrong(number):
    copy = number
    result = 0
    while number > 0:
        lastDigit = number % 10
        result = result + (lastDigit**3)
        number //= 10

    return ((result == copy), copy)


number = int(input("Enter a number: "))
isAmstrong, num = check_amstrong(number)
if isAmstrong:
    print(f"{num} is an amstrong number")
else:
    print(f"{num} is not an amstrong number")
