N = int(input())
dp = [-1] * 1001

dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, N+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[N] == 0:
    print("CY")
else:
    print("SK")