import sys
input = sys.stdin.readline

N, K, L = list(map(int, input().split()))

res = []
for i in range(N):
    chk = True
    temp = list(map(int, input().split()))

    for j in temp:
        if L > j:
            chk = False

    if chk == True and sum(temp) >= K:
        res.extend(temp)

print(len(res) // 3)
print(*res)