class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        left, right = 0, len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            water = height * width
            maxwater = max(maxwater, water)

            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
        return maxwater