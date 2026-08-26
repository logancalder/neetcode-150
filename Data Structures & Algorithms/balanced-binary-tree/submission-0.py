# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def dfs(root):
            nonlocal balanced

            if not root: return 0

            l, r = dfs(root.left), dfs(root.right)

            if abs(l - r) > 1:
                balanced = False
            
            return max(l, r) + 1

        dfs(root)
        
        return balanced