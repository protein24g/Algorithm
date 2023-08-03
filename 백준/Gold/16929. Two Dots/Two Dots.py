import sys
input = sys.stdin.readline

def dfs(x, y, color, cnt, sx, sy):
    global cycle
    
    if cycle is True:
        return

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if nx == sx and ny == sy and cnt >= 4:
                cycle = True
                return
            if ary[nx][ny] == color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, color, cnt+1, sx, sy)
                visited[nx][ny] = 0

def start():
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            cnt = 1
            dfs(i, j, ary[i][j], cnt, i, j)
            if cycle:
                return 'Yes'
    return 'No'

N, M = list(map(int, input().split()))
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

ary = [[a for a in input().rstrip()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cycle = False

print(start())
