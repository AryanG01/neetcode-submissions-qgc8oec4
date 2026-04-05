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

        mapping = {}
        
        def dfs(cur):
            if cur in mapping:
                return mapping[cur]
            
            mapping[cur] = Node(cur.val)

            for neighbor in cur.neighbors:
                mapping[cur].neighbors.append(dfs(neighbor))
            
            return mapping[cur]
        
        return dfs(node)
