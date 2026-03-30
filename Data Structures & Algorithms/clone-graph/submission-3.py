"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone_n = Node(node.val)
        cloned_map = {}
        cloned_map[node] = clone_n
        
        q = deque([node])
        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in cloned_map:
                    cloned_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                cloned_map[curr].neighbors.append(cloned_map[neighbor])
        return clone_n    