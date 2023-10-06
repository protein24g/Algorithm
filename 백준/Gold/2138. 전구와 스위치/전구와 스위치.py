import sys
input = sys.stdin.readline

def chk():
    cnt = 0
    a_copy = ary[:]
    for i in range(1, N):
        if a_copy[i-1] != target[i-1]:
            for j in range(i-1, i+2):
                if 0 <= j < N:
                    a_copy[j] = 1 - a_copy[j]
            cnt += 1
    if a_copy == target: return cnt
    else: return 1e9

N = int(input())
ary = list(map(int, input().strip()))
target = list(map(int, input().strip()))

res = chk()
ary[0], ary[1] = 1 - ary[0], 1 - ary[1]
res = min(res, chk() + 1)
if res == 1e9: print(-1)
else: print(res)
