class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DeleteMed:

    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Delete the middle node
        prev.next = slow.next

        return head

    def runner(self):
        # Create the list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1,
                ListNode(2,
                ListNode(3,
                ListNode(4,
                ListNode(5)))))

        result = self.deleteMiddle(head)
        self.printList(result)

    def printList(self, head: ListNode):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        print()

if __name__ == "__main__":
    dm = DeleteMed()
    dm.runner()
