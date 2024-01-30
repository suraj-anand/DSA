import math
debug = False

class Stack:
    def __init__(self):
        self.array = []
    
    def __str__(self):
        return f"stack => {self.array}"
    
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

def calc(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return math.trunc(a / b)
    else:
        raise Exception(f"Unknown Operator: {operator}")

def solve(tokens):
    stack = Stack()
    operators = ["+", "-", "*", "/"]
    
    for token in tokens:
        if token not in operators:
            stack.push(int(token))
        else:
            y = stack.pop()
            x = stack.pop()
            result = calc(x, token, y)
            stack.push(result)
    return stack.topElement()
            

if __name__ == "__main__":
    tests = [
        ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"],
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ]
    # for tokens in tests:
    print(solve(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    # if debug:
        # break
        
    
    