import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))
each = 0

for i in range(K):
    each += nums[i]
maxv = each

for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)
print(maxv)
