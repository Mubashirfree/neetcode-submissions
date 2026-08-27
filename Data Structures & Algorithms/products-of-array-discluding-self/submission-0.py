class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we are going to do it using prefix and  postfix
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        output=[0]*len(nums)
        pre=1
        post=1
        for i in range(len(nums)):
            prefix[i]=pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=post
            post*=nums[i]
        for i in range(len(nums)):
            output[i]=prefix[i]*postfix[i]
        return output    