class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p, z, n, res = [], [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        
        P, N = set(p), set(n)

        if len(z) >= 3:
            res.append([0, 0, 0])
        
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                neg = -(p[i] + p[j])
                if neg in N:
                    res.append([neg, p[i], p[j]])
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                pos = -(n[i] + n[j])
                if pos in P:
                    res.append([pos, n[i], n[j]])
        
        if len(z) > 0:
            for val in P:
                if -val in N:
                    res.append([-val, 0, val])

        # Use a set of tuples to remove duplicate triplets caused by duplicate numbers in input
        return [list(x) for x in set(tuple(sorted(t)) for t in res)]