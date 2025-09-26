class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Palindromell:
    def is_palindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Find middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second_half = self.reverse_list(slow)
        first_half = head

        # Compare both halves
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# Helper to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# Test code
if __name__ == "__main__":
    values = [1, 2, 3, 2, 1]  # Change values to test other inputs
    head = create_linked_list(values)
    checker = Palindromell()
    result = checker.is_palindrome(head)

    if result:
        print("The linked list is a palindrome.")
    else:
        print("The linked list is NOT a palindrome.")
