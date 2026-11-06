class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in h_map:
                return [h_map[comp],i]
            h_map[num] = i

        