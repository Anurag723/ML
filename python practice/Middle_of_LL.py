class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Utility function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# Utility function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


# Main block to test the implementation
if __name__ == "__main__":
    # Example input
    values = [1, 2, 3, 4, 5]

    # Create linked list
    head = create_linked_list(values)

    # Print original list
    print("Original list:")
    print_linked_list(head)

    # Find the middle node
    solution = Solution()
    middle = solution.middleNode(head)

    # Print result from middle node onwards
    print("Middle node onward:")
    print_linked_list(middle)
