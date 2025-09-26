class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LoopLength:
    def detectCycle(self, head):
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

    def findLoopLength(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Loop detected, now find length
                loop_length = 1
                current = slow.next
                while current != slow:
                    loop_length += 1
                    current = current.next
                return loop_length

        return 0  # No loop


# Helper function to create linked list with a cycle
def createLinkedListWithCycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_entry = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_entry = current

    if pos != -1:
        current.next = cycle_entry

    return head


# Main function
def main():
    # Example: values = [3, 2, 0, -4], cycle starts at index 1 (value 2)
    values = [3, 2, 0, -4]
    pos = 1

    head = createLinkedListWithCycle(values, pos)
    loop_finder = LoopLength()

    cycle_start = loop_finder.detectCycle(head)
    if cycle_start:
        print("Cycle starts at node with value:", cycle_start.val)
    else:
        print("No cycle detected.")

    loop_length = loop_finder.findLoopLength(head)
    print("Length of the loop:", loop_length)


if __name__ == "__main__":
    main()
