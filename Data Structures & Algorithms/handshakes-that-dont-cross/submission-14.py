class Solution:
    def numberOfWays(self, total_ppl: int) -> int:
        MOD = 1000000007

        d = {}
        def f(n):
            #base case 
            if n == 0: 
                return 1
            if n == 1:
                return 0
            #memo lookup
            if n in d:
                return d[n]
            #recursion
            _sum = 0
            for j in range(1, n, 2):
                p = f(j-1) * f(n-j-1)
                _sum += p
            d[n] = _sum
            return d[n]
        return f(total_ppl) % MOD