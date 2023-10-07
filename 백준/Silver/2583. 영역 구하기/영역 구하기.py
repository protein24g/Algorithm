import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    ary[x][y] =1
    cnt = 1
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < M and 0 <= ny < N:
                if ary[nx][ny] == 0:
                    ary[nx][ny] = 1
                    q.append([nx, ny])
                    cnt += 1
    return cnt

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
M, N, K = map(int, input().split())
ary = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    l_x, l_y, r_x, r_y = map(int, input().split())
    for i in range(l_y, r_y):
        for j in range(l_x, r_x):
            ary[i][j] = 1

res = []
for i in range(M):
    for j in range(N):
        if ary[i][j] == 0 and not visited[i][j]:
            res.append(bfs(i, j))
print(len(res))
print(*sorted(res))
