from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        originalList = {}
        current = head
        index = 0

        while current:
            originalList[index] = [current.val,current.random]
            current = current.next
            index += 1
        
        copyNodes = {}

        for idx,val in originalList.items():
            newNode = Node(val[0])
            copyNodes[idx] = newNode
        

        for i in range(len(copyNodes)- 1):
            copyNodes[i].next = copyNodes[i+1]
        copyNodes[len(copyNodes)-1].next = None


        node_to_index = {}
        current = head
        index = 0

        while current:
            node_to_index[current] = index
            current = current.next
            index += 1
        

        for i in range(len(copyNodes)):
            originalRandom = originalList[i][1]
            if originalRandom is None:
                copyNodes[i].random = None
            
            else:
                random_index = node_to_index[originalRandom]
                copyNodes[i].random = copyNodes[random_index]
        
        return copyNodes[0]