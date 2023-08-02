import sys
from collections import deque
sys.setrecursionlimit(10**6)

def bfs(x, y):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append([x, y])
    cnt, res = 0, -1
    
    while q:
        x, y = q.popleft()
        cnt += 1
        if ary[x][y] == 1: return visited[x][y]
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny] == 0:
                    if ary[nx][ny] != -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])
    return res

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ary = []
for i in range(5): ary.append(list(map(int, input().split())))
r, c = list(map(int, input().split()))
print(bfs(r, c))
