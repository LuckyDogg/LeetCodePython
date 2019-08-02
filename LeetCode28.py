class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle) if len(needle) > 0 else 0
        except:
            return -1
