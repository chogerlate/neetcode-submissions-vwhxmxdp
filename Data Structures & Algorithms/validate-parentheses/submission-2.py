class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mp_pair = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        for c in s :
            if c in ")}]" :  
                if stack :
                    current_open = stack.pop()
                    if mp_pair[c] != current_open :
                        return False    
                else :
                    return False

            if c in "([{" :
                stack.append(c)
        
        return True if not stack else False