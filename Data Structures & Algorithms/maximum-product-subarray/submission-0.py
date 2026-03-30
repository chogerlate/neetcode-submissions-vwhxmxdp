class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize everything to the first number
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]

        # Start from the second number
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 1. If the current number is negative, it swaps the roles 
            # of max and min (big negative * negative = big positive)
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # 2. Choice: Start fresh at 'num' or multiply by previous results
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # 3. Update the best we've ever seen
            global_max = max(global_max, current_max)
            
        return global_max

