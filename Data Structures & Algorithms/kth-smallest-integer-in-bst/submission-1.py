# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def addNode(node):
            if not node:
                return

            addNode(node.left)
            stack.append(node)
            addNode(node.right)
        
        addNode(root)
        
        return stack[k-1].val
           