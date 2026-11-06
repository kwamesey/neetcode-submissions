class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i, num in enumerate(nums):
            h_map[num] = i
        res = []
        for i, num in enumerate(nums):
            comp = target - num
            if comp in h_map and i != h_map[comp]:
                res = [i,h_map[comp]]

        a,b = res
        if a > b:
            return [b,a]
        return [a,b]
        

        