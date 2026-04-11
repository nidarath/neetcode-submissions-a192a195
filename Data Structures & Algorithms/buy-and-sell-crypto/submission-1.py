class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = 0, 0
        sell = 1 # sell is always after
        while sell < len(prices): 
            profit = max(profit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
            sell +=1
        return profit