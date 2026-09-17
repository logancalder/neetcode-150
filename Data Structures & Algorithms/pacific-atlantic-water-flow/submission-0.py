class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()

        def dfs(x, y, seen):
            seen.add((x,y))

            for x2, y2 in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x2 + x, y2 + y

                if (
                    0 <= nx < len(heights) and
                    0 <= ny < len(heights[0]) and
                    ((nx, ny)) not in seen and
                    heights[nx][ny] >= heights[x][y]
                ):
                    dfs(nx, ny, seen)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, pacific)
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, atlantic)

        return [[x,y] for x, y in pacific & atlantic]

        