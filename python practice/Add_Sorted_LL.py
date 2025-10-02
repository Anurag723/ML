class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AddTwoSortedLL:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(f"{curr.data}->", end="")
            curr = curr.next
        print("null")

    @staticmethod
    def find_sum(a, b):
        dummy = Node(0)
        tail = dummy
        carry = 0

        while a or b:
            x = a.data if a else 0
            y = b.data if b else 0

            total = carry + x + y
            carry = total // 10
            tail.next = Node(total % 10)
            tail = tail.next

            if a: a = a.next
            if b: b = b.next

        if carry > 0:
            tail.next = Node(carry)

        return dummy.next

# ----- Example Usage -----

if __name__ == "__main__":
    sll1 = AddTwoSortedLL()
    sll1.insert_end(1)
    sll1.insert_end(4)
    sll1.insert_end(8)

    sll2 = AddTwoSortedLL()
    sll2.insert_end(3)
    sll2.insert_end(5)
    sll2.insert_end(1)

    result = AddTwoSortedLL()
    result.head = AddTwoSortedLL.find_sum(sll1.head, sll2.head)
    
    result.print_list()
