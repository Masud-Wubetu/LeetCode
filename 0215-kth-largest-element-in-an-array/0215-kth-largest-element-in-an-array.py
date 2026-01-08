class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(arr, s, e ):
            if s >= e:
                return
            
            pivot = arr[e]
            left = s

            for i in range(s, e):
                if arr[i] < pivot:
                  arr[i], arr[left] = arr[left], arr[i]
                  left += 1
            arr[e], arr[left] = arr[left], arr[e]

            quickSort(arr, s, left -1)
            quickSort(arr, left + 1, e)

        quickSort(nums, 0, len(nums) - 1)
        return nums[-k]


        