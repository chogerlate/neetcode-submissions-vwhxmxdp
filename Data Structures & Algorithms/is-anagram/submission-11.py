class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter dict
        from collections import Counter
        if (Counter(s).items()) == (Counter(t).items()):
            return True
        else :
            return False
