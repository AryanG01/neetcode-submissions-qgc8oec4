class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        If total gas is less than total cost, there's no solution. But if 
        total gas >= total cost, there is guaranteed to be one valid starting point.

        we can use 2 pointers a start and an end to make a window of possible routes.
        so we keep track of total amount of gas at the starting point and see if we can
        get to the next station if not we decrease our starting point to add in another 
        station as we need more gas. But if we can then increase start to show we can
        travel to another station
        """

        start = len(gas) - 1
        end = 0

        total = gas[start] - cost[start]

        while start != end:
            if total < 0:
                start -= 1
                total += gas[start] - cost[start]
            else:
                total += gas[end] - cost[end]
                end += 1
        
        return start if total >= 0 else -1