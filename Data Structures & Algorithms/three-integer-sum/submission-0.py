class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        res = set()
        n = len(nums)
        
        # Iterate over pairs (j, k)
        for j in range(n - 1):
            for k in range(j + 1, n):
                a, b = nums[j], nums[k]
                target = -(a + b)
                
                # Check if the target exists in the list
                if target not in hashmap:
                    continue
                
                # Count how many times target appears among the chosen numbers
                count = 0
                if target == a:
                    count += 1
                if target == b:
                    count += 1
                
                # The available count for target in the list must be greater than the count already used
                if hashmap[target] > count:
                    # Sort the triplet to avoid duplicates
                    triplet = tuple(sorted([a, b, target]))
                    res.add(triplet)
        
        return [list(trip) for trip in res]
