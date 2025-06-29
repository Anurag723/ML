class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        nn = Node(data)

        if not self.head:
            self.head = nn
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = nn

    def print(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("null")


ll = linkedlist()

ll.insert(12)
ll.insert(14)
ll.insert(16)
ll.insert(18)
ll.insert(20)

ll.print()