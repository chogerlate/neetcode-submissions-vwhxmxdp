class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this is also character frequency comparision problem
        # we will use dict to store the list of words for each pattern
        # "pattern" : ["word1", "word2"]
        # well for optimization let just apply Counter dict for each element 
        # then group them and create the result by gathering index
        mp = defaultdict(list)
        for word in strs:
            vector = [0] * 26
            for char in word:
                vector[ord(char) - ord('a')] += 1
            key = tuple(vector)
            mp[key].append(word)
        
        return [ value for key,value in mp.items()]
            


