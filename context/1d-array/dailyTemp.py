def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    
    # O(n^2) - brute , TLE
    for i in range(n):
        foundGreater = False
        waitingDays = 0
        for j in range(i+1, n):
            waitingDays += 1
            if temperatures[i] < temperatures[j]:
                foundGreater = True
                break
        if foundGreater:
            answer[i] = waitingDays
        else:
            answer[i] = 0
        
    return answer
    
if __name__ == "__main__":
    temperatures = [89,62,70,58,47,47,46,76,100,70]
    
    result = dailyTemperatures(temperatures)
    print(result)
    
    
