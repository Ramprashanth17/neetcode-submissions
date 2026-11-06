class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, ht = stack.pop()
                width = i - index
                area = ht * width
                max_area = max(area, max_area)
                start = index
            stack.append((start, height))

        for i, height in stack:
            width = len(heights) - i
            area = height * width
            max_area = max(area, max_area)
        
        return max_area