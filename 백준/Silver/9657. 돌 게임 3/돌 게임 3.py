N = int(input())
dp = [-1] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1
dp[5] = 1

for i in range(6, N+1):
    if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] ==0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[N] == 1:
    print("SK")
else:
    print("CY")