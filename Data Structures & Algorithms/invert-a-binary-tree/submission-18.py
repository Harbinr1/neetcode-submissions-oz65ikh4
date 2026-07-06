# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        leftSide = self.invertTree(root.left)
        rightSide = self.invertTree(root.right)

        temp = leftSide
        
        root.right  = temp
        root.left = rightSide

        return root
        