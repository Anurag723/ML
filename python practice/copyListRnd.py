class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None

    # Step 1: Interleave original and copied nodes
    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate original and copied list
    curr = head
    dummy = Node(0)
    temp = dummy

    while curr:
        temp.next = curr.next
        temp = temp.next

        curr.next = curr.next.next
        curr = curr.next

    return dummy.next

# Helper to print list with random pointers
def print_list(head):
    curr = head
    while curr:
        rand_val = curr.random.val if curr.random else "None"
        print(f"Node({curr.val}) -> Random({rand_val})")
        curr = curr.next
    print()

def main():
    # Create nodes: 1 -> 2 -> 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    # Link next pointers
    n1.next = n2
    n2.next = n3

    # Set random pointers
    n1.random = n3     # 1 → 3
    n2.random = n1     # 2 → 1
    n3.random = n3     # 3 → 3

    print("Original list:")
    print_list(n1)

    # Deep copy
    copied_head = copy_random_list(n1)

    print("Copied list:")
    print_list(copied_head)

if __name__ == "__main__":
    main()
