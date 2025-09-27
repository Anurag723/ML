class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class OddEven:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        curr = head.next.next
        odd = head
        even = head.next
        eve = even
        count = 1

        while curr is not None:
            if count % 2 != 0:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            curr = curr.next
            count += 1

        even.next = None
        odd.next = eve

        return head

    # Helper method to create a linked list from a list
    def create_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper method to print a linked list
    def print_list(self, head):
        current = head
        while current:
            print(f"{current.val} -> ", end="")
            current = current.next
        print("None")


# Test code
if __name__ == "__main__":
    solution = OddEven()

    # Test input
    arr = [1, 2, 3, 4, 5]
    head = solution.create_list(arr)

    print("Original List:")
    solution.print_list(head)

    result = solution.oddEvenList(head)

    print("Modified List:")
    solution.print_list(result)
