class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        stack = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and ((i,j) not in seen):
                    current_nodes = []
                    stack.append((i,j))
                    is_enclosed = True

                    while stack:
                        x, y = stack.pop()

                        if (
                            x < 0 or x >= len(board) or
                            y < 0 or y >= len(board[0])
                        ):
                            is_enclosed = False
                            continue
                        
                        if board[x][y] == 'X':
                            continue
                        
                        seen.add((x,y))
                        current_nodes.append((x,y))

                        for x2, y2 in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx = x + x2
                            ny = y + y2

                            if (nx,ny) not in seen:
                                stack.append((nx,ny))

                    if is_enclosed:
                        for x,y in current_nodes:
                            board[x][y] = 'X'

        
            
