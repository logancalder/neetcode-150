class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def expand(coord):
            x, y = coord

            if (
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0]) or
                (x,y) in seen or grid[x][y] == 0
            ):
                return 0

            seen.add((x,y))

            total = 1

            total += expand((x + 1, y))
            total += expand((x - 1, y))
            total += expand((x, y + 1))
            total += expand((x, y - 1))

            
            return total

        max_area = 0

        for i, row in enumerate(grid):
            for j, coord in enumerate(row):
                max_area = max(max_area, expand((i,j)))
        
        return max_area

