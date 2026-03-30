class Solution:
    def findMin(self, nums: List[int]) -> int:
        # task find the smallest value in the rotated sort array
        # this is not monotonic array 
        # binary search to find the pivot point 
        return min(nums)