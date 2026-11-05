from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROW = len(image)
        COL = len(image[0])
        orig_c = image[sr][sc]

        
        q = deque([(sr,sc)])
        visit = set()

        while q:
            r,c = q.popleft()
            if (r,c) in visit:
                continue
            visit.add((r,c))
            image[r][c] = color

            delta_row = [-1,0,1,0]
            delta_col = [0,-1,0,1]

            for i in range(4):
                new_row = r + delta_row[i]
                new_col = c + delta_col[i]

                row_check = 0 <= new_row and new_row < ROW
                col_check = 0 <= new_col and new_col < COL

                if not row_check or not col_check:
                    continue
                if image[new_row][new_col] != orig_c:
                    continue
                q.append((new_row,new_col))

        return image


        