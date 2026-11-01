from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visit = set()
        if not any(1 in sublist for sublist in grid): return 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        mins = 0
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                r,c = q.popleft()

                delta_row = [-1,0,1,0]
                delta_col = [0,-1,0,1]
                for i in range(4):
                    nr = r + delta_row[i]
                    nc = c + delta_col[i]
                    row_bounds = 0 <= nr and nr < len(grid)
                    col_bounds = 0 <= nc and nc < len(grid[0])
                    if row_bounds is False or col_bounds is False: continue
                    if grid[nr][nc] == 0: continue
                    if (nr,nc) in visit: continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        visit.add((nr,nc))
            mins += 1            
        if mins == 1:
            return -1
        if any(1 in sublist for sublist in grid):
            return -1
        return mins - 1

#   2  1  1
#   0  1  1
#   1  0  1                







