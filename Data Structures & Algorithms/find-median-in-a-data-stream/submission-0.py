class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if self.high and self.high[0] > num:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        
        if len(self.high) - len(self.low) > 1:
            heapq.heappush(self.low, -heapq.heappop(self.high))
        elif len(self.low) - len(self.high) > 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))

    def findMedian(self) -> float:
        if (len(self.low) + len(self.high)) % 2 == 0:
            return (-self.low[0] + self.high[0]) / 2
        else:
            if len(self.low) > len(self.high):
                return -self.low[0]
            else:
                return self.high[0]
        