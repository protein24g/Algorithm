from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = []
q = deque([])
visited = [[False]*M for _ in range(N)]
res = [[-1]*M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 2:
            q.append((i, j))
            visited[i][j] = True
            res[i][j] = 0

        if row[j] == 0:
            res[i][j] = 0
    board.append(row)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and board[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                res[nx][ny] = res[x][y] + 1

for row in res:
    for i in row:
        print(i, end=" ")
    print()
