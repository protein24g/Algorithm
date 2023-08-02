from collections import deque

def bfs(x, y):
    global n, m
    q = deque()
    q. append([x, y])

    res = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if ary[nx][ny] == 0:
                    ary[nx][ny] = ary[x][y] + 1
                    q.append([nx, ny])
                    res = max(res, ary[x][y] + 1)
                elif ary[nx][ny] > 1:
                    if ary[x][y]+1 < ary[nx][ny]:
                        ary[nx][ny] = ary[x][y]+1
                        q.append([nx, ny])
                        res = max(res, ary[x][y] + 1)

d = [(-1, -1), (-1, 1), (1, -1), (1, 1),
     (-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = list(map(int, input().split()))
ary = []

for i in range(n): ary.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        if ary[i][j] == 1:
            bfs(i, j)

res = 0            
for i in range(n):
    for j in range(m):
        res = max(res, max(ary[i])-1)
print(res)
