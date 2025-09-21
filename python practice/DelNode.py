class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Deletes the given node (not the tail) from a singly linked list.
        """
        if node is None or node.next is None:
            return  # Cannot delete if it's None or the last node

        node.val = node.next.val
        node.next = node.next.next

# Helper function to build a linked list from list of values
def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test runner
if __name__ == "__main__":
    # Create linked list: 4 -> 5 -> 1 -> 9
    values = [4, 5, 1, 9]
    head = build_linked_list(values)

    print("Original list:")
    print_linked_list(head)

    # Find the node with value 5 (second node)
    node_to_delete = head.next  # node with value 5

    # Delete node using the solution
    Solution().deleteNode(node_to_delete)

    print("\nAfter deleting node with value 5:")
    print_linked_list(head)
