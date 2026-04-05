class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)):
            if (target - numbers[i]) in hashmap:
                return [hashmap[target - numbers[i]], i + 1]
            else:
                hashmap[numbers[i]] = i + 1