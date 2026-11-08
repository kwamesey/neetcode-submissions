class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]

        size = [1] * n

        def find(node):
            res = node

            if res != par[res]:
                par[res] = find(par[par[res]])
                return find(par[res])
            
            return res

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                return 0
            
            if size[p2] > size[p1]:
                par[p1] = p2
                size[p2] += size[p1]
            else:
                par[p2] = p1
                size[p1] += size[p2]
            return 1

        for n1,n2 in edges:
            n -= union(n1,n2)

        return n
            
        