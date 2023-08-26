from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx, sy, s_size):
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * (n) for _ in range(n)]
    visited[sx][sy] = True
    fish = []
    
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if ary[nx][ny] != 0 and ary[nx][ny] < s_size:
                        fish.append((cnt + 1, nx, ny))
                        q.append((nx, ny, cnt + 1))
                    elif ary[nx][ny] == 0 or ary[nx][ny] == s_size:
                        q.append((nx, ny, cnt + 1))
                        
    fish.sort()
    if fish:
        return [fish[0][1], fish[0][2], fish[0][0]]
    else:
        return []

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
s_size = 2
sx, sy = -1, -1

ary = []
for i in range(n):
    tmp = list(map(int, input().split()))
    ary.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            sx, sy = i, j
ary [sx][sy] = 0
ans, eat = 0, 0
while True:
    fish_eat = bfs(sx, sy, s_size)
    if fish_eat:
        x, y, move = fish_eat
        ary[x][y] = 0
        eat += 1
        ans += move
        if eat == s_size:
            s_size += 1
            eat = 0
        sx, sy = x, y
    else: break
print(ans)
