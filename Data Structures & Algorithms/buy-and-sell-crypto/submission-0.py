class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        fast, slow = 0, 0 

        while fast < len(prices):
            cur_profit = prices[fast] - prices[slow]
            max_profit = max(max_profit, cur_profit)
            if prices[fast] < prices[slow]:
                slow = fast
            fast += 1            
        return max_profit