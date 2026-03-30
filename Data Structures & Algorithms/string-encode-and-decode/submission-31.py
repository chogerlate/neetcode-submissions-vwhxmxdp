class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w))+"#"+w
        return res  
    def decode(self, s: str) -> List[str]:
        res, l  = [], 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            wl = int(s[l:r])
            r = r+1
            res.append(s[r:r+wl])
            l = r+wl
        return res