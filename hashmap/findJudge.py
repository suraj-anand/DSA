def findJudge(n: int, trust: list[list]) -> int:
    hashmap = { i:0 for i in range(1, n+1)}
    for ptrust in trust:
        person, trustedOn = ptrust
        hashmap[person] = -1
        
        if hashmap.get(trustedOn, 0) != -1:
            hashmap[trustedOn] = hashmap.get(trustedOn, 0) + 1
    
    print(hashmap)
    for key, val in hashmap.items():
        if val == n - 1:
            return val
    
    return -1
    

if __name__ == "__main__":
    n = 1
    trust = []
    
    r = findJudge(n=n, trust=trust)
    print(r)