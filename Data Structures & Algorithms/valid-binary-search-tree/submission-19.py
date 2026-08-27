# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = float('inf')
        low = float('-inf')

        def dfs(root,low,high):
            if not root:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            left = dfs(root.left,low,root.val)
            right = dfs(root.right,root.val,high)

            return left and right

        return dfs(root,float('-inf'),float('inf'))
        