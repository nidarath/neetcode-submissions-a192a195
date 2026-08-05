class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       #two pointers 
       #profit = sell - buy
        left, right = 0, 1 #where left is buy, right is sell
        maxP = 0
        while right < len(prices): # while the week isn't over
            if prices[left] < prices[right]: # if the buy is less than the right
                profit = prices[right] - prices[left] # sell - buy
                maxP = max(maxP, profit) # check & store if greater profit
            else:
                left = right # move pointers to same place
            right += 1 # move the right ahead
        return maxP #return the max profit