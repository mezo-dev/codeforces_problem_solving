from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        compined_list = nums1[:m] + nums2[:n]
        nums1[:] = self.quick_sort(compined_list)


    def quick_sort(self, arr: List) -> List[int]:

        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2] # mid index

        left_side = [l for l in arr if l < pivot] 
        middel = [m for m in arr if m == pivot] 
        right_side = [r for r in arr if r > pivot]

        return self.quick_sort(left_side) + middel + self.quick_sort(right_side)
    


obj = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
obj.merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
print(nums1)