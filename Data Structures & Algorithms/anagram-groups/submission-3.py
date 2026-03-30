class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this is also character frequency comparision problem
        # we will use dict to store the list of words for each pattern
        # "pattern" : ["word1", "word2"]
        # well for optimization let just apply Counter dict for each element 
        # then group them and create the result by gathering index
        mp = {}
        for idx, s in enumerate(strs):
            # let encode the word
            vector = [0] * 26
            # encode 
            for c in s :
                vector[ord(c)-ord('a')] += 1
            
            encoded_vector = tuple(vector) 
            if encoded_vector not in mp :
                mp[encoded_vector] = [s]
            else :
                mp[encoded_vector].append(s)
        
        return [ group for group in mp.values()]

            


