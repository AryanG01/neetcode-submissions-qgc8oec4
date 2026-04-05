class Solution:

    def numberOfHoursNeeded(self, piles, speed):
        res = 0
        for i in piles:
            res += math.ceil(i / speed)
        
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2
            if self.numberOfHoursNeeded(piles, mid) <= h:
                high = mid
            else:
                low = mid + 1
        
        return low

