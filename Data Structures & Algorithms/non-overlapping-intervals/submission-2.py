class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        To return the minimum number of intervals we need to remove to make 
        the rest of the intervals non-overlapping 
        
        ideal approach would be to remove the bigger intervals that will conflict 
        so sort them for smallest ending point first and for all those with same 
        ending point keep the smallest starting point
        """
        sorted_arr = sorted(intervals, key=lambda x: (x[1], x[0]))
        temp = sorted_arr[0][1]
        
        
        counter = 0

        for i in range(len(sorted_arr) - 1):
            if sorted_arr[i + 1][0] < temp:
                counter += 1
            else:
                temp = sorted_arr[i + 1][1]

        return counter