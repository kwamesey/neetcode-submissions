#return the min amount of time to get to the bottom right corner

#we can only go into a cell if the water level is less than or equal to 
#the time

#we can use a min_heap.
#start at (0,0) & we grab the water level (0,0,0) level,r,c
#and we push into our min heap, we check neighbors, we check bounds checks
#and once we visit a cell, we know thats the minimum time to get there
#and we check at the top of our q to see if the r,c is the last cell
#then we return the max grid[r][c] in our visit set?
# no actually we will be passing the max level as we find the bottom right cell
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        start = (grid[0][0],0,0)
        min_heap = []
        heapq.heappush(min_heap, start)
        q = deque()


        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
        time = 0
        while min_heap or q:
            time += 1
            if min_heap:
                level,r,c = heapq.heappop(min_heap)
                if (r,c) == (ROWS - 1, COLS - 1):
                    return level
                if (r,c) in visit:
                    continue
                visit.add((r,c))
                for dr,dc in neighbors:
                    new_row = r + dr
                    new_col = c + dc
                    row_check = 0 <= new_row and new_row < ROWS
                    col_check = 0 <= new_col and new_col < COLS
                    if row_check is False or col_check is False:
                        continue
                    if (new_row,new_col) in visit:
                        continue
                    step = grid[new_row][new_col]
                    new_level = max(step,level)
                    if new_level > time:
                        q.append((new_level,new_row,new_col))
                    if new_level <= time:
                        heapq.heappush(min_heap,(new_level,new_row,new_col))

            if q and q[0][0] <= time:
                level,r,c = q.popleft()
                heapq.heappush(min_heap, (level,r,c))
            




                
                


            
