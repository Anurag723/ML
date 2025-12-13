class RemDupEle:

    # Definition for singly-linked list
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    # Remove all elements that have duplicates
    @staticmethod
    def deleteDuplicates(head):
        dummy = RemDupEle.ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check for duplicates
            if curr.next and curr.val == curr.next.val:
                dupVal = curr.val
                # Skip all nodes with duplicate value
                while curr and curr.val == dupVal:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next

    # Utility method to print the list
    @staticmethod
    def printList(head):
        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    # Main method
    @staticmethod
    def main():
        # Creating sorted linked list:
        # 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
        head = RemDupEle.ListNode(1)
        head.next = RemDupEle.ListNode(2)
        head.next.next = RemDupEle.ListNode(3)
        head.next.next.next = RemDupEle.ListNode(3)
        head.next.next.next.next = RemDupEle.ListNode(4)
        head.next.next.next.next.next = RemDupEle.ListNode(4)
        head.next.next.next.next.next.next = RemDupEle.ListNode(5)

        print("Original List:")
        RemDupEle.printList(head)

        head = RemDupEle.deleteDuplicates(head)

        print("After Removing Duplicates:")
        RemDupEle.printList(head)


# Run main
if __name__ == "__main__":
    RemDupEle.main()
