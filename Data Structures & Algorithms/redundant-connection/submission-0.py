class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    def find(self,node):
        res = node
        if res != self.par[res]:
            self.par[res] = self.find(self.par[res])
            return self.par[res]
        return res

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        
        if p1 == p2:
            return 0
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        return 1 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            n1,n2 = edge
            if uf.union(n1,n2) == 0:
                return edge

            

        
        