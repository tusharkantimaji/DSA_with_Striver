# Time = n1 + n2
# Space = n1 + n2

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
    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()
def addList(llist1, llist2):
    pointer1 = llist1.head
    pointer2 = llist2.head
    headNode = Node(None)
    duplicateNode = headNode
    while pointer1 != None and pointer2 != None:
        if pointer1.data < pointer2.data:
            newNode = Node(pointer1.data)
            duplicateNode.next = newNode
            pointer1 = pointer1.next
        else:
            newNode = Node(pointer2.data)
            duplicateNode.next = pointer2
            pointer2 = pointer2.next
        duplicateNode = duplicateNode.next
    while pointer1 != None:
        duplicateNode = pointer1
        pointer1 = pointer1.next
        duplicateNode = duplicateNode
    return headNode.next
        
llist1 = LinkedList()
llist1.pushElement(4)
llist1.pushElement(2)
llist1.pushElement(1)

llist2 = LinkedList()
llist2.pushElement(4)
llist2.pushElement(3)
llist2.pushElement(1)

llist1.printList()
llist2.printList()

llist3 = LinkedList()
llist1.head = addList(llist1, llist2)
llist1.printList()