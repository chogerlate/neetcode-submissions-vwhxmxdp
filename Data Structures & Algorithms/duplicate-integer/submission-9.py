class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # this question is obvisouly hashmap 
        seen = set()
        for n in nums :
            if n in seen: return True
            else: seen.add(n)
        return False