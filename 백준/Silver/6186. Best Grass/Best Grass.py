import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global n, m
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                if ary[nx][ny] == '#':
                    dfs(nx, ny)
    
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = list(map(int, input().split()))
ary = []
cnt = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    ary.append(list(map(str, input())))
for i in range(n):
    for j in range(m):
        if ary[i][j] == '#' and visited[i][j] == 0:
            cnt += 1
            dfs(i, j)
print(cnt)