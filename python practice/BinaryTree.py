from collections import deque

class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    # Insert (Binary Search Tree style)
    def insert(self, value):
        if self.data is None:
            self.data = value
            return

        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinaryTree(value)

    # Inorder Traversal
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    # Preorder Traversal
    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # Postorder Traversal
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

    # Level Order Traversal
    def level_order(self):
        q = deque([self])
        while q:
            node = q.popleft()
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


# ---------------- RUNNER CODE ----------------
if __name__ == "__main__":
    tree = BinaryTree()

    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        tree.insert(v)

    print("Inorder Traversal:")
    tree.inorder()

    print("\nPreorder Traversal:")
    tree.preorder()

    print("\nPostorder Traversal:")
    tree.postorder()

    print("\nLevel Order Traversal:")
    tree.level_order()
