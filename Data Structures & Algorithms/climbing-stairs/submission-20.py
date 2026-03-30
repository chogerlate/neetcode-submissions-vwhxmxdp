class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Step to solve the dynamic programming
        1. we analyst the problem with these questions:
            -> 1. Identify the State: What variables uniquely define a subproblem? 
            (e.g., i for index in an array, w for remaining capacity in a bag).
            -> 2. The Recursive Relation: how do we solve the current state using the result from smaller state
            -> 3. Base Case: the smallest possible version of this problem that we know the result 
        2. Analyst the problem
            1. Identify the state:
                1.1 the Big problem is find the number of distinct way to climb to the top
                1.2 the smallest problem is 
        """
        memo = {}
        def dp(current_step: int) -> int :
            
            if current_step <= 3 : return current_step
            if current_step in memo : return memo[current_step]

            current_step_count = dp(current_step - 1) + dp(current_step - 2)
    
            memo[current_step] = current_step_count 
            return current_step_count
        
        count = dp(n)
        return count