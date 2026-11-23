class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le, ri = 0, len(numbers) -1

        while le < ri:
            test = numbers[le] + numbers[ri]
            if test > target:
                ri -= 1
            if test < target:
                le += 1
            if test == target:
                return [le+1,ri+1]
        
        return []


        