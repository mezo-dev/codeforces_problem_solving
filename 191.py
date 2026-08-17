from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}

        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
    
        for k, v in result.items():
            if v == 1:
                return k






obj = Solution()
print(obj.singleNumber(nums=[1]))