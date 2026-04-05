class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n, p, z = [], [], []

        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)
        
        if len(z) > 2:
            res.add((0, 0, 0))
        
        if z:
            for num in n:
                if -num in p:
                    res.add((num, 0, -num))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if -(n[i] + n[j]) in p:
                    target = -1*(n[i]+n[j])
                    res.add(tuple(sorted([n[i],n[j],target])))
        
        for k in range(len(p)):
            for l in range(k + 1, len(p)):
                if -(p[k] + p[l]) in n:
                    target = -1*(p[k]+p[l])
                    res.add(tuple(sorted([p[k],p[l],target])))
        
        return [list(r) for r in res]

