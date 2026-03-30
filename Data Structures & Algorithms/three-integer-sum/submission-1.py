class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        analyst:
        this is obvioustly 2 pointer with O(n^2) solution
        let start by fixed each target so we can now focus on the 
        A + B = -fixed_target
        
        """
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            hs = set()
            for j in range(i+1, n):
                target_pair = -nums[i] - nums[j] 
                if target_pair in hs :
                    res.add((nums[i], target_pair, nums[j]))
                hs.add(nums[j])

        return list(res)

