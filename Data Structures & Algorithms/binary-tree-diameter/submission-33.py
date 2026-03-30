# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 
        def dfs(node):

            if not node:
                return 0 
            

            left_side = dfs(node.left)
            right_side = dfs(node.right)

            self.diameter = max(self.diameter,left_side+right_side)

            return 1 + max(left_side,right_side)
        
        dfs(root)
        return self.diameter
        
        
        