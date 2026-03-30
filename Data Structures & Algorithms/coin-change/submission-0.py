class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        3 step framework:
        1. idenpendent states -> constraint -> remaining_value, idx_coin 
        2. recurrent relation -> min_coins = min(dp(idx_coin+1, remaining_value))
            - for each remaining_value we can find the most efficient ways to pick coin so this is overlap sub problem
        3. base case: if remaining_value < 0 -> return float(inf), remaining_value == 0 return 0
        """
        memo = {}
        def dp(remaining):
            # BASE CASES
            if remaining == 0: return 0  # It takes 0 coins to make 0 cents
            if remaining < 0: return float('inf') # Impossible path
            
            # CHECK MEMO
            if remaining in memo: return memo[remaining]

            # RECURRENCE
            # We want the MINIMUM of all possible coins we could pick
            best_for_this_amount = float('inf')
            
            for coin in coins:
                # We add 1 because we are using exactly ONE 'coin' right now
                result = dp(remaining - coin)
                
                if result != float('inf'):
                    best_for_this_amount = min(best_for_this_amount, result + 1)

            # STORE & RETURN
            memo[remaining] = best_for_this_amount
            return best_for_this_amount

        final_result = dp(amount)
        
        # If result is still infinity, it means no combination worked
        return final_result if final_result != float('inf') else -1