def leaderElementsBrute(arr):
    result = []

    # Brute
    for (index, element) in enumerate(arr):
        isLeader = True
        for j in range(index+1, len(arr)):
            if element < arr[j]:
                isLeader = False
                break
        if isLeader:
            result.append(element)

    return result

def leaderElementsOptimal(arr):
    n = len(arr)
    result = []
    max = arr[n-1]

    for i in range(n-1, -1, -1):
        if i == n-1:
            result.append(arr[i])
        else:
            if arr[i] > max:
                result.append(arr[i])
                max = arr[i]
    
    return result


def main():
    arr = [1, 2, 3, 2]
    result = leaderElementsOptimal(arr)
    print(f"Leader Elements: {result}")


if __name__ == "__main__":
    main()