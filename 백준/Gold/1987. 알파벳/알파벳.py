import sys
input = sys.stdin.readline

def dfs(x, y, z):
    global R, C, cnt

    cnt = max(cnt, z)
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < R and 0 <= ny < C:
            if ary[nx][ny] not in result:
                result.add(ary[nx][ny])
                dfs(nx, ny, z + 1)
                result.remove(ary[nx][ny])

R, C = list(map(int, input().split()))

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ary = [list(map(str, input())) for _ in range(R)]

cnt = 1
result = set(ary[0][0])
dfs(0, 0, cnt)
print(cnt)