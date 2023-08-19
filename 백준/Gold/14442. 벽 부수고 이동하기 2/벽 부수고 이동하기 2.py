from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, k])
    visited[0][0][k] = 1
    res = 1e9
    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            res = min(res, visited[x][y][z])
            continue
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if ary[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])
                elif ary[nx][ny] == 1 and z > 0 and visited[nx][ny][z-1] == 0:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    q.append([nx, ny, z-1])
    if res == 1e9: return -1
    else: return res
                    
    
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m , k = map(int, input().split())
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
ary = [list(map(int, input().strip())) for _ in range(n)]
print(bfs())
