class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for idx, temp in enumerate(temperatures) :
            while stack and stack[-1][1] < temperatures[idx]:
                temp_idx, t = stack.pop()
                res[temp_idx] = idx - temp_idx
            
            # base case add the temp and their correspond index to stack
            stack.append((idx, temp))
        return res

            