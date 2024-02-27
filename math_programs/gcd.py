def GCD(a, b):
    if  b % a == 0:
        return a
    else:
        return GCD(b%a, a)

if __name__ == "__main__":
    
    a = 1
    b = 3
    print(f"Gcd of {a} and {b} is {GCD(a, b)}")