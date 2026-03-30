class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # same shit as pre-post sum just different operation
        # we have 2 memory for forward products and backward products 
        # [ 1, 2 ,4 ,6] -> [1,1,2,8] forward
        # backward -> [48,24,6,1]
        forward = [1] * len(nums) 
        for i in range(1, len(nums)):
            forward[i]  = nums[i-1] * forward[i-1]

        n = len(nums)
        backward = [1] * n
        for j in range(n-2, -1, -1):
            backward[j] = nums[j+1] * backward[j+1]

        print(forward, backward)
        return [ n * m for n, m in zip(forward, backward)]

