# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexes = {}

        for i, num in enumerate(inorder):
            indexes[num] = i

        preIdx = 0

        def dfs(left, right):
            nonlocal preIdx

            if left > right:
                return None

            root_val = preorder[preIdx]

            root = TreeNode(root_val)
            mid = indexes[root_val]

            preIdx += 1

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(inorder) - 1)