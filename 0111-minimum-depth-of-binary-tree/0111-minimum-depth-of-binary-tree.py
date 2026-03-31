# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, ans, depths):
            if node is None:
                return ans
            ans += 1
            if node.left is None and node.right is None:
                depths.append(ans)
            print(ans)
            left = dfs(node.left, ans, depths)
            right = dfs(node.right, ans, depths)
            return max(left, right)
        
        depths = []
        dfs(root, 0, depths)
        if depths:
            return min(depths)