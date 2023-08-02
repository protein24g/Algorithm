import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt, n, m
    visited[x][y] = 1
    cnt += 1

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            if ary[nx][ny] == '.' and visited[nx][ny] == 0:
                dfs(nx, ny)
    return cnt

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while 1:
    m, n = list(map(int, input().split()))
    if m == n == 0: break
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ary = []
    cnt = 0
    for i in range(n): ary.append(list(map(str, input())))
    for i in range(n):
        for j in range(m):
            if ary[i][j] == '@':

                print(dfs(i, j))
