"""Parameterized Recursion"""
# def factorial(n, fact=1):
#     if n <= 1:
#         print(fact)
#         return
#     factorial(n - 1, fact=fact * n)

"""Functional Recursion"""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
