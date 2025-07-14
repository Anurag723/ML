class node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class bintree:
    def __init__(self):
        self.root = None

    def levelord(self, root):
        if not root:
            return


        que = []
        que.append(root)

        while que:
            temp = que.pop()
            print(temp.data,end=" ")

            if temp.right:
                que.append(temp.right)

            if temp.left:
                que.append(temp.left)

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


bt = bintree()
bt.create_binary_tree()
bt.levelord(bt.root)