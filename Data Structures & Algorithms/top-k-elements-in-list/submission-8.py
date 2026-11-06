class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n,times in count.items():
            freq[times].append(n)

        res = []
        

        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res

            
        