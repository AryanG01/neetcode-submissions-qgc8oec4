class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s =[(p, s) for p, s in zip(position, speed)]
        p_s.sort(reverse=True)

        fleet = 1
        t1 = (target - p_s[0][0]) / p_s[0][1]

        for i in range(1, len(p_s)):
            t2 = (target - p_s[i][0]) / p_s[i][1]

            if t2 > t1:
                fleet += 1
                t1 = t2
            
        return fleet
