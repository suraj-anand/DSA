def printn(n: int):
    if n <= 0:
        return
    print("Hello")
    printn(n-1)

if __name__ == "__main__":
    printn(5)
