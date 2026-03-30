class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l, max_r = [height[0]] * n, [height[n-1]] * n
        cur_max_l, cur_max_r = height[0], height[n-1]
        min_h = [0] * n
        res = 0

        for i in range(n):
            if cur_max_l < height[i] :
                max_l[i] = height[i]
                cur_max_l = height[i]
            else :
                max_l[i] = cur_max_l
            if cur_max_r < height[n-i-1]:
                max_r[n-i-1] = height[n-i-1]
                cur_max_r = height[n-i-1]
            else :
                max_r[n-i-1] = cur_max_r
        print(max_l, max_r)
        for i in range(n):
            min_h[i] = min(max_l[i], max_r[i])
            temp_res = min_h[i] - height[i] 
            if temp_res > 0:
                res += temp_res
        return res