def getSubSequences(n=0, arr=[], subseq: list=[]):
    if n > len(arr) - 1:
        print(subseq)
        return

    getSubSequences(n=n+1, arr=arr, subseq=[*subseq, arr[n]])
    if len(subseq) != 0:
        subseq.pop()
    getSubSequences(n=n-1, arr=arr, subseq=[*subseq, arr[n]])


if __name__ == "__main__":
    arr = [3, 5, 2]
    getSubSequences(n=0, arr=arr, subseq=[])    