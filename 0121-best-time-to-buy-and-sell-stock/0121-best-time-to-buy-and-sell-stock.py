class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_prices = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_prices > p:
                buy_prices = p
            profit = max(profit, p - buy_prices)

        return profit
