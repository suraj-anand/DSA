class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
        
    def create(self, arr: list):
        n = len(arr)
        if n == 0:
            raise Exception(f"Atlease one element is required")
        
        self.head = Node(data=arr[0])
        temp = self.head
        idx = 1
        while idx < n:
            newnode = Node(data=arr[idx])
            temp.next = newnode
            temp = newnode
            idx += 1
        return self.head
    
    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()
    
    def insertHead(self, element):
        newnode = Node(data=element)
        newnode.next = self.head
        self.head = newnode

    def insertTail(self, element):
        if self.isEmpty():
            self.head = Node(data=element)
            return self.head
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data=element)
        return self.head
    
    def insertPosition(self, element, position):
        if position == 0:
            return self.insertHead(element)
        
        count = 0
        temp = self.head
        while temp != None:
            if count == position - 1:
                break
            temp = temp.next
            count += 1
        
        if temp:
            newnode = Node(data=element)
            newnode.next = temp.next
            temp.next = newnode
        return self.head 
            
    def deleteHead(self):
        if self.isEmpty():
            return self.head

        self.head = self.head.next
        return self.head
    
    def deleteTail(self):
        if self.isEmpty():
            return self.head

        prev = self.head
        temp = self.head
        while temp.next != None:
            prev = temp
            temp = temp.next
        
        prev.next = None
        return self.head
    
    def deletePosition(self, position):
        if position == 0:
            return self.deleteHead()
        
        count = 0
        prev = self.head
        temp = self.head
        while temp != None:
            if count == position:
                break
            count += 1
            prev = temp
            temp = temp.next
        
        if temp:
            prev.next = temp.next
        return self.head
        
if __name__ == "__main__":
    ll = LinkedList()
    arr = [10,20,30]
    head = ll.create(arr)
    ll.deletePosition(position=2)
    ll.print()
    