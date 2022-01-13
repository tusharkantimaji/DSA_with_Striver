# Time = n + (n/2)
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
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        index = count//2 + 1
        temp = self.head
        while index > 1:
            temp = temp.next
            index -=  1
        return temp.data
    

llist = LinkedList()
llist.pushElement(6)
llist.pushElement(5)
llist.pushElement(4)
llist.pushElement(3)
llist.pushElement(2)
llist.pushElement(1)
llist.printLinkedList()
middleElement = llist.findMiddleElement()
print(middleElement)