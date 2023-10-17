def solution(s):
    answer = 1e9
    for i in range(0, len(s)):
        stack = []
        res = ''
        for j in range(0, len(s), i+1):
            tmp = s[j:j+i+1]
            if not stack or stack[-1] == tmp:
                stack.append(tmp)
            else:
                if len(stack) == 1:
                    res += stack[0]
                else:
                    res += str(len(stack)) + stack[0]
                stack = []
                stack.append(tmp)
        
        if stack:
            if len(stack) == 1: res += stack[0]
            else: res += str(len(stack)) + stack[0]
        answer = min(answer, len(res))
        
    return answer