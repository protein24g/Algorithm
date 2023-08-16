from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
home, chik = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, k in enumerate(tmp):
        if k == 1:
            home.append([i, j])
        elif k == 2:
            chik.append([i, j])

res = 1e9
for ch in combinations(chik, m):
    com_res = 0
    for h in home:
        dist = 1e9
        for c in ch:
            dist = min(dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        com_res += dist
    res = min(res, com_res)
print(res)
