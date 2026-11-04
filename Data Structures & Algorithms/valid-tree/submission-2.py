class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(n)}

        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        visit = set()

        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)

            for neighbors in adjlist[node]:
                if neighbors == parent:
                    continue
                if neighbors in visit:
                    return False
                if dfs(neighbors,node) is False:
                    return False
            
            return True

        if dfs(0,-1) is False: return False
        return len(visit) == n
        


        