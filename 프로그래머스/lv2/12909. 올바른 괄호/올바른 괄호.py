def solution(s):
    answer = True
    op = 0
    ary = []
    for i, j in enumerate(s):
        if i == 0 and j == ')': return False
        elif j == '(':
            ary.append(j)
            op += 1
        elif j == ')':
            op -= 1
            if op < 0: return False
    if op == 0: return True
    else: return False