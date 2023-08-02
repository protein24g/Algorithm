import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y, h):
    global n
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and ary[nx][ny] > h:
                dfs(nx, ny, h)
    
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
ary, m = [], 0
for i in range(n):
    ary.append(list(map(int, input().split())))
    tmp = max(ary[i])
    if m < tmp: m = tmp

res = 1
for i in range(1, m+1):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and ary[j][k] > i:
                dfs(j, k, i) 
                cnt += 1
    res = max(res, cnt)
print(res)
