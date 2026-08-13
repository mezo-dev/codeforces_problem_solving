



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        print(len(haystack) - len(needle) + 1)

        for i in range(len(haystack) - len(needle) + 1):

            if haystack[i:i + len(needle)] == needle:
                return i
            
        return -1




obj = Solution()
print(obj.strStr(haystack="hello world", needle="world"))