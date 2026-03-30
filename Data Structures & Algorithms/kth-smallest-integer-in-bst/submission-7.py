# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(node,k):
            nonlocal count
            if not node:
                return None
            
            left_result = dfs(node.left,k)
            if left_result is not None:
                return left_result
            
            count += 1
            if k == count:
                return node
            
            right_result = dfs(node.right,k)
            if right_result is not None:
                return right_result
            
            
        node =  dfs(root,k)
        return node.val
            

        