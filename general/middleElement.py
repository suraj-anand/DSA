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
    
    def findMiddle(self):
        slow = self.head
        fast = self.head

        while slow != None or fast != None:
            if fast == None or fast.next == None:
                print(f"Mid Element: {slow.data}")
                break
            slow = slow.next
            fast = fast.next.next
        
ll = LinkedList()
ll.create(array=[1,2,3,4])
ll.printLL()
ll.findMiddle()
