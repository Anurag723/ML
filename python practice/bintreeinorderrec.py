class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None
    
    def create_binary_tree(self):
        first = node(1)
        second = node(2)
        third = node(3)
        fourth = node(4)
        fifth = node(5)
        sixth = node(6)
        seventh = node(7)

        self.root = first
        first.left = second
        first.right = third
        second.left = fourth
        second.right = fifth
        third.left = sixth
        third.right = seventh

    def recinorder(self, node):
        if node:
            self.recinorder(node.left)
            print(node.data, end = " ")
            self.recinorder(node.right)

bt = tree()
bt.create_binary_tree()
bt.recinorder(bt.root)