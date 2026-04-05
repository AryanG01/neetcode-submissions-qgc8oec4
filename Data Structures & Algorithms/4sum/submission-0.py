class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                rem = target - (nums[i] + nums[j])
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] < rem:
                        l += 1
                    elif nums[l] + nums[r] > rem:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
        
        return [list(x) for x in set(tuple(sorted(t)) for t in res)]
                
