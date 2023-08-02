from collections import deque

def bfs():
    q = deque()
    visited[0][0][0] = 1
    q.append([0, 0, 0])

    while q:
        w, x, y = q.popleft()
        if x == n-1 and y == m-1: return visited[w][x][y]
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[w][nx][ny] == 0 and ary[nx][ny] == 0:
                    visited[w][nx][ny] = visited[w][x][y] + 1
                    q.append([w, nx, ny])
                elif ary[nx][ny] == 1 and w == 0 and visited[w+1][nx][ny] == 0:
                    visited[w+1][nx][ny] = visited[w][x][y] + 1
                    q.append([w+1, nx, ny])
    return -1

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = list(map(int, input().split()))
ary = []
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
for i in range(n):
    ary.append(list(map(int, input())))
print(bfs())
