from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    visited = [[-1] * (n) for _ in range(n)]
    q = deque(v)
    for i, j in q: visited[i][j] = 0
    res = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if ary[nx][ny] != 1 and visited[nx][ny] == -1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    res = max(res, visited[x][y] + 1)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and ary[i][j] != 1:
                return 1e9
    return res

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
ary = []
virus = []

for i in range(n):
    ary.append(list(map(int, input().split())))
    for j in range(n):
        if ary[i][j] == 2: virus.append([i, j])

ans = 1e9
for i in combinations(virus, m): ans = min(ans, bfs(i))
if ans == 1e9: print(-1)
else: print(ans)
