class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DetLoop:
    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self, limit=20):
        curr = self.head
        count = 0
        while curr and count < limit:
            print(curr.data, end=" -> ")
            curr = curr.next
            count += 1
        if curr:
            print("... (possible cycle detected)")
        else:
            print("None")

    # ✅ Cycle Detection using Floyd's Algorithm
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    # ⛓️ Introduce a cycle for testing: link last node to node at position `pos` (1-based index)
    def create_cycle(self, pos):
        if pos <= 0:
            return

        loop_node = None
        curr = self.head
        last = None
        index = 1

        while curr:
            if index == pos:
                loop_node = curr
            last = curr
            curr = curr.next
            index += 1

        if last and loop_node:
            last.next = loop_node  # Create cycle

# ---------------------------------------------
# 🔽 Test the implementation
if __name__ == "__main__":
    ll = DetLoop()

    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    ll.insert_end(40)
    ll.insert_end(50)

    print("Linked List (before creating cycle):")
    ll.print_list()

    print("Cycle detected?", ll.has_cycle())  # Should be False

    # Create a cycle: last node points to node at position 2 (value 20)
    ll.create_cycle(2)

    print("\nLinked List (after creating cycle):")
    ll.print_list()  # Limited print to avoid infinite loop

    print("Cycle detected?", ll.has_cycle())  # Should be True
