def print_pattern16(n):
    for i in range(n):
        initialCharASCII = ord("A")
        for j in range(i + 1):
            print(chr(initialCharASCII), end=" ")
        initialCharASCII += 1
        print()


def print_pattern17(n):
    for i in range(1, n + 1):
        # Spaces
        for j in range(n - i):
            print(" ", end="")

        # set 1
        initialCharASCII = ord("A")
        for j in range(i):
            print(chr(initialCharASCII), end="")
            initialCharASCII += 1

        # set 2
        initialCharASCII -= 1
        for j in range(i - 1):
            initialCharASCII -= 1
            print(chr(initialCharASCII), end="")

        print()


def print_pattern18(n):
    for i in range(1, n + 1):
        initialCharASCII = 65 + (n - i)
        for j in range(i):
            print(chr(initialCharASCII), end="")
            initialCharASCII += 1

        print()


# print_pattern16(5)
# print_pattern17(4)
print_pattern18(5)
