# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mid = root

        while mid:
            if p.val > mid.val and q.val > mid.val:
                mid = mid.right
            
            elif p.val < mid.val and q.val < mid.val:
                mid = mid.left
            

            else:
                return mid

        