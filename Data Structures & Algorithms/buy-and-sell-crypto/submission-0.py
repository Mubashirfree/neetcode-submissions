class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mastProfit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                currentProfit=prices[j]-prices[i]
                mastProfit=max(currentProfit,mastProfit)
        return mastProfit