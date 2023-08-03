import copy, sys
from collections import deque
input = sys.stdin.readline

def dfs(cnt):
    global n, m
    if cnt == 3: bfs(); return
    for i in range(n):
        for j in range(m):
            if ary[i][j] == 0:
                ary[i][j] = 1
                dfs(cnt+1)
                ary[i][j] = 0

def bfs():
    global n, m, res
    q = deque()
    m_ary = copy.deepcopy(ary)
    for i in range(n):
        for j in range(m):
            if m_ary[i][j] == 2: q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if m_ary[nx][ny] == 0:
                    m_ary[nx][ny] = 2; q.append((nx, ny))
    cnt = 0
    for i in range(n): cnt += m_ary[i].count(0)
    res = max(res, cnt)
    
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]

res = 0
dfs(0)

print(res)
