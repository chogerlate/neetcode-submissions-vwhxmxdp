class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = []
        total = -1
        while True :
            total = sum([ int(c)**2 for c in s])
            if total == 1 :
                return True
            if total in seen :
                break 
            seen.append(total)
            s = str(total)
        return False