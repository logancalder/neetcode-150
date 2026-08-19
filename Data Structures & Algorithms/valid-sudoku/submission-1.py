class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r, row in enumerate(board):
            seen = set()
            for c, num in enumerate(row):
                if num == ".":
                    continue
                # rows logic
                if num not in seen:
                    seen.add(num)
                else:
                    return False

                # cols logic
                if num not in cols[c]:
                    cols[c].add(num)
                else:
                    return False

                # box logic
                # row index, col index both int div by 3
                boxcoords = (r // 3, c // 3) 
                if num not in boxes[boxcoords]:
                    boxes[boxcoords].add(num)
                else:
                    return False
        return True
                
                