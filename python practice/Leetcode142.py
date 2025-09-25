class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find the start of the cycle
                start = head
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start  # Start of the cycle

        return None  # No cycle

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_entry = None

    for i in range(1, len(values)):
        node = ListNode(values[i])
        current.next = node
        current = node
        if i == pos:
            cycle_entry = current

    if pos != -1:
        current.next = cycle_entry

    return head

# Test the implementation
if __name__ == "__main__":
    values = [3, 2, 0, -4]
    pos = 1  # Cycle starts at node with value 2

    head = create_linked_list_with_cycle(values, pos)
    solution = Solution()
    cycle_node = solution.detectCycle(head)

    if cycle_node:
        print(f"Cycle starts at node with value: {cycle_node.val}")
    else:
        print("No cycle detected.")
