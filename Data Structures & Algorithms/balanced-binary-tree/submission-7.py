# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_valid(root):
            if not root:
                return 0
            
            left_depth = check_valid(root.left)
            right_depth = check_valid(root.right)

            if abs(left_depth - right_depth) > 1:
                return - 1
            
            if left_depth == -1 or right_depth == -1:
                return -1

            return 1 + max(left_depth,right_depth)
        return check_valid(root) != -1
            
