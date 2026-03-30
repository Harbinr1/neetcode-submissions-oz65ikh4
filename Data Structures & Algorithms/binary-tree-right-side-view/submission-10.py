# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        result = []

        if root:
            q.append(root)
        else:
            return []

        while q:
            levels_size = len(q)
            
            for i in range(levels_size):
                node = q.popleft()
                if node and i == 0:
                    result.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                

        
        return result
