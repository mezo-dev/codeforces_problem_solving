


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for char in s[::-1]:
            if char == " " and length == 0:
                continue
            if char == " ":
                return length

            length += 1
        return length


obj = Solution()
print(obj.lengthOfLastWord(s="   fly me   to   the moon  "))