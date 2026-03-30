class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start:int, current:List[int], remaining:int) -> None:
            # current: as a current state of each iteration
            # remaining: as a current target value 
            if remaining == 0 :
                if current not in ans :
                    ans.append(current.copy())
                return
            if remaining < 0 :
                return

            for i in range(start, len(candidates)):
                # if i > 1 and candidates[i] == candidates[i-1] :
                #     continue
                current.append(candidates[i])
                backtrack(i+1, current, remaining - candidates[i])
                current.pop()

        candidates.sort()
        backtrack(0, [], target)
        return ans