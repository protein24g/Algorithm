import sys
input = sys.stdin.readline
n = int(input())
ary = list(map(int, input().split()))
m = int(input())

start, end = 0, max(ary)
while start <= end:
    mid = (start + end) // 2
    cur = 0
    for i in ary:
        if mid <= i: cur += mid
        else: cur += i
    if cur <= m: start = mid + 1
    else: end = mid - 1
print(end)
