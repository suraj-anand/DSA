def atoi(s: str, factor=0) -> int:
    n = len(s)
    if n == 0:
        return 0
    
    if s.isdigit():
        r = int(s[0]) * (10 ** (n-1))
        return  r + atoi(s[1:]) 
    else:
        return 0 + atoi(s[1:])
    
if __name__ == "__main__":
    s = "  5 431"
    print(atoi(s))