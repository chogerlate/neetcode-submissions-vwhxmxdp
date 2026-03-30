class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Let analyst the problem 
        is this dp:
        1. the current state come from the past state [check]
        2. Does we need the best path from the previous result to acheive the best path of the final result [check]
        conclusion: DP [Yes]

        3-steps framework:
        1. Identify the idenpenden states to track for the sub-problem
            - the floor-th -> track the current floor
        2. Recurrent relaship 
            - we have 2 action for each step: take 1 step or 2 step 
            - recurrent relaship would be 
                `best_cost_for_each_floor = this_floor_cost + min(solve(current_floor -1), solve(current_floor - 2))`
        3. base case
            - if we start at index 0 the cost equal to cost[0]
            - if we start at index 1 the cost equal to cost[1]
            - let go 
        """
        memo = {}
        def dp(floor_th: int) -> int :
            if floor_th in memo : return memo[floor_th]
            if floor_th == 0 : return cost[0]
            if floor_th == 1 : return cost[1]

            min_cost_at_floor_th = min(cost[floor_th] + dp(floor_th - 1), cost[floor_th] + dp(floor_th-2))
            memo[floor_th] = min_cost_at_floor_th
            return min_cost_at_floor_th

        n = len(cost)
        cost.append(0)
        best_cost = dp(n)
        return best_cost