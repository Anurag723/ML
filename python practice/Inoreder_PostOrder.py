class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Inorder_Postorder:

    def buildTree(self, inorder, postorder):
        # Map value -> index for O(1) lookup
        self.idx_map = {v: i for i in inorder}

        # Index of last element in postorder
        self.post_index = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None

            # Get root from postorder
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)

            # Split by inorder index
            mid = self.idx_map[root_val]

            # Build right subtree first
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)


def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


def main():
    inorder =  [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Inorder_Postorder()
    root = sol.buildTree(inorder, postorder)

    print("Preorder of constructed tree:")
    print_preorder(root)


if __name__ == "__main__":
    main()
