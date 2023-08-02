N, K = list(map(int, input().split()))

coin = []

for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

cnt = 0
for i in range(N):
    cnt += K // coin[i]
    K -= (K // coin[i]) * coin[i]
print(cnt)
