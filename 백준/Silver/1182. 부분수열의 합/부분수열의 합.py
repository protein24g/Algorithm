from itertools import combinations
n, s = map(int, input().split())
ary = list(map(int, input().split()))
cnt = 0
for i in range(1, len(ary)+1):
    for j in combinations(ary, i):
        if sum(j) == s: cnt += 1
print(cnt)