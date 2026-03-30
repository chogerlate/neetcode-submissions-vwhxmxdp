class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # intuitive An anagram is a string that contains the exact same characters as another string, 
        # but the order of the characters can be different.
        if len(s) != len(t) :
            # these 2 words do not have exact numbers of characters as anagram describe 
            return False
        # proceed with the anagram checking process
        hm = {} 
        for idx in range(len(s)):
            if s[idx] in hm :
                hm[s[idx]] += 1 
            else :
                hm[s[idx]] = 1
            if t[idx] in hm :
                hm[t[idx]] -= 1 
            else :
                hm[t[idx]] = -1
        
        for num in hm.values():
            if num :
                return False
        return True

            

