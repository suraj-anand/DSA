# A.K.A G.C.D

n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))

hcf = 1
for i in range(1, min(n1, n2)):
    if n1 % i == 0:
        hcf = i

print(f"HCF of {n1} and {n2} is {hcf}")
