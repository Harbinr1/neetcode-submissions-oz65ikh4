# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(node,subNode):
            if not node and not subNode:
                return True
            
            if not subNode and node:
                return False
            
            if subNode and not node:
                return False
            
            if node.val != subNode.val:
                return False
            
            left = isSame(node.left,subNode.left)
            right = isSame(node.right,subNode.right)

            return left and right

        if not subRoot:
            return True
            
        if not root:
            return False

        if isSame(root,subRoot):
            return True
            
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



            
        
        