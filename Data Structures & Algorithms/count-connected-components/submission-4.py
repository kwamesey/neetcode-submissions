class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    def find(self, node):
        res = node
        if res != self.par[res]:
            self.par[res] = self.find(self.par[res])
            return self.par[res]
        return res

    def union(self, n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return
        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for a,b in edges:
            if uf.find(a) == uf.find(b):
                continue
            uf.union(a,b)
            res -= 1

          
        return res








        