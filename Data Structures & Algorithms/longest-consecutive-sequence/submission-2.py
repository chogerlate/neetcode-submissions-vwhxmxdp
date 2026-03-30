class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num-1 not in num_set:
                streak = 1
                cur = num
                while cur+1 in num_set:
                    streak += 1
                    cur = cur + 1
                longest_streak = max(longest_streak, streak)

        return     longest_streak                

