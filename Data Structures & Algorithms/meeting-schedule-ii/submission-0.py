"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []

        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
        
        days = 0
        res = 0

        time.sort(key=lambda x: (x[0], x[1]))

        for i in time:
            days += i[1]
            res = max(days, res)
        
        return res