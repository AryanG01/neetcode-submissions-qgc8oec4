class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            heapq.heappush(arr, num)

        res = []
        while arr:
            res.append(heapq.heappop(arr))
        
        return res