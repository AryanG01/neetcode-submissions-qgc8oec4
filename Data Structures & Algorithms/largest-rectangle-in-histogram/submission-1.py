class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        We can use a stack and keep track of the rectangles being formed. 

        if our stack is empty so we just add it our stack and dont do anything else, but
        since we need the width it might make more sense to keep track of the index coz
        then we can do a retrieval for the height

        we only keep strictly increasing elements in the stack if we encounter anything
        less than or equal to we pop the biggest element from the array and we get the
        height. 
        
        we see if the stack is empty meaning the height we have is the smallest
        and the rectangle can extend across all the points till now so width is i, else
        the width be the index we are at - index of the next biggest element - 1 coz
        the next biggest element wont come in the rectangle of the current height

        we calulate the height obtained anb compare it to max height 
        """
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = i + 1 if not stack else i + 1 - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        
        return maxArea