# Time = max(n1, n2)
# Space = max(n1, n2)

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addElement(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    def printList(self):
        point = self.head
        while point != None:
            print(point.data, end=" --> ")
            point = point.next
        print()
    
    def sumElement(self, head1, head2):
        pointer1 = self.head
        c = 0
        while head1 != None and head2 != None:
            s = head1.data + head2.data + c
            c = s // 10
            s = s % 10
            newNode = Node(s)
            if self.head == None:
                self.head = newNode
                pointer1 = self.head
            else:
                pointer1.next = newNode
                pointer1 = pointer1.next
            head1 = head1.next
            head2 = head2.next
        while head1 != None:
            s = head1.data + c
            c = s // 10
            s = s % 10
            newNode = Node(s)
            pointer1.next = newNode
            pointer1 = pointer1.next
            head1 = head1.next
        while head2 != None:
            s = head2.data + c
            c = s // 10
            s = s % 10
            newNode = Node(s)
            pointer1.next = newNode
            pointer1 = pointer1.next
            head2 = head2.next
        if c != 0:
            newNode = Node(c)
            pointer1.next = newNode

            
llist1 = LinkedList()
llist1.addElement(9)
llist1.addElement(4)
llist1.addElement(2)

llist2 = LinkedList()
llist2.addElement(4)
llist2.addElement(6)
llist2.addElement(5)

llist1.printList()
llist2.printList()

llist3 = LinkedList()
llist3.sumElement(llist1.head, llist2.head)
llist3.printList()