class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:
            if i in d:
                if not stack or stack.pop() != d[i]:
                    return False
            else:
                stack.append(i)
        if not stack: return True
        else: return False
