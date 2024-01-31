def isOdd(n):
    return n % 2 != 0


def largestOddNumber(num : str):
    i = len(num) - 1
    while i >= 0:
        n = int(num[i])
        if isOdd(n):
            return num[0:i+1]
        i -= 1
    return ""


if __name__ == "__main__":
    num = "2720502"
    result = largestOddNumber(num)
    print(f"result => {result}")