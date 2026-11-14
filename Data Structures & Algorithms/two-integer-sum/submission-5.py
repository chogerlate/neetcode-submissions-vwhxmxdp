class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort and look up hm 
        hs = {nums[0]:0}
        n = len(nums)
        for i in range(1, n):
            if target-nums[i] in hs:
                return [hs[target-nums[i]],i]
            else:
                hs[nums[i]] = i
            

            