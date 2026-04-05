class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-stone for stone in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            s1 = heapq.heappop(arr)
            s2 = heapq.heappop(arr)
            
            rem = s1 - s2

            if rem != 0:
                heapq.heappush(arr, rem)
        
        return -arr[0] if arr else 0

