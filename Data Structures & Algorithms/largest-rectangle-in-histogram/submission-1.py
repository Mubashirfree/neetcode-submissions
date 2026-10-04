class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=float('-inf')
        for i in range(len(heights)):
            start_index=i
            while stack and stack[-1][1]>heights[i]:
                maxArea=max(maxArea,(i-stack[-1][0])*stack[-1][1])
                start_index=stack[-1][0]
                stack.pop()
            stack.append([start_index,heights[i]])
        for i,n in stack:
            maxArea=max(maxArea,(len(heights)-i)*n)
        return maxArea 
