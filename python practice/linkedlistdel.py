class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, val):
        nn = Node(val)

        if not self.head:
            self.head = nn
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = nn

    def delete(self):
        if not self.head:
            print("Linked list is empty!!!")
            return
        
        if not self.head.next:
            self.head = None
            return
        
        curr = self.head
        
        while curr.next and curr.next.next:
            curr = curr.next

        curr.next = None

    def print(self):
        curr = self.head
        while curr.next:
            print(curr.data,end = "->")
            curr = curr.next

        print("null")

ll = linkedlist()

ll.insert(12)
ll.insert(14)
ll.insert(16)
ll.insert(18)
ll.insert(20)

print("before delete...")
ll.print()

ll.delete()
print("after delete...")
ll.print()