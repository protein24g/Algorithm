def dfs(x, y):
    global cnt, n, m
    visited[x][y] = 1
    cnt += 1

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                if ary[x][y] == ary[nx][ny]:
                    dfs(nx, ny)
    return cnt

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
m, n = list(map(int, input().split()))
ary = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n): ary.append(list(map(str, input())))

res_w, res_b = 0, 0
for i in range(n):
    for j in range(m):
        if ary[i][j] == 'W' and visited[i][j] == 0:
            cnt = 0            
            res_w += (dfs(i, j)**2)
        elif ary[i][j] == 'B' and visited[i][j] == 0:
            cnt = 0
            res_b += (dfs(i, j)**2)
        
print(res_w, res_b)
