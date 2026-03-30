class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0 
        for idx, h in enumerate(heights):
            fallback_idx = idx
            while stack and stack[-1][-1] > h :
                temp_idx, temp_h = stack.pop()
                res = max(res, (idx-temp_idx) * temp_h)
                fallback_idx = temp_idx
                
            stack.append((fallback_idx, h))
        
        while stack :
            temp_idx, temp_h = stack.pop()
            res = max(res, (n-temp_idx) * temp_h)
        
        return res 