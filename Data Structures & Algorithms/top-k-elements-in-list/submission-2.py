class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for num in nums:
            hash[num]=hash.get(num,0)+1
        freq=[[]for i in range(len(nums)+1)]
        for n,v in hash.items():
            freq[v].append(n)
        #print(freq)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
      