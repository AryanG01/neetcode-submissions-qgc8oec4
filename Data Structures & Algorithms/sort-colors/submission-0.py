class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums, 0, len(nums) - 1)
    
    def mergeSort(self, arr, l, r):
        if l >= r:
            return 

        mid = l + (r - l) // 2

        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, r, mid)
    
    def merge(self, arr, l, r, mid):
        i = l
        j = mid + 1

        while i <= mid and j <= r:
            # already in correct order
            if arr[i] <= arr[j]:
                i += 1
            else:
                # arr[j] should be placed before arr[i]
                value = arr[j]
                index = j

                # shift left half right by 1
                while index > i:
                    arr[index] = arr[index - 1]
                    index -= 1

                arr[i] = value

                # update pointers
                i += 1
                mid += 1
                j += 1


    

