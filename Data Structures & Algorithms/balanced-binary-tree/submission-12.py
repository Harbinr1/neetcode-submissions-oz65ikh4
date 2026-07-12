# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0 
            
            left_side = dfs(root.left)
            if left_side == -1:
                return -1
            
            right_side = dfs(root.right)
            if right_side == -1:
                return -1
            
            if abs(left_side - right_side) > 1:
                return -1
            
            return 1 + max(left_side,right_side)
        
        return dfs(root) != -1