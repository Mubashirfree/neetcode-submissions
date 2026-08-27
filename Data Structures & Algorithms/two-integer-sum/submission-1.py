class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            val=target-nums[i]
            for k in hash.keys():
                if k==val:
                    return sorted([i,hash[k]])
            hash[nums[i]]=i
        