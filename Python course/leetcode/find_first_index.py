class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = haystack.find(needle)
        return x


s = Solution()
print(s.strStr("sadbutsad", "sad"))
