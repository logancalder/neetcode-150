class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        profit = 0

        while r < len(prices):
            if l == r:
                r += 1
            elif prices[l] >= prices[r]:
                l += 1
            else:
                profit = max(prices[r] - prices[l], profit)
                r += 1
        
        return profit