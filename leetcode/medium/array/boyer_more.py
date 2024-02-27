def boyerMoore(arr: list):
    candidate = None
    count = 0
    
    for element in arr:
        if element == candidate:
            count += 1
        else:
            count -= 1
            if count <= 0:
                candidate = element
                count = 1
    return candidate

if __name__ == "__main__":
    ar = [3,2,3]
    bm = boyerMoore(ar)
    print(bm)
    
        