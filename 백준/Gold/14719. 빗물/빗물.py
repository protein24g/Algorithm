import sys
input = sys.stdin.readline

H, W = map(int, input().split())
ary = list(map(int, input().split()))
cnt = 0
for i in range(1, W-1):
    tmp = min(max(ary[:i]), max(ary[i+1:]))
    if tmp > ary[i]:
        cnt += tmp - ary[i]
    
print(cnt)
