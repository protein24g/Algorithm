import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ary = []
for i in range(n): ary.append(int(input()))
ary.sort()

left, right = 0, 0
res = 2e9
while left <= right and right < n:
    if ary[right] - ary[left] < m: right += 1
    else:
        res = min(res, ary[right] - ary[left])
        left += 1
print(res)
      
        