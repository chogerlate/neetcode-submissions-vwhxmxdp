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
        # Edge case: If there is only one house, the "circle" is just that house.
        if len(nums) == 1: 
            return nums[0]
        
        def calculate_max_loot(house_range):
            two_houses_back = 0  # Max loot if we stopped 2 houses ago
            one_house_back = 0   # Max loot if we stopped 1 house ago
            
            for current_house_money in house_range:
                # OPTION 1: Rob current house (must add to loot from 2 houses ago)
                rob_current = current_house_money + two_houses_back
                
                # OPTION 2: Skip current house (keep the loot from 1 house ago)
                skip_current = one_house_back
                
                # The new 'best' is the winner of these two options
                current_max = max(rob_current, skip_current)
                
                # Shift our "memory" forward for the next house in the loop
                two_houses_back = one_house_back
                one_house_back = current_max
                
            return one_house_back

        # PART 1: Ignore the last house (Range: Start to Second-to-Last)
        loot_ignoring_last = calculate_max_loot(nums[:-1])
        
        # PART 2: Ignore the first house (Range: Second to the Very Last)
        loot_ignoring_first = calculate_max_loot(nums[1:])
        
        # The answer is the best of both worlds
        return max(loot_ignoring_last, loot_ignoring_first)