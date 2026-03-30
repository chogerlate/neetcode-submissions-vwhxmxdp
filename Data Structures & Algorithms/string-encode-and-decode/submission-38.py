class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: <length>#<string>
        """
        encoded = ""
        for word in strs:
            length = len(word)
            encoded = encoded + str(length) + "#" + word
        return encoded

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string back to a list of strings.
        """
        decoded = []
        print(s)
        total_lenght = len(s)
        i = j = 0
        while i < total_lenght :
            if s[i] == "#" and s[j:i].isdigit():
              word_length = int(s[j:i])
              word = "".join(s[i+1:i+word_length+1])      
              i = i+word_length+1
              j = i
              decoded.append(word)
              continue
            i += 1
        return decoded