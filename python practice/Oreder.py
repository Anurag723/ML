# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Map each value to its index in inorder for O(1) lookup
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # pointer in preorder

        def helper(left, right):
            if left > right:
                return None

            # Pick root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Split inorder into left/right subtree
            mid = idx_map[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)

# -------- Runner Code --------

def print_inorder(root):
    """Print tree inorder for verification."""
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder  = [9, 3, 15, 20, 7]

    sol = Solution()
    tree = sol.buildTree(preorder, inorder)

    print("Inorder traversal of reconstructed tree:")
    print_inorder(tree)
    print()
