# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        total = 0

        def isGood(node, largest):
            total = 0
            
            if node.val >= largest:
                total += 1
            
            largest = max(largest, node.val)
            
            if node.left:
                total += isGood(node.left, largest)
            if node.right:
                total += isGood(node.right, largest)
            
            return total
        
        return isGood(root, -101)