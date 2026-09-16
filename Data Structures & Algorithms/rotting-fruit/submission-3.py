class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # track coords of fresh fruit

        # spread via BFS

        q = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    fresh += 1
        
        total_time = 0

        while q:
            x, y, time = q.popleft()

            total_time = max(total_time, time)

            if (
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0]) or
                grid[x][y] == 0
            ):
                continue
            
            for ax, ay in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = ax + x, ay + y

                if (
                    0 <= nx < len(grid) and
                    0 <= ny < len(grid[0]) and
                    grid[nx][ny] == 1
                ):
                    grid[nx][ny] = 2
                    q.append((nx, ny, time + 1))
                    fresh -= 1
        
        return total_time if not fresh else -1
