number = int(input("Enter a number: "))
copy = number
reverse = 0
while number > 0:
    reverse = (reverse * 10) + (number % 10)
    number //= 10

if reverse == copy:
    print(f"{copy} is a palindrome")
else:
    print(f"{copy} is not a palindrome")
