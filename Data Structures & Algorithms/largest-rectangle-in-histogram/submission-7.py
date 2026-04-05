class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        l = len(heights)

        for i in range(l):
            while stack and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = l if not stack else l - stack[-1] - 1
            max_area = max(max_area, height * width)
    
        return max_area


