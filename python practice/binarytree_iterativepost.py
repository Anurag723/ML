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

    def iterativepost(self):
        if self.root:
            stack = []
            curr = self.root

            while stack or curr:
                if curr:
                    stack.append(curr)
                    curr = curr.left

                else:
                    temp = stack[-1].right

                    if not temp:
                        temp = stack.pop()
                        print(temp.data, end=" ")

                        while stack and temp == stack[-1].right:
                            temp = stack.pop()
                            print(temp.data, end= " ")

                    else:
                        curr = temp


bt =  tree()
bt.create_binary_tree()
bt.iterativepost()