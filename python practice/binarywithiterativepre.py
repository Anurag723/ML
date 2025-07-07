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

    def recpreorder(self,node):
        if node:
            print(node.data,end=" ")
            self.recpreorder(node.left)
            self.recpreorder(node.right)

    def itrpreorder(self, node):
        if node:
            stack, result = [node], []
            while stack:
                nn = stack.pop()
                result.append(nn)

                if nn.right:
                    stack.append(nn.right)

                if nn.left:
                    stack.append(nn.left)


            return result
        
        else:
            return []
        
bt = tree()
bt.create_binary_tree()
print("Iterative preOrder approach")
result = bt.itrpreorder(bt.root)

for i in result:
    print(i.data,end=" ")