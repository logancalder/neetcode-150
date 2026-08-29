# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        stack, seen = [(root, 0)], {}

        while stack:
            node, lvl = stack.pop()
            if not node:
                continue
            
            if not lvl in seen:
                seen[lvl] = node.val
            
            lvl += 1

            stack.append((node.left, lvl))
            stack.append((node.right, lvl))

        result = []

        for lvl in seen:
            result.append(seen[lvl])
        
        return result

