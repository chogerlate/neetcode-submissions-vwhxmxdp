class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r,res = 0, len(nums)-1, nums[0]
        
        while l <= r :
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = l + (r-l)//2            
            res = min(res, nums[m])
            if nums[m] < nums[l]:
                r = m-1
            else :
                l = m+1
        
        return res 