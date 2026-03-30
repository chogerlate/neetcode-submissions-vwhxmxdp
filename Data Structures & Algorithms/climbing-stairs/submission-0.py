class Solution:
    def climbStairs(self, n: int) -> int:
        
        # mem = {}
        def climb(x):
            if x > n :
                return 0
            elif x == n :
                return 1 
            
            return climb(x+1) + climb(x+2)
        
        return climb(0)