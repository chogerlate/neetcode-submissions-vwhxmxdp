class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # intuitive: use hashmap to store pass by elements 
        hm = {}
        for num in nums :
            if num in hm: # if the element already inside hashmap -> this imply that we found duplicate element
                return True
            hm[num] = 1 
        return False 