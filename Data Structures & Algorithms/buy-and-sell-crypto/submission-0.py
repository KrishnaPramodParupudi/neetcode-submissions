class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] 
        profit = 0
        for value in prices[1:] :
            if value < min_price :
                min_price = value
            if value-min_price > profit :
                profit = value-min_price
        return profit