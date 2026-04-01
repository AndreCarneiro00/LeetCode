# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def max_depth(node):
            if not node:
                return 0

            left = max_depth(node.left)
            right = max_depth(node.right)
            return max(left, right) + 1

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        print(left_depth, right_depth)
        self.ans = max(left_depth + right_depth, self.ans)
        return self.ans
