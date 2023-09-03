class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        if s == s[::-1]: return s
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    res.append(s[i:j])
        return max(res, key=len)
