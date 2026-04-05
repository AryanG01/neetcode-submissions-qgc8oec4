class Solution:
    def numWays(self, n: int, k: int) -> int:
        '''
        if we just have 1 post the number of ways of paintign it are k

        if we have 2, the if we paint of them the same or diff it doesnt matter as they are both valid,
        so we have k * k options

        the interesting part comes from 3 fences onwards
        if we want to paint the same as the prev we can only do it if the prev fence was of a diff colour
        and then the number of ways to paint he new fence same is the same as the number of ways to paint
        the old fence diff

        if we want to paint the new fence diff, then it doesnt matter what the pre fence was we just take
        total number of ways to get to prev fence (prev_same + prev_diff) * (k - 1) where (k - 1) is the
        number of diff colours we an paint the new fence
        '''
        if n == 1:
            return k
        
        if n == 2:
            return k * k
        
        prev_same = k
        prev_diff = k * (k - 1)

        for i in range(3, n + 1):
            new_same = prev_diff
            new_diff = (prev_same + prev_diff) * (k - 1)

            prev_same, prev_diff = new_same, new_diff
        
        return prev_same + prev_diff