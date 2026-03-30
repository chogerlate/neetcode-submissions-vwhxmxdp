class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for s in strs:
            # Create a count array for a-z (26 letters)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Convert count array to tuple to make it hashable
            key = tuple(count)
            
            if key in anagram_groups:
                anagram_groups[key].append(s)
            else:
                anagram_groups[key] = [s]
        
        return list(anagram_groups.values())

