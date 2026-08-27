class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        hash={}
        for i in range(len(nums)):
            hash[nums[i]]=i
        maxcount=1
        count=1
        i=0
        for i in range(len(nums)):
            prev=nums[i]-1
            if prev in hash:
                continue
            next=nums[i]+1
            while next in hash:
                count+=1
                next+=1
            maxcount=max(maxcount,count)
            count=1
            
        return maxcount
            
