class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hm = defaultdict(list)

        for s in strs:
            v = [0]*26
            for i in s:
                v[ord(i) - ord('a')] += 1
            
            hm[tuple(v)].append(s)
        
        return list(hm.values())
    