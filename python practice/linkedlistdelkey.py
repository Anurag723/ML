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

    def delete(self, val) -> bool:
        if(self.head == None):
            print("List is already empty!!!")
            return False
        
        curr = self.head
        prev = None

        while curr:
            if curr.data == val:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next

        print("Value not found")
        return False

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
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

print("After delete!!!")

ll.delete(14)
ll.print()