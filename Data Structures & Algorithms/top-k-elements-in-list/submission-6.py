class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # int : occur

        for num in nums:
            count[num] += 1
        if len(count) == 1:
            return [nums[0]]

        
        res = set()
        i=0
        while i < k:
            test=0
            fin =() #int,occur
            for n in count:
                val = count[n]
                if val > test :
                    test = val
                    fin = (n,val)
            
            no,val = fin
            count[no] = 0
            res.add(no)
            i += 1
            
        return list(res)


        