class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0
        for i in range(len(prices)-1):
            if  prices[i]<prices[i+1]:
                total+=prices[i+1]-prices[i]
        return total
       