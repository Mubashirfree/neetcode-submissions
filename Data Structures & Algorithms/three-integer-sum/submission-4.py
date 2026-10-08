class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum=a+nums[l]+nums[r]
                if threeSum==0:
                    res.append([a,nums[l],nums[r]])
                    #[-2,-2,0,0,2,2] if we move only pointer it is enough
                    r-=1
                    while r>l and r<len(nums)-1 and nums[r]==nums[r+1]:
                        r-=1
                elif threeSum<0:
                    l+=1
                else:
                    r-=1
        return res
