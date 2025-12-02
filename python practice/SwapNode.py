class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNode:

    def swap_pairs(self, head):
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            # Swap
            first.next = second.next
            second.next = first
            curr.next = second

            curr = first  # move to next pair

        return dummy.next

    def print_list(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()


# Test the code
if __name__ == "__main__":
    sn = SwapNode()

    # Create list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    print("Original list:")
    sn.print_list(head)

    print("After swapping:")
    new_head = sn.swap_pairs(head)
    sn.print_list(new_head)
