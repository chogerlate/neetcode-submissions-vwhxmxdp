class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: <length>#<string>
        """
        res = ""
        for s in strs:
            # We prefix the string with its length and a delimiter
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string back to a list of strings.
        """
        res = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter '#' to know where the length ends
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract the length
            length = int(s[i:j])
            
            # 3. Use that length to jump exactly to the end of the original string
            # The string starts at j+1 and ends at j+1+length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. Move our pointer 'i' to the start of the next encoded block
            i = end
            
        return res