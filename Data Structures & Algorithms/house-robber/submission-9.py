class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        is this dp:
        1. state(t+1) come from state(t) [check]
        2. state(t+1) use the best result from state(t) [check]
        3-step framework:
        1. idenpendent state -> sequnece style: n-th house
        2. recurrent relation:
            n equal to the lenght of nums 
            the best answer should be in this formula nums[n] + dp(n-2)
        3. smallest base case
            n == 1 -> nums[0]
        """
        if len(nums) == 1: return nums[0]

        def solve_range(houses):
            memo = {}
            def dp(i):
                if i < 0: return 0
                if i == 0: return houses[0]
                if i in memo: return memo[i]
                
                # Logic: Max(Rob, Skip)
                memo[i] = max(houses[i] + dp(i - 2), dp(i - 1))
                return memo[i]
            
            return dp(len(houses) - 1)

        # Pattern: Max of (Linear solve without last) vs (Linear solve without first)
        return solve_range(nums)