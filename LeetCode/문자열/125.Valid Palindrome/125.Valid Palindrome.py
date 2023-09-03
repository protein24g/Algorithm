from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque()
        for i in s:
            if i.isalnum():
                q.append(i.lower())
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
