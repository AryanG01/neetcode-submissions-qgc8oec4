class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        can we do a recursive approach? We start with the first index and see the max
        jumps we can make and in all of the positions we can end up we have another 
        call to see if we can end up at the last pos from any of them. There might be 
        a lot of duplicates in this process coz jumps cant get added up if they werent
        used

        how about dp? we calculate the max possible ways??? no idea how to implement
        this in dp

        actually we can just check if its possible to reach this index from another one.
        The front approach is just dp but if we go from the back we see if we can reach 
        an index from a previous index + jump and then decrement our goal accordingly
        coz if we can reach n from n-1, then we see if we can reach n-1 from n-2 and so
        on so forth
        """

        final_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= final_index:
                final_index = i
        
        return final_index == 0