from itertools import combinations
n, m = map(int, input().split())
ary = [i for i in range(1, n+1)]
for i in combinations(ary, m):
    print(*i)
