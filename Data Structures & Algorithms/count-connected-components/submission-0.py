class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()

        count = 0 
        def dfs(node):
            if node in visit:
                return
            visit.add(node)

            for nei in adj[node]:
                dfs(nei)
            return True
            
        
        for node in range(n):
            if dfs(node) is True:
                count += 1
            if len(visit) == n:
                return count
            
            


        