class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, arr: list):
        self.head = None

        if not arr:
            raise Exception("Not a valid array")
        
        newNode = Node(arr[0])
        self.head = newNode
        prev = newNode

        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            newNode.prev = prev
            prev.next = newNode
            prev = newNode
    
    def __str__(self):
        temp = self.head
        result = ""
        while temp != None:
            result += f"{temp.data} <=> "
            temp = temp.next
        return result
    
    def print_in_reverse(self): # O(2N) - Can be further optimised
        tail = self.head
        while tail.next != None:
            tail = tail.next
        while tail != None:
            print(f"{tail.data} <=> ", end='')
            tail = tail.prev
    
    def insert_at_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insert_at_last(self, data):
        newNode = Node(data)
        if self.head == None or self.head.next == None:
            self.head = newNode
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        temp.next = newNode
        newNode.prev = temp


array = [10, 20, 30, 40, 50]
dll = DoublyLinkedList(array)
dll.insert_at_begin(5)
dll.insert_at_last(60)
print(dll)