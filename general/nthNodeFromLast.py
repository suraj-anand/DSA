class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def create(self, array: list):
        if not array:
            raise Exception("Please provide an array with atleast of 1 element")
        self.head = Node(array[0])
        
        temp = self.head
        for i in array[1:]:
            newNode = Node(i)
            temp.next = newNode
            temp = newNode
    
    def printLL(self):
        temp = self.head
        while temp != None:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print()

    def nNodeFromLast(self, n):
        i = j = self.head

        count = 0
        while count < n:
            if j != None:
                j = j.next
            else:
                raise Exception(f"{n} is greater than the size of the LL")
            count += 1
        
        while j != None:
            i = i.next
            j = j.next
        
        print(f'{n}th Node from the Last is {i.data}')
    
    
        
ll = LinkedList()
ll.create(array=[1, 2, 3, 4, 5])
ll.printLL()
ll.nNodeFromLast(3)