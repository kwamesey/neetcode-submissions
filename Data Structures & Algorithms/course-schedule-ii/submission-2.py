
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pmap = {c:[] for c in range(numCourses)}

        indegree = [0] * numCourses

        for crs,pre in prerequisites:
            pmap[crs].append(pre)
            indegree[pre] += 1

        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        res = []
        finish = 0
        while len(q) > 0:
            crs = q.popleft()
            res.append(crs)
            finish += 1

            for pre in pmap[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        if finish != numCourses:
            return []
        return res[::-1]



