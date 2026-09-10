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
        head_track = head
        top = node = Node(0)
        mapping = {}

        while head_track:
            dummy = Node(head_track.val)
            
            node.next = dummy
            node = node.next

            mapping[head_track] = node

            head_track = head_track.next
        
        top = top.next
        head_track = head

        while head_track:
            if head_track.random:
                mapping[head_track].random = mapping[head_track.random]
            head_track = head_track.next
        
        return top
        

