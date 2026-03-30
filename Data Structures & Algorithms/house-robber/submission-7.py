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
        if len(nums) == 1: 
            return nums[0]

        def calculate_maximum_profit(nums: list[int]) -> int:
            one_house_prior, two_house_prior = 0, 0 
            maximum_profit = 0

            for amount in nums :
                current_house_profit = amount + two_house_prior 
                keep_the_one_house_prior = one_house_prior
                maximum_profit = max(current_house_profit, keep_the_one_house_prior)
                one_house_prior, two_house_prior = maximum_profit, keep_the_one_house_prior

            return maximum_profit
        
        return calculate_maximum_profit(nums)