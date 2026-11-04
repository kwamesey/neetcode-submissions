import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {node:[] for node in range(1,n+1)}

        for src,tar,ti in times:
            adj[src].append((tar,ti))
        
        visit = set()
        time = [float('inf')] * (n+1)
        time[k] = 0

        min_heap = []
        heapq.heappush(min_heap, (time[k],k))

        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)

            for nei,time2 in adj[node]:
                if nei in visit:
                    continue
                new_time = t+time2
                if new_time < time[nei]:
                    time[nei] = new_time
                    heapq.heappush(min_heap, (new_time,nei))
        
        time.pop(0)

        if len(visit) != n:
            return -1

        
        return max(time)
            

        
        
        