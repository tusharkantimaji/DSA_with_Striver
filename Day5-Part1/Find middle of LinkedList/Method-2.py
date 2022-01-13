# Time = (n/2)
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
    
    def findMiddleElement(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data
    

llist = LinkedList()
# llist.pushElement(6)
llist.pushElement(5)
llist.pushElement(4)
llist.pushElement(3)
llist.pushElement(2)
llist.pushElement(1)
llist.printLinkedList()
middleElement = llist.findMiddleElement()
print(middleElement)