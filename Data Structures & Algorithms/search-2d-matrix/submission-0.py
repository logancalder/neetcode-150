class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else: # its here
                l, r = 0, len(matrix[m]) - 1
                current_matrix = matrix[m]
                while l <= r:
                    m = (l + r) // 2
                    if target == current_matrix[m]:
                        return True
                    elif target < current_matrix[m]:
                        r = m - 1
                    else:
                        l = m + 1
        return False
                    
                    
        