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
            w1,n1 = heapq.heappop(min_heap)
            if n1 in res:
                continue
            res[n1] = w1

            for neighbor in adj[n1]:
                n2,w2 = neighbor
                if n2 in res:
                    continue
                new_weight = w1 + w2
                if dist[n2] > new_weight:
                    dist[n2] = new_weight
                    heapq.heappush(min_heap,(new_weight,n2))

        for node in range(n):
            if node not in res:
                res[node] = -1
        return res
