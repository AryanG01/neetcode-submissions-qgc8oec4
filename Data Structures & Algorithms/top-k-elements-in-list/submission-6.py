class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq =[[] for _ in range(len(nums) + 1)]

        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        cnt = 0

        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for j in range(len(freq[i])):
                    res.append(freq[i][j])
                    cnt += 1
        
                if cnt == k:
                    return res
        
        return res
