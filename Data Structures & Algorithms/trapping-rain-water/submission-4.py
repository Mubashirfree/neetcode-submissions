class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftmax=0
        rightmax=0
        total=0
        while l<=r:
            if leftmax<=rightmax:
                amount=leftmax-height[l]
                if amount<0:
                    amount=0
                total+=amount
                leftmax=max(height[l],leftmax)
                l+=1
            else:
                amount=rightmax-height[r]
                if amount<0:
                    amount=0
                total+=amount                
                rightmax=max(height[r],rightmax)
                r-=1
        return total