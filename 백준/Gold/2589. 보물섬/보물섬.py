from collections import deque
import sys
input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
ary = []
for i in range(n): ary.append(list(input()))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if ary[nx][ny] == 'L':
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        cnt = max(cnt, visited[nx][ny])
                        q.append((nx, ny))
    return cnt - 1

res = 0
for i in range(n):
    for j in range(m):
        if ary[i][j] == 'L':
            visited = [[0] * (m) for _ in range(n)]
            res = max(res, bfs(i, j))
print(res)
