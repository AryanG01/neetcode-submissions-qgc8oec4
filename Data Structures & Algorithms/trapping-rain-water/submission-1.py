class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Use a pointer first to get the starting point its where the height 
        starts to drop from the next element coz that means the water can be trapped

        so check while start < total length, we go until the condition is satisified
        then whenever we have a start we increment another pointer end that will stop
        when we hit something of the same length or bigger. 
        
        while we are incrementing we will keep track of the smaller heights coz thats
        how much to minus of the volume

        if there is no bigger one to the left then we will keep track of the largest 
        height we saw and use it to calulate the volume and increment start after that
        """

        volume = 0
        start = 0
        
        if len(height) < 2:
            return 0

        while start < len(height):
            # This is to ensure that we get a starting point from which water 
            # can be trapped
            while start < len(height) - 1 and height[start] <= height[start + 1]:
                start += 1
            
            if start == len(height) - 1:
                break
            
            end = start + 1

            decrement = 0
            distance = 0
            max_smallest_height = (0, 0, 0, 0) # the height, the index, distance 
                                               # and decrement till this point

            while end < len(height) and height[end] < height[start]:
                decrement += height[end]
                distance += 1
                if height[end] >= max_smallest_height[0]:
                    max_smallest_height = (height[end], end, distance - 1, decrement - height[end])

                end += 1

            if end != len(height):
                volume += height[start] * distance - decrement
                start = end
            else:
                volume += max_smallest_height[0] * max_smallest_height[2] - max_smallest_height[3]
                start = max_smallest_height[1]

        return volume

