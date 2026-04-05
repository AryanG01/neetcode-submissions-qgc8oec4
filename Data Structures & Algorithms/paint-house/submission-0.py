class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev_red = costs[0][0]
        prev_blue = costs[0][1]
        prev_green = costs[0][2]

        for i in range(1, len(costs)):
            temp_red, temp_blue, temp_green = prev_red, prev_blue, prev_green
            prev_red = costs[i][0] + min(temp_green, temp_blue)
            prev_blue = costs[i][1] + min(temp_red, temp_green)
            prev_green = costs[i][2] + min(temp_red, temp_blue)
        
        return min(prev_red, prev_blue, prev_green)