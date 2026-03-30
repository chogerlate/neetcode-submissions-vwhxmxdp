class Solution:
    def findMin(self, nums: List[int]) -> int:
        # task find the smallest value in the rotated sort array
        # this is not monotonic array 
        # binary search to find the pivot point 
        left, right = 0, len(nums)-1
        res = nums[left]
        while left < right :
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else :
                left = mid + 1
        return nums[left]
