from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = Counter(s)
        stack, al = [], set()
        for i in s:
            d[i] -= 1
            if i in al:
                continue
            while stack and i < stack[-1] and d[stack[-1]] > 0:
                al.remove(stack.pop())
            stack.append(i)
            al.add(i)
        return ''.join(stack)
