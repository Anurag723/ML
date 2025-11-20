class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class InsertSortedClass:

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                # Case 1: Already in sorted order
                lastSorted = curr
            else:
                # Case 2: Insert curr into sorted portion
                prev = dummy
                while prev.next and prev.next.val < curr.val:
                    prev = prev.next

                # Insert curr
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = lastSorted.next

        return dummy.next

    # build a linked list from a Python list
    def build_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        cur = head
        for value in arr[1:]:
            cur.next = ListNode(value)
            cur = cur.next
        return head

    # print linked list
    def print_list(self, head):
        cur = head
        vals = []
        while cur:
            vals.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(vals))


# Main test
if __name__ == "__main__":
    isc = InsertSortedClass()

    arr = [4, 2, 1, 3]
    head = isc.build_list(arr)

    print("Original List:")
    isc.print_list(head)

    sorted_head = isc.insertionSortList(head)

    print("Sorted List:")
    isc.print_list(sorted_head)
