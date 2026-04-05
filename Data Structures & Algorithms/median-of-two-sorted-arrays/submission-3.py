class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1 = len(nums1)
        len2 = len(nums2)

        total = len1 + len2
        half = (total + 1) // 2

        low = 0
        high = len1

        while low <= high:
            i = low + (high - low) // 2
            j = half - i

            L1 = nums1[i - 1] if i > 0 else float("-inf")
            R1 = nums1[i] if i < len1 else float('inf')

            L2 = nums2[j - 1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < len2 else float('inf')

            if L1 <= R2 and L2 <= R1:
                if total % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)
            elif L1 >= R2:
                high = i - 1
            elif L2 >= R1:
                low = i + 1

