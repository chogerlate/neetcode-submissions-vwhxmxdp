class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for n in num_set:
            # Check if 'n' is the START of a sequence
            # If n-1 exists, 'n' is just a middle/end part of a sequence, so skip it
            if (n - 1) not in num_set:
                current_num = n
                current_streak = 1

                # While the next consecutive number exists, keep going
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak