class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def numOfTrips(cap):
            days = 0
            total = 0
            for i in weights:
                if total + i > cap:
                    total = 0
                    days += 1
                total += i
            if total:
                days += 1

            return days


        while low <= high:
            mid = low + (high - low) // 2

            if numOfTrips(mid) > days:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
