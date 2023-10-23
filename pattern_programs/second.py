def print_pattern6(n):
    for i in range(n):
        for j in range(1, n - i + 1):
            print(j, end="")
        print()


def print_pattern7(n):
    for i in range(n):
        # Space
        for j in range(1, n - i):
            print(" ", end="")

        # Star
        for j in range(1, 2 * i + 2):
            print("*", end="")

        print()


def print_pattern8(n):
    for i in range(n):
        # Space
        for j in range(i):
            print(" ", end="")
        # Star
        for j in range(((2 * n) - (2 * i + 1))):
            print("*", end="")
        print()


def print_pattern9(n):
    for i in range(n):
        # Space
        for j in range(1, n - i):
            print(" ", end="")

        # Star
        for j in range(1, 2 * i + 2):
            print("*", end="")
        print()
    for i in range(n):
        # Space
        for j in range(i):
            print(" ", end="")
        # Star
        for j in range(((2 * n) - (2 * i + 1))):
            print("*", end="")
        print()


def print_pattern10(n):
    for i in range(1, 2 * n):
        if i <= n:
            numStars = i
        else:
            numStars = 2 * n - i
        for j in range(numStars):
            print("*", end="")
        print()


# print_pattern6(5)
# print_pattern7(5)
# print_pattern8(3)
# print_pattern9(5)
print_pattern10(5)
