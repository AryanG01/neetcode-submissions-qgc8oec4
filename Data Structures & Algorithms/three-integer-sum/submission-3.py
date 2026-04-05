class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, z, p = [], [], []
        res = set()

        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)
        
        if len(z) > 2:
            res.add((0, 0, 0))

        if len(z) > 0:
            for num in n:
                if -num in p:
                    res.add((num, 0, -num))
            
            for num in p:
                if -num in n:
                    res.add((-num, 0, num))
        
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                if -(n[i] + n[j]) in p:
                    res.add((n[i], n[j], -(n[i] + n[j])))

        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                if -(p[i] + p[j]) in n:
                    res.add((-(p[i] + p[j]), p[i], p[j]))
        
        return [list(elem) for elem in res]