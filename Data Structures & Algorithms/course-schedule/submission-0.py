class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #for every courses to start, we want to map it to an empty prereq list
        pre_map = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        #visitset stores the courses we touch in the DFS path
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if pre_map[crs] == []:
                return True

            visit.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre) is False: return False

            visit.remove(crs)
            pre_map[crs] = []
            return True
        
        for crs in range(numCourses):
            test = dfs(crs)
            if test is False: return False
        return True
            

        