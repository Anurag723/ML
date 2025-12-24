class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    # Move pre to the node before left
    for _ in range(left - 1):
        pre = pre.next

    curr = pre.next
    # Reverse sublist
    for _ in range(right - left):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = pre.next
        pre.next = next_node

    return dummy.next

# Helper function to print the list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List: ", end="")
    print_list(head)

    head = reverse_between(head, 2, 4)

    print("Reversed List (2 to 4): ", end="")
    print_list(head)
