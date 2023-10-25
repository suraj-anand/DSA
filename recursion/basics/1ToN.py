def func(n, i=1):
    if n <= 0:
        return
    print(i)
    func(n - 1, i + 1)


# Backtracks
def func(n):
    if n <= 0:
        return
    func(n - 1)
    print(n)


func(10)
