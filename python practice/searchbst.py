from collections import deque

class BSTSearch:
    class Node:
        def __init__(self, val):
            self.left = None
            self.data = val
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return self.Node(val)

        if val < root.data:
            root.left = self.insert(root.left, val)
        elif val > root.data:
            root.right = self.insert(root.right, val)

        return root

    def createbst(self):
        first = self.Node(6)
        sec = self.Node(4)
        three = self.Node(8)
        fourth = self.Node(3)
        fifth = self.Node(5)
        sixth = self.Node(7)
        seventh = self.Node(9)

        self.root = first

        first.left = sec
        first.right = three

        sec.left = fourth
        sec.right = fifth

        three.left = sixth
        three.right = seventh

    def traversal(self):
        if self.root is None:
            return

        que = deque()
        que.append(self.root)

        while que:
            temp = que.popleft()
            print(temp.data, end=" ")

            if temp.left:
                que.append(temp.left)
            if temp.right:
                que.append(temp.right)
        print()

    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

# Main
if __name__ == "__main__":
    tree = BSTSearch()
    tree.createbst()
    tree.root = tree.insert(tree.root, 2)
    tree.root = tree.insert(tree.root, 10)
    res = tree.search(tree.root, 6)
    print(res.data if res else "Not Found")
