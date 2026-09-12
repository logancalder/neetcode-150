class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        def expand(coord):
            nonlocal seen

            x, y = coord

            if int(grid[x][y]) == 0 or (x,y) in seen:
                return 0

            seen.add((x,y))

            total = 1

            if x + 1 < len(grid):
                total += expand((x + 1, y))
            if x - 1 >= 0:
                total += expand((x - 1, y))
            
            if y + 1 < len(grid[x]):
                total += expand((x, y + 1))
            if y - 1 >= 0:
                total += expand((x, y - 1))
            
            return total

        num_islands = 0

        for i, row in enumerate(grid):
            for j, coord in enumerate(row):
                if expand((i,j)) > 0:
                    num_islands += 1
        
        return num_islands




