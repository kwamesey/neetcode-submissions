from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    pos = (r,c)
                    q.append(pos)
        length = 0
    
        while len(q) > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                if length < grid[r][c]:
                    grid[r][c] = length

                delta_row = [-1,0,1,0]
                delta_col = [0,-1,0,1]
                for i in range(4):
                    dr = delta_row[i]
                    dc = delta_col[i]
                    nr = r + dr
                    nc = c + dc
                    row_check = 0 <= nr and nr < len(grid)
                    col_check = 0 <= nc and nc < len(grid[0])
                    if row_check is False or col_check is False:
                        continue
                    if (nr,nc) in visited: continue
                    if grid[nr][nc] == -1: continue
                    if length +1 < grid[nr][nc]:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                    
            length += 1



        