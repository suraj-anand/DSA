def removeOuterParentheses(string):
    
    numOfClose, numOfOpen = 0, 0
    primitiveStart = 0
    result = ""
    
    for i in range(len(string)):
        if string[i] == "(":
            numOfOpen += 1
        elif string[i] == ")":
            numOfClose += 1

        if numOfClose == numOfOpen:
            primitive = string[primitiveStart: i + 1]
            result += primitive[1:len(primitive)-1]
            primitiveStart = i + 1
    return result

if __name__ == "__main__":
    s = "(()())(())(()(()))"
    result = removeOuterParentheses(s)
    
    print(f'Result => {result}')