class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        cnt = 0

        for i in range(len(freq) - 1, -1, -1):
            for x in freq[i]:
                res.append(x)
                cnt += 1

                if cnt == k:
                    return res
        
        return res
