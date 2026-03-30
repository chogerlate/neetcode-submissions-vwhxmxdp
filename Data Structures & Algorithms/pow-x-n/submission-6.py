class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = x
        
        if n == 0 :
            return 1
        elif n > 0 :
            for _ in range(n-1):
                result *= x
        elif n < 0 :
            n = -1 * n
            for _ in range(n-1):
                result *= x
            result = 1/result
        return result