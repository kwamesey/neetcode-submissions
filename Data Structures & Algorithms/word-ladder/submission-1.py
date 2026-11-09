from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "-" + word[i+1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "-" + word[i+1:]
                    for w in adj[pattern]:
                        if w in visit:
                            continue
                        q.append(w)
                        visit.add(w)
            res += 1

        return 0
        


            




        