from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result ^= i
        return result







obj = Solution()
print(obj.singleNumber(nums=[1]))
obj = Solution()
print(obj.singleNumber(nums=[1]))