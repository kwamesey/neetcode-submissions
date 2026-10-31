class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                pos = (r,c)
                if self.work(pos,grid,visited):
                    count += 1

        return count

    def work(self,pos,grid, visited):
        r,c = pos
        row_bounds = 0 <= r and r < len(grid)
        col_bounds = 0 <= c and c < len(grid[0])
        if row_bounds is False or col_bounds is False: return False
        if grid[r][c] == "0": return False
        if pos in visited: return False
        visited.add(pos)
        delta_row = [-1,0,1,0]
        delta_col = [0,-1,0,1]

        for i in range(len(delta_row)):
            new_row = delta_row[i] + r
            new_col = delta_col[i] + c
            new_pos = (new_row,new_col)
            self.work(new_pos,grid,visited)

        return True





        