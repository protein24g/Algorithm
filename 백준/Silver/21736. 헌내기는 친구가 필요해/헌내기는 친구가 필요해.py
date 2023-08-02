import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                if ary[nx][ny] != 'X':
                    if ary[nx][ny] == 'P': cnt += 1
                    dfs(nx, ny)
    return cnt

cnt = 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = list(map(int, input().split()))
visited = [[0 for _ in range(m)] for _ in range(n)]
ary = []
for i in range(n):
    ary.append(list(map(str, input())))
for i in range(n):
    for j in range(m):
        if ary[i][j] == 'I':
            if dfs(i, j) == 0:
                print('TT')
            else:
                print(cnt)
