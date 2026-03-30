class Solution:
    def findMin(self, nums: List[int]) -> int:
        # task find the smallest value in the rotated sort array
        # this is not monotonic array 
        # binary search to find the pivot point 
        left, right = 0, len(nums)-1
        res = nums[left]
        while left <= right :
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[right] :
                right = mid - 1
            else :
                left = mid + 1
        return res