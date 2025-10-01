class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Intersection:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pointA = headA
        pointB = headB

        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA

        return pointA

if __name__ == "__main__":
    # Shared part of the lists
    common = ListNode(8)
    common.next = ListNode(10)

    # First list: 3 -> 7 -> 8 -> 10
    headA = ListNode(3)
    headA.next = ListNode(7)
    headA.next.next = common

    # Second list: 99 -> 1 -> 8 -> 10
    headB = ListNode(99)
    headB.next = ListNode(1)
    headB.next.next = common

    intersection = Intersection()
    result = intersection.getIntersectionNode(headA, headB)

    if result:
        print(f"Intersection at node with value: {result.val}")
    else:
        print("No intersection.")
