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


def print_pattern19(n):
    # First Half
    for i in range(n):
        # Star - 1
        for j in range(n - i):
            print("*", end="")
        
        # Space
        for j in range(2*i):
            print(" ", end="")

        # Star - 2
        for j in range(n - i):
            print("*", end="")
        print("")
    
    # Second half
    for i in range(n):
        # star - 1
        for j in range(i+1):
            print("*", end="")
        
        # Space
        for j in range((2*n) - (2*(i+1))):
            print(" ", end="")
        
        # star - 2
        for j in range(i+1):
            print("*", end="")
        
        print("")

# print_pattern16(5)
# print_pattern17(4)
# print_pattern18(5)
print_pattern19(5)