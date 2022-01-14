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
    def removeNth(self, n):
        fast = self.head
        slow = self.head
        for i in range(n):
            fast = fast.next
            if fast == None:
                if i == n-1:
                    return self.head.next
                return self.head
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head
        
llist = LinkedList()
llist.pushElement(5)
llist.pushElement(4)
llist.pushElement(3)
llist.pushElement(2)
llist.pushElement(1)
llist.printList()

llist.removeNth(5)

llist.printList()

