# Time = n
# Space = 1

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def pushElement(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print()
    
    def reverse(self):
        if not self.head:
            return self.head
        prev = None
        curr = self.head
        foll = self.head.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = foll
            if foll:
                foll = foll.next
        self.head = prev

llist = LinkedList()
llist.pushElement(5)
llist.pushElement(4)
llist.pushElement(3)
llist.pushElement(2)
llist.pushElement(1)
llist.printLinkedList()
llist.reverse()
llist.printLinkedList()

