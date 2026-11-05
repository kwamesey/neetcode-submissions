from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for char in s:
            map_s[char] += 1

        for char in t:
            map_t[char] += 1

        return map_s == map_t
            


