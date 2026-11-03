class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        # while left < right:
        #     if heights[left] <= heights[right]:
        #         left += 1
        #     else:
        #         right -= 1
        #     width = right - left
        #     min_height = min(heights[left], heights[right])
        #     area = min_height * width
        #     best = max(area, best)
        # return best
        while left < right:
            width = right - left 
            min_height = min(heights[left], heights[right])
            area = min_height * width
            best = max(best, area)
            if heights[left] > heights[right]:
                right -= 1 
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
            # left += 1
            # right -= 1
        
        return best

        