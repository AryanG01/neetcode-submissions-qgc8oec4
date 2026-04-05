class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        maxV = 0

        while start < end:
            v = (end - start) * min(heights[start], heights[end])
            maxV = max(v, maxV)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return maxV