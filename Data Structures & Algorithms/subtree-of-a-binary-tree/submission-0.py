# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return sameTree(t1.left,t2.left) and sameTree(t1.right,t2.right)
        
        def dfsSearch(root):
            if not root:
                return False

            if not sameTree(root, subRoot):
                return dfsSearch(root.left) or dfsSearch(root.right)
            return True
        
        return dfsSearch(root)