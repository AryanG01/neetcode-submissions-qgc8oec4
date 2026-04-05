class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return point[0] ** 2 + point[1]**2
        
        minheap = []
        heapq.heapify(minheap)
        count = 0

        for point in points:
            heapq.heappush(minheap, (-dist(point), point))
            count += 1
            if count > k:
                heapq.heappop(minheap)
        
        return [point for _, point in minheap]