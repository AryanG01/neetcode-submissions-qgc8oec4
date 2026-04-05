class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p_dis = []

        for i in range(len(points)):
            p_dis.append([points[i], points[i][0] ** 2 + points[i][1] ** 2])
        
        sorted_array = sorted(p_dis, key=lambda x: x[1])

        return [point[0] for point in sorted_array[:k]]
