def charToInt(char):
    return ord(char) - ord("0")

def stringToInt(string):
    num = 0
    for i in string:
        num = (num * 10) + charToInt(i)
    return num
        
def multiply(num1, num2):
    n1 = stringToInt(num1)
    n2 = stringToInt(num2)
    return n1 * n2

if __name__ == "__main__":
    num1 = "2"
    num2 = "345"
    
    i = len(num1) - 1
    j = len(num2) - 1
    
    while i < len(num1) or j < len(num2):
        r = charToInt(num1[i]) * charToInt(num2[j])
        
    
    print(multiply(num1, num2))