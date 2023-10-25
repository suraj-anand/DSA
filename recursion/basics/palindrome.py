def check_palindrome(string, i):
    if i >= n // 2:
        return True

    if string[i] != string[n - i - 1]:
        return False

    return check_palindrome(string, i=i + 1)


string = "racecar"
# string = "racecar"
n = len(string)
if check_palindrome(string=string, i=0):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
