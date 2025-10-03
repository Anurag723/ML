class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Check if there are at least k nodes left
        count = 0
        ptr = head
        while ptr and count < k:
            ptr = ptr.next
            count += 1
        
        if count < k:
            return head  # Not enough nodes to reverse

        # Step 2: Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3: head becomes the end of the reversed group, so connect it to next group
        head.next = self.reverseKGroup(curr, k)

        # Step 4: Return new head (which is 'prev' after reversal)
        return prev

# Helper: Create a linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper: Print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# Main function to run the solution
def main():
    input_values = [1, 2, 3, 4, 5]
    k = 2

    head = create_linked_list(input_values)
    print("Original List:")
    print_linked_list(head)

    solution = Solution()
    result = solution.reverseKGroup(head, k)

    print(f"Reversed in groups of {k}:")
    print_linked_list(result)

if __name__ == "__main__":
    main()
