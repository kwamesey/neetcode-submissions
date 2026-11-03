class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def work(r,c,visit,prevHeight):
            row_check = 0 <= r and r < rows
            col_check = 0 <= c and c < cols
            if (r,c) in visit or row_check is False or col_check is False or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            delta_row = [-1,0,1,0]
            delta_col = [0,-1,0,1]

            for i in range(4):
                new_row = r + delta_row[i]
                new_col = c + delta_col[i]
                work(new_row,new_col,visit,heights[r][c])

        for c in range(cols):
            work(0, c, pac, heights[0][c])
            work(rows - 1,c,atl,heights[rows - 1][c])
        for r in range(rows):
            work(r, 0, pac,heights[r][0])
            work(r,cols - 1,atl,heights[r][cols-1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        