import sys
input = sys.stdin.readline
from collections import deque

def check(x, y):
    c = 0
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if ary[nx][ny] == 0:
                c += 1
    return c

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and ary[nx][ny] != 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True                    
                

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = list(map(int, input().split()))
ary = []
for _ in range(N):
    ary.append(list(map(int, input().split())))

res = 0
while True:
    res += 1
    ary2 = []
    for i in range(N):
        tmp = []
        for j in range(M):
            if ary[i][j] != 0: tmp.append(max(0, ary[i][j] - check(i, j)))
            else: tmp.append(0)
        ary2.append(tmp)
    ary = ary2
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt, zero_cnt = 0, 0
    for i in range(N):
        if sum(ary[i]) == 0:
            zero_cnt += 1
        else:
            for j in range(M):
                if ary[i][j] != 0 and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1

    if cnt >= 2:
        print(res)
        break
    elif zero_cnt == N:
        print(0)
        break
    
