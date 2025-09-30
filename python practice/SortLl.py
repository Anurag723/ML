class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SortLl:
    def sortList(self, head):
        if not head or not head.next:
            return head

        premid = self.middle(head)
        mid = premid.next
        premid.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def middle(self, head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev

    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy.next

    def printList(self, head):
        while head:
            print(head.val, end=" -> " if head.next else "")
            head = head.next
        print()


# Main function to run the example
if __name__ == "__main__":
    # Create linked list: 4 -> 2 -> 1 -> 3
    node4 = ListNode(3)
    node3 = ListNode(1, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(4, node2)

    sorter = SortLl()

    print("Original list:")
    sorter.printList(node1)

    sorted_head = sorter.sortList(node1)

    print("Sorted list:")
    sorter.printList(sorted_head)
