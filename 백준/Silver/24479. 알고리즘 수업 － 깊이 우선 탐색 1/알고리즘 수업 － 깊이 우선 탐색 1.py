import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(ary, r, visited):
    global cnt
    visited[r] = cnt
    for i in ary[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(ary, i, visited)

n, m, r = list(map(int, input().split()))
ary = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    u, v = list(map(int, input().split()))
    ary[u].append(v)
    ary[v].append(u)

for i in range(n+1): ary[i].sort()

cnt = 1
dfs(ary, r, visited)
for i in range(1, n+1): print(visited[i])
