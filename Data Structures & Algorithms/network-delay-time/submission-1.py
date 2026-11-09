import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range (n+1)}
      

        for src,dst,ti in times:
            adj[src].append((dst,ti))

        time = [float('inf')] * (n+1)
        time[k] = 0
        min_heap = []
        visit = set()


        heapq.heappush(min_heap,(time[k],k))
        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            for nei,ti in adj[node]:
                if nei in visit:
                    continue
                new_time = ti +t
                if new_time < time[nei]:
                    time[nei] = new_time
                    heapq.heappush(min_heap, (new_time,nei))

        time.pop(0)
    
        return max(time) if float('inf') not in time else -1




        
        
