class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = {1:1, 2:2}
        def dp(n):
            if n == 1 :
                return 1
            elif n == 2 : 
                return 2
            if n in mem:
                return mem[n]
            res = dp(n-1) + dp(n-2)
            mem[n] = res
            return mem[n]
        dp(n)
        return mem[n]