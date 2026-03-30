class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # this question is obvisouly hashmap 
        seen = set()
        for n in nums :
            if n not in seen :
                seen.add(n)
            else :
                return True
        return False
            