import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            if stone1 == stone2:
                continue
            if stone1 > stone2:
                res_stone = stone1 - stone2
            #if stone2 > stone1:
            #    res_stone = stone2 - stone1
            res_stone = -res_stone
            heapq.heappush(max_heap,res_stone)
        
        if not len(max_heap):
            return 0
        
        return -max_heap[0]
        
