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
        left_side = self.invertTree(root.left)
        right_side = self.invertTree(root.right)

        temp = left_side
        root.right = temp
        root.left = right_side

        return root