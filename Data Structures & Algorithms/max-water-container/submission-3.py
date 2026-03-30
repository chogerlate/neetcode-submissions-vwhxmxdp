class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        classic 2 pointers from opposite end
        formula for calculate the maximum water = max(max_area, current_area)
        area calculation formula = min(heights[right], heights[left]) * (right - left)
        """
        left, right = 0, len(heights) -1 
        max_area = -1

        while left < right :
            current_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, current_area)

            if heights[left] < heights[right] :
                left += 1
            else :
                right -= 1
        
        return max_area
