class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l , r = 0 , len(heights) - 1
        while l < r:
            width = abs(r - l)
            height = min(heights[r],heights[l])
            a = width * height
            res = max(res,a)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res



        