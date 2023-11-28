
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, arr):
        self.head = None

        if not arr:
            raise Exception("Invalid Array")

        self.head = Node(arr[0])
        t = self.head
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            t.next = temp
            t = temp

    def __str__(self):
        result = ""
        temp = self.head
        while temp != None:
            result += f"{temp.data} -> "
            temp = temp.next
        return result

    def insertAtFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertAtLast(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
    
    def insertAtIndex(self, data, index):
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        count = 0
        temp = self.head
        while temp != None:
            count += 1
            if count == index:
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next

    def deleteFirst(self):
        if self.head == None:
            print("LL is Empty")
            return 
        self.head = self.head.next

    def deleteLast(self):
        if self.head == None:
            print("LL is empty")
            return
        temp = self.head
        while temp.next.next != None: # points to the second last
            temp = temp.next
        temp.next = None

    def deleteAtIndex(self, index):
        if self.head == None:
            print("LL is Empty")
            return
        if index == 0:
            self.head = self.head.next
        temp = self.head
        prev = self.head
        count = 0
        while temp != None:
            count += 1
            if count == index:
                prev.next = temp.next
            prev = temp
            temp = temp.next

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    l1 = LinkedList(arr)
    print(l1)
    l1.deleteAtIndex(0)
    print(l1)