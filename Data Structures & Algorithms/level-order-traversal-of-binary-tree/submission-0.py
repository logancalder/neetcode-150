# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def extend_list(self, lvl, arr):
        if len(arr) <= lvl:
            arr.append([])

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        result = [[root.val]]

        while q:
            node, lvl = q.popleft()
            lvl += 1

            if node.left:
                self.extend_list(lvl, result)
                result[lvl].append(node.left.val)
                q.append((node.left, lvl))

            if node.right:
                self.extend_list(lvl, result)
                result[lvl].append(node.right.val)
                q.append((node.right, lvl))
        
        return result
            
    
