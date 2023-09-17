import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cur = 1
cnt = 0
for tmp in range(int(input())):
    tmp = int(input())
    if cur <= tmp <= (cur + m - 1):
        continue
    elif cur < tmp:
        cnt += tmp - (cur+m-1)
        cur += tmp - (cur+m-1)
    elif tmp < cur:
        cnt += cur - tmp
        cur -= cur - tmp 
print(cnt)
