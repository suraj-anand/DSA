class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        
    def __str__(self):
        return f"stack: {self.array}, top: {self.top}"
    
    def push(self, element):
        self.array.append(element)
        self.top += 1
    
    def pop(self):
        if self.isEmpty():
            print("Underflow")
            return
        
        self.top -= 1
        return self.array.pop()
    
    def isEmpty(self):
        return self.top == -1
    
    def peek(self):
        return self.array[self.top]
    
stack1 = Stack()
stack2 = Stack()

while True:
    choice = input("Enter Choice: ")
    
    if choice == "print":
        print(f"queue => {stack2}")
    
    elif choice == "push":
        element = int(input("Enter element to push to queue:"))
        while not stack2.isEmpty():
            stack1.push(stack2.pop())
        stack2.push(element)
        while not stack1.isEmpty():
            stack2.push(stack1.pop())
    
    elif choice == "pop":
        print("Popped element", stack2.pop())
    
    elif choice == "peek":
        print(stack2.peek())
    
    else:
        break
        
        