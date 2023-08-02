from collections import deque

def bfs(x, y):
    global n, m
    q = deque()
    q.append([x, y])
    ary[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if ary[nx][ny] == 1:
                    ary[nx][ny] = 0
                    cnt += 1
                    q.append([nx, ny])
    return cnt
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = list(map(int, input().split()))
ary = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n): ary.append(list(map(int, input().split())))

res = []
for i in range(n):
    for j in range(m):
        if ary[i][j] == 1 and visited[i][j] == 0:
            res.append(bfs(i, j))
if len(res) == 0:
    print(len(res))
    print(0)
else:
    print(len(res))
    print(max(res))
