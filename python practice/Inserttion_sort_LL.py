class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(float('-inf'))
        dummy.next = head
        curr = head

        while curr and curr.next:
            # If the current node is already <= next, continue
            if curr.val <= curr.next.val:
                curr = curr.next
                continue

            # Extract the node to be reinserted
            to_insert = curr.next
            curr.next = to_insert.next

            # Runner scans from the beginning of the sorted part
            runner = dummy
            while runner.next and runner.next.val < to_insert.val:
                runner = runner.next

            # Insert the node
            to_insert.next = runner.next
            runner.next = to_insert

        return dummy.next
