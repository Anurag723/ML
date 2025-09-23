class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ReversesllIter:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_beg(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Insert at a specific position (1-based index)
    def insert_at(self, val, pos):
        new_node = Node(val)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        count = 1
        while count < pos - 1 and curr is not None:
            curr = curr.next
            count += 1
        if curr is None:
            print("Position out of bounds")
            return
        new_node.next = curr.next
        curr.next = new_node

    # Delete from beginning
    def del_beg(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp

    # Delete from end
    def del_end(self):
        if self.head is None or self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        return curr

    # Delete at a specific position (1-based index)
    def del_at(self, pos):
        if self.head is None:
            return
        if pos == 1:
            self.head = self.head.next
            return
        curr = self.head
        count = 1
        while count < pos - 1 and curr.next is not None:
            curr = curr.next
            count += 1
        if curr.next is None:
            print("Position out of bounds")
            return
        curr.next = curr.next.next

    # Reverse the linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # Print the linked list
    def print_list(self):
        curr = self.head
        while curr:
            print(f"{curr.data}->", end="")
            curr = curr.next
        print("None")

# -------------------------
# Main function to test
# -------------------------
if __name__ == "__main__":
    ll = ReversesllIter()

    # Insert elements
    ll.insert_beg(10)
    ll.insert_beg(20)
    ll.insert_end(30)
    ll.insert_at(25, 3)

    print("Original List:")
    ll.print_list()

    ll.reverse()
    print("Reversed List:")
    ll.print_list()

    ll.del_beg()
    print("After deleting from beginning:")
    ll.print_list()

    ll.del_end()
    print("After deleting from end:")
    ll.print_list()

    ll.del_at(2)
    print("After deleting at position 2:")
    ll.print_list()
