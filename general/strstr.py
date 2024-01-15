def strstr(s: str, x: str):
    n, m = len(s), len(x)
    i, j = 0, 0
    flag = 0

    while i < n:

        if s[i] == x[j]:
            flag = 1
            i += 1
            j += 1

        else:
            j = 0
            flag = 0

        i += 1
    return False

s = "ababaaaaaa"
x = "abaa"
print(strstr(s, x))