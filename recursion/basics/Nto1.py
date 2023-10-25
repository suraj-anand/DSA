# def func(n):
#     if n <= 0:
#         return
#     print(n)
#     func(n - 1)


def func(n, i=1):
    if i > n:
        return
    func(n, i + 1)
    print(i)


func(10)
