class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining part
        tail.next = list1 if list1 else list2

        return dummy.next

# Helper function to create a linked list from a Python list
def create_list(arr):
    dummy = ListNode(0)
    tail = dummy
    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Helper function to print a linked list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Runner code
if __name__ == "__main__":
    list1 = create_list([1, 3, 5])
    list2 = create_list([2, 4, 6])

    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)

    print("Merged List:")
    print_list(merged)
