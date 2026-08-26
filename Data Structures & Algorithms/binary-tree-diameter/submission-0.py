# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            longest = 0
            
            def traverse(root):
                nonlocal longest

                if not root:
                    return 0

                l, r = traverse(root.left), traverse(root.right)

                longest = max(longest, l + r)

                return max(l, r) + 1
        
            traverse(root)

            return longest

            
            # for every node, check L of left and R
                # if a node down line has L and R, return longest fork
            # store the longest value
