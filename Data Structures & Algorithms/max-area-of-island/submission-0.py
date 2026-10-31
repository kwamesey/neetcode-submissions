class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                pos = (r,c)
                area = self.island_area(pos,visited,grid)
                if area > max_area:
                    max_area = area
        return max_area


    def island_area(self,pos,visited,grid):
        r,c = pos
        row_bounds = 0 <= r and r < len(grid)
        col_bounds = 0 <= c and c < len(grid[0])
        if row_bounds is False or col_bounds is False: return 0
        if grid[r][c] == 0: return 0
        if pos in visited: return 0
        visited.add(pos)

        area = 1
        delta_row = [-1,0,1,0]
        delta_col = [0,-1,0,1]
        for i in range(4):
            nr = r + delta_row[i]
            nc = c + delta_col[i]
            np = (nr,nc)
            area += self.island_area(np,visited,grid)
        return area

        

        