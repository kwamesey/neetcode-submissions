class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        visit = set()
        good_region = set()

        def dfs(r,c,visit):
            row_check = 0 <= r and r < rows
            col_check = 0 <= c and c < cols
            if row_check is False or col_check is False:
                return
            if (r,c) in visit:
                return
            if board[r][c] == "X":
                return
            visit.add((r,c))
            
            
            delta_row = [-1,0,1,0] #up down
            delta_col = [0,-1,0,1] #left right
            for i in range(4):
                new_row = r + delta_row[i]
                new_col = c + delta_col[i]
                dfs(new_row,new_col,visit)
            good_region.add((r,c))


        #start from row edges
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c,visit)
            if board[rows-1][c] == "O":
                dfs(rows-1,c,visit)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0,visit)
            if board[r][cols-1] == "O":
                dfs(r,cols-1,visit)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in good_region:
                    continue
                board[r][c] = "X"

        


