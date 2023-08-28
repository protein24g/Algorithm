import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y, s, dep):
    global res
    if dep == 4:
       res = max(res, s)
       return
    else:
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    dfs(nx, ny, s + ary[nx][ny], dep + 1)
                    visited[nx][ny] = False

def f_dfs(x, y, s):
    global res
    f_d = [[(-1, 0), (0, -1), (0, 1)],
         [(1, 0), (0, -1), (0, 1)],
         [(0, -1), (-1, 0), (1, 0)],
         [(0, 1), (-1, 0), (1, 0)]]

    for udlr in f_d:
        tmp = s
        for i in udlr:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < n and 0 <= ny < m:
                tmp += ary[nx][ny]
            else: break
        else:
            res = max(res, tmp)  

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
visited = [[False] * (m) for _ in range(n)]

ary = []
for i in range(n):
    ary.append(list(map(int, input().split())))

res = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, ary[i][j], 1)
        visited[i][j] = False

        f_dfs(i, j, ary[i][j])
print(res)
