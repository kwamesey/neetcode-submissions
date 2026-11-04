import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {node:[] for node in range(n)}
        for edge in edges:
            from_,to,weight = edge
            adj[from_].append((to,weight))
        res = {} # map a node(vertex) to the dist of the shortest path from 0
        
        dist = [float('inf')] * n
        dist[src] = 0
        min_heap = []
        heapq.heappush(min_heap,(dist[src],src))
        
        while min_heap:
            d,node = heapq.heappop(min_heap)
            if node in res:
                continue
            res[node] = d

            for neighbor in adj[node]:
                nei,w = neighbor
                if nei in res:
                    continue
                new_weight = d + w
                if dist[nei] > new_weight:
                    dist[nei] = new_weight
                    heapq.heappush(min_heap,(new_weight,nei))

        for node in range(n):
            if node not in res:
                res[node] = -1
        return res
