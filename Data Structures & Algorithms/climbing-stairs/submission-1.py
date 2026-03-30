class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = {}
        def climb(x):
            if x > n :
                return 0
            elif x == n :
                return 1 
            mem[x] = climb(x+1) + climb(x+2)
            return mem[x]
        
        return climb(0)