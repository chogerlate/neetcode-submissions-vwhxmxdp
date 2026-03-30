class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        l, r = 0, len(s)
        res = 0
        for idx, c in enumerate(s) :
            if c in seen :
                # res = max(res, idx-l-1)
                l = max(seen[c]+1, l)
            res = max(res, idx-l+1)
            seen[c] = idx
        return res