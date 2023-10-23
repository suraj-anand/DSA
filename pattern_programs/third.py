def print_pattern11(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            start = 0
        else:
            start = 1

        for j in range(i):
            print(start, end=" ")
            if start == 0:
                start += 1
            else:
                start -= 1
        print()


def print_pattern12(n):
    for i in range(1, n + 1):
        # num1
        for j in range(1, i + 1):
            print(j, end="")

        # spaces
        spaces = (n * 2) - 2 * i
        for j in range(spaces):
            print(" ", end="")

        # num2
        for j in range(i, 0, -1):
            print(j, end="")

        print()


def print_pattern13(n):
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()


def print_pattern14(n):
    for i in range(n):
        initialCharASCII = ord("A")
        for j in range(i + 1):
            print(chr(initialCharASCII), end=" ")
            initialCharASCII += 1
        print()


def print_pattern15(n):
    for i in range(n):
        initialCharASCII = ord("A")
        for j in range(n - i, 0, -1):
            print(chr(initialCharASCII), end=" ")
            initialCharASCII += 1
        print()


# print_pattern11(5)
# print_pattern12(5)
# print_pattern13(5)
# print_pattern14(5)
print_pattern15(5)
