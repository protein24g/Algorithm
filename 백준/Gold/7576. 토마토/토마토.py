from collections import deque
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x, n_y = x + d[i][0], y + d[i][1]
            if N > n_x >= 0 and M > n_y >= 0 and ary[n_x][n_y] == 0:
                queue.append([n_x, n_y])
                ary[n_x][n_y] = ary[x][y] + 1

M, N = list(map(int, input().split()))

ary = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(M):
        if ary[i][j] == 1:
            queue.append([i, j])

bfs()

result = 0
for i in range(N):
    for j in range(M):
        if ary[i][j] == 0:
            print(-1)
            exit(0)
    tmp = max(ary[i])
    result = max(result, tmp)
print(result-1)