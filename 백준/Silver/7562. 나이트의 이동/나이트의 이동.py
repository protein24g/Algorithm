from collections import deque

def bfs(x, y, ex, ey):
    d = [[-2, -1], [-2, 1], [-1, -2], [-1, 2],
     [1, -2], [1, 2], [2, -1], [2, 1]]
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return ary[x][y] - 1
        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if l > nx >= 0 and l > ny >= 0 and ary[nx][ny] == 0:
                q.append([nx, ny])
                ary[nx][ny] = ary[x][y] + 1

t = int(input())
for i in range(t):
    l = int(input())
    ary = [[0 for _ in range(l)] for _ in range(l)]
    x, y = list(map(int, input().split()))
    ex, ey = list(map(int, input().split()))
    ary[x][y] = 1
    print(bfs(x, y, ex, ey))