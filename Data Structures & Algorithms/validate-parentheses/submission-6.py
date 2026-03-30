class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mp_pair = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        for c in s :
            if c in "{([":
                stack.append(mp_pair[c])
            elif c in ")]}" :
                if not stack or stack.pop() != c :
                    return False
            else :
                return False
        return True if not stack else False