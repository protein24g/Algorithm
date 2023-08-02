import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    global w, h
    visited[x][y] = 1
    for i in range(8):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < h and 0 <= ny < w:
            if visited[nx][ny] == 0 and ary[nx][ny] == 1:
                dfs(nx, ny)

d = [(-1, 0), (1, 0), (0, -1), (0, 1),
     (-1, -1), (-1, 1), (1, -1), (1, 1)]
while 1:
    w, h = list(map(int, input().split()))
    if w == h == 0: break
    ary = []
    cnt = 0
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        ary.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if ary[i][j] and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
