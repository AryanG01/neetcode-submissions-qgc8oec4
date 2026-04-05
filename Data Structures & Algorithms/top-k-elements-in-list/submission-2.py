class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for num, count in count.items():
            freq[count].append(num)
        
        res = []
        cnt = 0

        for i in range(len(freq) -1, -1, -1):
            for e in freq[i]:
                res.append(e)
                cnt += 1
                if cnt == k:
                    return res
        
        return res