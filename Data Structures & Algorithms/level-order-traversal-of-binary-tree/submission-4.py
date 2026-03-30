# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        q = deque()
        result = []
        levels = []
        if not root:
            return []
        else:
            q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                levels.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(levels)
            levels = []
        return result
        

            

        