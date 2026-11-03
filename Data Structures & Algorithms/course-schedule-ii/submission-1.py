class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            pre_map[crs].append(pre)

        visit=set()
        res=[]
        def dfs(crs):
            if crs in visit:
                return False
            if pre_map[crs] == [] and crs not in res:
                res.append(crs)
                return

            visit.add(crs)
            for course in pre_map[crs]:
                if dfs(course) is False: return False

            visit.remove(crs)
            pre_map[crs] = []
            if crs not in res:
                res.append(crs)
            return
            
            
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res




        