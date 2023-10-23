def print_pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


def print_pattern2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()


def print_pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


def print_pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()


def print_pattern5(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


# print_pattern1(5)
# print_pattern2(5)
# print_pattern3(5)
# print_pattern4(5)
print_pattern5(5)
