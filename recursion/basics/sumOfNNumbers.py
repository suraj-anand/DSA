"""Parameterized Recursion"""
# def sum(n, s=0):
#     if n <= 0:
#         print(s)
#         return s
#     sum(n - 1, s=s + n)

"""Functional Recursion"""


def sum(n):
    if n <= 1:
        return 1
    return n + sum(n - 1)


print(sum(5))
