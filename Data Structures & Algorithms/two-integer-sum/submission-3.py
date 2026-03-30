class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this is also hashtable prolem 
        # the hashtable store "value": "index" 
        mp = {}
        for idx, n in enumerate(nums) :
            target_sum_pair = target - n 
            if target_sum_pair in mp :
                return [mp[target_sum_pair], idx]
            else :
                mp[n] = idx

