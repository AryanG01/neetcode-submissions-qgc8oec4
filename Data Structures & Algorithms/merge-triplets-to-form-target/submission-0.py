class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        ok so we have a bunch of triplets and we need to see if we can obtain the target
        by taking the max between each of the indexes.

        we can start by ignoring all those triplets where even a single value is greater
        than its position in target, coz then we can never reach the target coz the value
        at that index will always be greater

        so now we just need to check amongst the values we have so far if we can get 
        target[0] at index 0, target[1] at index 1 and target[2] at index 2
        """

        hashmap = {
            0: False,
            1: False,
            2: False
        }

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    hashmap[i] = True
        
        return hashmap[0] == True and hashmap[1] == True and hashmap[2] == True