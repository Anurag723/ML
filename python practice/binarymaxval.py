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

    def max(self, root) -> int:
        if not root:
            return float('-inf')
        
        res = root.data
        left = self.max(root.left)
        right = self.max(root.right)

        return max(res, left, right)
    
    
bt = binarytree()
bt.create_binary_tree()
print(bt.max(bt.root))