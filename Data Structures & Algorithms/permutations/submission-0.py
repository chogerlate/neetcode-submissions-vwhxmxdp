class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [] # step 1: Initialize solution variable to store all the permuation results
        def backtrack(current:List[int], remaining:List[int]) -> None:
            # step 2: Indentify base case
            if not remaining:
                ans.append(list(current))
                return
            # step 3: Create exploration state
            for i in range(len(remaining)):
                # step 3.1: Choice chosing step
                current.append(remaining[i])
                # step 3.2: Explore another possibility
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()

        backtrack([], nums)
        return ans
        