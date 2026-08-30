# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validChild(node, parent, upper, lower):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False
            
            return validChild(node.left, node, node.val, lower) and validChild(node.right, node, upper, node.val)
        
        return validChild(root.left, root, root.val, -1000000000) and validChild(root.right, root, 1000000000, root.val)
        