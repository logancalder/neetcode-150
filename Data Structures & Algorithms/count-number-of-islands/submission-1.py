class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        def expand(coord):
            x, y = coord

            if (
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0]) or
                (x,y) in seen or grid[x][y] == '0'
            ):
                return False

            seen.add((x,y))

            expand((x + 1, y))
            expand((x - 1, y))
            expand((x, y + 1))
            expand((x, y - 1))
            
            return True

        num_islands = 0

        for i, row in enumerate(grid):
            for j, coord in enumerate(row):
                if expand((i,j)):
                    num_islands += 1
        
        return num_islands




