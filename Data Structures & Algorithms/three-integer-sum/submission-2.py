class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,num in enumerate(nums):
            l , r = i+1, len(nums) - 1
            while l < r:
                cur_sum = num + nums[l] + nums[r]
                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    trip = [num,nums[l],nums[r]]
                    if trip not in res:
                        res.append(trip)
                    l += 1
                    r -= 1
            
        
        return res



        