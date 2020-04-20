class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not needle in haystack: return -1
        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)]:
                return i
                break
import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        loc = re.search(needle,haystack).span()
        return loc[0]
