class Stack:
    def __init__(self):
        self.array = []
    
    def push(self, element):
        self.array.append(element)
        return self.array
    
    def isEmpty(self):
        return len(self.array) == 0
    
    def pop(self):
        return self.array.pop()
    
    def topElement(self):
        if len(self.array) <= 0:
            return False
        return self.array[-1]


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    hashmap = {
        '(' : ')', 
        '{' : '}', 
        '[' : ']'
    }
    opening = set(["(", "{", "["])
    closing = set([")", "}", "]"])
    
    stack = Stack()

    for symbol in s:
        if symbol in opening:
            stack.push(symbol)
        
        elif symbol in closing:
            if stack.isEmpty():
                return False
            topElement = stack.pop()
            if symbol != hashmap[topElement]:
                return False
    
    return stack.isEmpty()

if __name__ == "__main__":
    s = "()[]{}{}"
    result = isValid(s)
    print(result)