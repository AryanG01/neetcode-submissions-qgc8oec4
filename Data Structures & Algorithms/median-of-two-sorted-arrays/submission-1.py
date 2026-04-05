class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Make sure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m  # binary search range in nums1

        while left <= right:
            # Partition nums1 at i, which gives us j from nums2
            i = (left + right) // 2
            j = half - i

            # Get values on either side of partition
            L1 = nums1[i - 1] if i > 0 else float('-inf')  # max on left of nums1
            R1 = nums1[i] if i < m else float('inf')       # min on right of nums1
            L2 = nums2[j - 1] if j > 0 else float('-inf')  # max on left of nums2
            R2 = nums2[j] if j < n else float('inf')       # min on right of nums2

            # Valid partition found
            if L1 <= R2 and L2 <= R1:
                if total % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)
            
            # Adjust search direction
            elif L1 > R2:
                right = i - 1  # move left
            else:
                left = i + 1   # move right
