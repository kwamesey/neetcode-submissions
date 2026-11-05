class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                return True
            nums_map[num] = num
        return False
        