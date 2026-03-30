class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem analysis 
        deal with subarray and substring [x] -> sliding window
        using 2 pointers to keep expand and shrink the windows
        Time Complexity -> O(n)
        Space -> O(1)
        """
        # edge case
        if not s: return 0
        p1, p2 = 0,0
        max_length = 0 # to keep track the global max_lenght
        # using hashset would be fine
        hashset = set()
        while p2 < len(s):
            while s[p2] in hashset:
                hashset.remove(s[p1])
                p1 += 1
            hashset.add(s[p2])
            p2 += 1
            max_length = max(max_length, p2-p1)
        return max_length
            

