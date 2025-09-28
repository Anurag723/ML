class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the n-th node from end
    slow.next = slow.next.next

    return dummy.next

# Helper function to create a linked list from a list of values
def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Main function to test the code
def main():
    values = [1, 2, 3, 4, 5]
    n = 2

    print("Original list:")
    head = build_list(values)
    print_list(head)

    head = remove_nth_from_end(head, n)

    print(f"After removing {n}-th node from the end:")
    print_list(head)

if __name__ == "__main__":
    main()
