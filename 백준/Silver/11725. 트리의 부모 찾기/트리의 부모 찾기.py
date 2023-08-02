import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    for i in ary[x]:
        if visited[i] == 0:
            visited[i] = x
            dfs(i)

n = int(input())
ary = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    ary[a].append(b); ary[b].append(a)
dfs(1)
for i in range(2, len(visited)):
    print(visited[i])
