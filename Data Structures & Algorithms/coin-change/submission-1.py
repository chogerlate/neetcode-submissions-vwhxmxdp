class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        3 step framework:
        1. idenpendent states -> constraint -> remaining_value 
        2. recurrent relation -> min_coins = min(dp(idx_coin+1, remaining_value))
            - for each remaining_value we can find the most efficient ways to pick coin so this is overlap sub problem
        3. base case: if remaining_value < 0 -> return float(inf), remaining_value == 0 return 0
        """
        memo = {}
        def dp(remaining):
            # BASE CASES
            if remaining == 0: return 0  # It takes 0 coins to make 0 cents
            if remaining < 0: return float('inf') # Impossible to find the answer

            # check the memory 
            if remaining in memo : return memo[remaining]

            # main recursive relationship
            min_coin = float("inf")
            for coin in coins :
                cur_min_coin = 1 + dp(remaining - coin)
                min_coin = min(cur_min_coin, min_coin)
            memo[remaining] = min_coin
            return min_coin

        final_result = dp(amount)
            
        return final_result if final_result != float('inf') else -1