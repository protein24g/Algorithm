from collections import deque
import sys
input = sys.stdin.readline

def bfs(idx):
    global k
    x, y = dist[idx]
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if ary[nx][ny] != 'X':
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    for i in range(k):
        if i == idx: continue
        nx, ny = dist[i]
        if visited[nx][ny] == 0: brute[idx][i] = INF
        else: brute[idx][i] = visited[nx][ny]

def dfs(cur, s, dep):
    global res
    if res <= s: return
    if dep == 5: res = min(res, s); return
    for i in range(k):
        if kvisited[i] or brute[cur][i] >= INF: continue
        kvisited[i] = True
        dfs(i, s + brute[cur][i], dep+1)
        kvisited[i] = False

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
ary = []
dist = [()]
for i in range(n):
    tmp = list(input().strip())

    for j in range(m):
        if tmp[j] == 'S':
            dist[0] = (i, j)
            tmp[j] = '.'
        elif tmp[j] == 'K':
            dist.append((i, j))
            tmp[j] = '.'
    ary.append(tmp)

INF, res = 1e9, 1e9
k = len(dist)
brute = [[INF] * (k) for _ in range(k)]
for i in range(k): bfs(i)

kvisited = [False] * k
kvisited[0] = True
dfs(0, 0, 0)
if res != INF: print(res)
else: print(-1)
