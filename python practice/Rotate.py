class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class RotateLL:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute the length and get the tail
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        # Step 2: Normalize k
        k = k % length
        if k == 0:
            return head

        # Step 3: Find new tail (length - k - 1) and new head
        tail = head
        for _ in range(length - k - 1):
            tail = tail.next

        new_head = tail.next
        tail.next = None
        curr.next = head

        return new_head

    def printList(self, head: ListNode):
        current = head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()

    def createList(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


if __name__ == "__main__":
    rll = RotateLL()
    
    # Example input
    nums = [1, 2, 3, 4, 5]
    k = 2

    # Create linked list
    head = rll.createList(nums)

    print("Original List:")
    rll.printList(head)

    # Rotate list
    rotated = rll.rotateRight(head, k)

    print("Rotated List:")
    rll.printList(rotated)
