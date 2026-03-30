class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dp(n):
            if n in memo : return memo[n]
            if n == 1 : return 1
            if n == 2 : return 2
            step_nth = dp(n-1) + dp(n-2)
            memo[n] = step_nth
            return step_nth

        res = dp(n)
        return res

        