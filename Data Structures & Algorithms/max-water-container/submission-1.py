class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        l = 0
        r = n - 1
        
        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            if area > max_area:
                max_area = area

            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1 

        return max_area