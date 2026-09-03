class Solution:
    def trap(self, height: List[int]) -> int:
        #with extra memory
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        minbar=[0]*len(height)
        left=0
        right=0
        for i in range(len(height)):
            leftmax[i]=left
            left=max(left,height[i])
        for i in range(len(height)-1,-1,-1):
            rightmax[i]=right
            right=max(right,height[i])
        for i in range(len(height)):
            minbar[i]=min(leftmax[i],rightmax[i])
        total=0
        for i in range(len(height)):
            amount=minbar[i]-height[i]
            if amount<0:
                amount=0
            total+=amount
        return total
