import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in range(1, N+1):
        if ary[v][i] == 1 and visited[i] == 0:
            dfs(i)
    
N, M = list(map(int, input().split()))

ary = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0] * (N+1)
    
for i in range(M):
    x, y = list(map(int, input().split()))
    ary[x][y] = 1
    ary[y][x] = 1

check = 0
for i in range(1, N+1):
    if visited[i] == 0:
       dfs(i)
       check += 1 
print(check)