class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeKLists:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        # Keep merging pairs until only one list remains
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwo(l1, l2))
            lists = merged_lists
        
        return lists[0]

    def mergeTwo(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwo(l1, l2.next)
            return l2

# Helper functions for building and printing lists
def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Runner code
if __name__ == "__main__":
    solution = MergeKLists()

    # Create test linked lists
    l1 = build_list([1, 4, 5])
    l2 = build_list([1, 3, 4])
    l3 = build_list([2, 6])

    lists = [l1, l2, l3]

    # Merge all k sorted lists
    merged = solution.mergeKLists(lists)

    # Print the result
    print("Merged Sorted List:")
    print_list(merged)
