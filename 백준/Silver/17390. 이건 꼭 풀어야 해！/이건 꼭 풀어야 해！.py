import sys
input = sys.stdin.readline

n, q = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
psum = [0] * (n+1)

for i in range(1, n+1):
    psum[i] = psum[i-1] + nums[i-1]
for i in range(q):
    l, r = list(map(int, input().split()))
    print(psum[r]-psum[l-1])
