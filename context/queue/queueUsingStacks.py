class Queue:
    def __init__(self):
        self.array = []
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        arr = []
        if (self.front > self.rear) or (self.front == -1 or self.rear == -1):
            return f"queue => {[]}, front => {q.front}, rear => {q.rear}"
        for i in range(self.front, self.rear + 1):
            arr.append(q.array[i])
        return f"queue => {arr}, front => {q.front}, rear => {q.rear}"
    
    def enqueue(self, element):
        if self.isEmpty():
            self.front += 1
        self.array.append(element)
        self.rear += 1
    
    def dequeue(self):
        deletedElement = None
        if self.isEmpty():
            print("Queue Underflow")
        elif self.front == self.rear:
            deletedElement = self.array[self.front]
            self.array[self.front] = 0
            self.front = -1
            self.rear = -1
        else:
            deletedElement = self.array[self.front]
            self.array[self.front] = 0
            self.front += 1
        return deletedElement
        
    def isEmpty(self):
        return self.front == self.rear == -1
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.front]
        else:
            print("Queue Empty")

class Stack: 
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()
    
    def __str__(self) -> str:
        return f"Stack => {self.q2}"
    
    def push(self, element):
        
        self.q1.enqueue(element)
        
        while not self.q1.isEmpty():
            self.q2.enqueue()
    
    def pop(self):
        pass

    def peek(self):
        pass
    
stack = Stack()
while True:
    choice = input("Enter Choice: ")
    
    if choice == "print":
        print(stack)
    
    elif choice == "push":
        element = int(input("Enter element to enqueue to queue:"))
        stack.push(element)
    
    elif choice == "pop":
        ele = stack.pop()
        print(f"Dequeqed element: {ele}")
    
    elif choice == "peek":
        print(stack.peek())
    
    elif choice == "exit()":
        break
        