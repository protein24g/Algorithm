import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
ary = list(map(int, input().split()))

left, right, cnt = 0, 1, 0
while right <= len(ary):
    if sum(ary[left:right]) < m: right += 1
    elif sum(ary[left:right]) > m: left += 1
    else: cnt += 1; right += 1
print(cnt)
