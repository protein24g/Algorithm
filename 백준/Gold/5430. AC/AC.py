import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for i in range(t):
    p = input().strip()
    n = int(input())
    flag = 1
    tmp = input().strip()
    tmp = deque(tmp[1:-1].split(','))
    if n == 0: tmp = deque()
    r_c = 0
    for j in p:
        if j == 'R': r_c += 1
        elif j == 'D':
            if len(tmp) == 0:
                print('error'); flag = 0; break
            else:
                if r_c % 2 == 0: tmp.popleft()
                else: tmp.pop()
    if flag == 0: continue
    else:
        if r_c % 2 == 0: print('[' + ",".join(tmp) + ']')
        else: tmp.reverse(); print('[' + ",".join(tmp) + ']')
