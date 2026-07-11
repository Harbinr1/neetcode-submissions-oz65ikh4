# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0

        def max_depth(root):
            if not root:
                return 0
            
            left_side = max_depth(root.left)
            right_side = max_depth(root.right)

            self.longest = max(self.longest,left_side + right_side)

            return 1 + max(left_side,right_side)
        max_depth(root)
        return self.longest

        