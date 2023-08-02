import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    pw = list(input().strip())
    l, r = [], []

    for j in pw:
        if j == '<':
            if l: r.append(l.pop())
        elif j == '>':
            if r: l.append(r.pop())
        elif j == '-':
            if l: l.pop()
        else: l.append(j)
    l.extend(reversed(r))

    print(''.join(l))