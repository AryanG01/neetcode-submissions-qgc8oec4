class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                elem = stack.pop()
                res[elem[0]] = i - elem[0]
            
            stack.append((i, temperatures[i]))
        
        return res
