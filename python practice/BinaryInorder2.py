class BinaryInorder2:

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    @staticmethod
    def inorderTraversal(root):
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res


if __name__ == "__main__":

    root = BinaryInorder2.TreeNode(1)
    root.right = BinaryInorder2.TreeNode(2)
    root.right.left = BinaryInorder2.TreeNode(3)

    print(BinaryInorder2.inorderTraversal(root))
