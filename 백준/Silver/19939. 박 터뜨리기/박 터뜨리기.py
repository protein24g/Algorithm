import sys
input = sys.stdin.readline
n, k = map(int, input().split())
check = k * (k + 1) // 2

if n < check: print(-1)
elif (n - check) % k == 0: print(k-1)
else: print(k)
    