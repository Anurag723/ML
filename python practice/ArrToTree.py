class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ArrToTree:

    def sortedArrayToBST(self, nums):
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])

        node.left = self.build(nums, left, mid - 1)
        node.right = self.build(nums, mid + 1, right)

        return node

    # in-order traversal (should match sorted array)
    def print_inorder(self, root):
        if not root:
            return
        self.print_inorder(root.left)
        print(root.val, end=" ")
        self.print_inorder(root.right)


if __name__ == "__main__":
    converter = ArrToTree()

    nums = [-10, -3, 0, 5, 9]
    root = converter.sortedArrayToBST(nums)

    print("In-order traversal of BST:")
    converter.print_inorder(root)
