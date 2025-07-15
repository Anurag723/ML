class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at beginning (optional)
    def insert_at_beginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete first occurrence (optional)
    def delete(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        if prev is None:
            self.head = self.head.next
        else:
            prev.next = temp.next

def twosum(ll1:node, ll2:node) -> node:
    res = node(0)
    curr = res

    carry = 0
    while ll1 or ll2:
        x = ll1.data if ll1 is not None else 0
        y = ll2.data if ll2 is not None else 0

        sum = x+y+carry
        carry = sum//10

        curr.next = node(sum%10)
        curr = curr.next

        if ll1:ll1 = ll1.next
        if ll2:ll2 = ll2.next

    if carry != 0: curr.next = node(carry)
    return res.next



def prt(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")



ll1 = linkedlist()
ll1.insert(2)
ll1.insert(4)
ll1.insert(5)


ll2 = linkedlist()
ll2.insert(5)
ll2.insert(6)
ll2.insert(4)

res = twosum(ll1.head, ll2.head)
prt(res)