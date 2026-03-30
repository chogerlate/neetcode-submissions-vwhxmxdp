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

        memo = {}
        def dp(house_nth: int) -> int:
            if house_nth == 0 : return nums[0]
            if house_nth < 0 : return 0
            if house_nth in memo : return memo[house_nth] 
            best_previous_nth = [ dp(next_idx) for next_idx in range(house_nth-2, -1, -1)] 
            best_house_nth = nums[house_nth] + (max(best_previous_nth) if best_previous_nth else 0 )
            memo[house_nth] = best_house_nth
            return best_house_nth 
        n = len(nums)
        best_rob = max(dp(n-1), dp(n-2))
        return best_rob