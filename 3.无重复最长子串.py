class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, d = -1, 0, {}
        for index, value in enumerate(s):
            if value in d and d[value] > k:
                k = d[value]
                d[value] = index
            else:
                d[value] = index
                res = max(res,index - k)
        return res
