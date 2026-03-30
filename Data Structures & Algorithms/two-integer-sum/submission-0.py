class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intuitive: if the target - element and if exist in
        hm = {} # we use num as key and pos as value
        for idx, num in enumerate(nums):
            search_num = (target - num)
            if search_num in hm :
                return [hm[search_num], idx]
            else :
                hm[num] = idx
        return -1 

            