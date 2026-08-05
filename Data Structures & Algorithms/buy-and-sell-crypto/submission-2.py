class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dynamic programming method
        #keep track of max profit and minimum buy 
        maxP = 0 
        minBuy = prices[0] #start at beginning

        #one pass so we make sure the buy is before the sell.
        for sell in prices:
            maxP = max(maxP, sell - minBuy) #check if sell can be higher as we go
            minBuy = min(minBuy, sell) #if there a lower amount
        return maxP