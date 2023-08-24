from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx, ny, nz = x + d[i][1], y + d[i][2], z + d[i][0]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if ary[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    ary[nz][nx][ny] = ary[z][x][y] + 1

d = [(0, -1, 0), (0, 1, 0), (0, 0, -1),
         (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
    
m, n, h = map(int, input().split())
ary = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    ary.append(tmp)

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if ary[i][j][k] == 1:
                q.append((i, j, k))
bfs()
ans = 0
for i in ary:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans-1)
