class BinaryPostOrder:

    # Tree node definition
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    # Recursive postorder traversal
    @staticmethod
    def postorder(root, res):
        if root is None:
            return

        BinaryPostOrder.postorder(root.left, res)
        BinaryPostOrder.postorder(root.right, res)
        res.append(root.val)

    # Driver code
    @staticmethod
    def main():
        # Constructing the tree
        #     1
        #      \
        #       2
        #      /
        #     3

        root = BinaryPostOrder.TreeNode(1)
        root.right = BinaryPostOrder.TreeNode(2)
        root.right.left = BinaryPostOrder.TreeNode(3)

        result = []
        BinaryPostOrder.postorder(root, result)

        print("Postorder Traversal:", result)


# Run main
BinaryPostOrder.main()
