class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # seperator: '{length}#'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 

        while i < len(s):
            j = i 
            # loop to '#' position
            while s[j] != '#': 
                j += 1 
            length = int(s[i:j]) # get word length  
            i = j+1 # set to position after '#'
            j = i + length # set to position of next seperator
            res.append(s[i:j]) # extract text
            i = j # set th start character to next seperator
        return res