class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # track coords of fresh fruit

        # spread via BFS

        q = deque()
        rotted = set()
        good = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    rotted.add((i,j))
                if grid[i][j] == 1:
                    good += 1
        
        total_time = 0

        while q:
            x, y, time = q.popleft()

            if (
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0]) or
                grid[x][y] == 0
            ):
                continue
            
            if grid[x][y] == 1:
                grid[x][y] = 2
                good -= 1
                rotted.add((x,y))
                total_time = time + 1

            for nx, ny in ((1,0),(-1,0),(0,1),(0,-1)):
                if (x + nx, y + ny) not in rotted:
                    q.append((x + nx, y + ny, total_time))
        
        if good > 0:
            return -1
        else:
            return total_time
            # otherwise is a fruit
