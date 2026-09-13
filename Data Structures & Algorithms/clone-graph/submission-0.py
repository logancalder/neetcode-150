"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def create(node):
            if not node:
                return None
            
            dummy = Node(node.val)

            seen[node] = dummy

            this_neighbors = []

            for neighbor in node.neighbors:
                if neighbor in seen:
                    this_neighbors.append(seen[neighbor])
                else:
                    this_neighbors.append(create(neighbor))
                
            dummy.neighbors = this_neighbors
            
            return dummy
        
        return create(node)

