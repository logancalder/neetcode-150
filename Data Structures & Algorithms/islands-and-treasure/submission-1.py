class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            i, j = q.popleft()

            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                x2 = i + x
                y2 = j + y

                if(
                    x2 < 0 or x2 >= len(grid) or
                    y2 < 0 or y2 >= len(grid[0]) or
                    grid[x2][y2] != 2147483647
                ):
                    continue

                grid[x2][y2] = grid[i][j] + 1

                q.append((x2,y2))

