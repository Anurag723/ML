class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
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

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


bt = tree()
bt.create_binary_tree()
bt.postorder(bt.root)