# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, curr):
            if not root:
                return False

            curr += root.val
            if not root.left and not root.right and curr == targetSum:
                return True
            
            return dfs(root.left, curr) or dfs(root.right, curr)

        return dfs(root, 0)