class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def __init__(self):
        self.root = None

    def create_binary_tree(self):
        first = treeNode(1)
        second = treeNode(2)
        third = treeNode(3)
        fourth = treeNode(4)
        fifth = treeNode(5)
        sixth = treeNode(6)
        seventh = treeNode(7)

        self.root = first
        first.left = second
        first.right = third
        second.left = fourth
        second.right = fifth
        third.left = sixth
        third.right = seventh

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)


bt = binarytree()
bt.create_binary_tree()
print("Inorder Traversal of the Binary Tree:")
bt.inorder_traversal(bt.root)