import sys
from collections import deque
sys.setrecursionlimit(10**6)

def bfs(x, y):
    global r, c
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        if ary[x][y] == 'G': return visited[x][y]
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0:
                    if ary[nx][ny] != 'X':
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])
    return -1
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = int(input())
for i in range(t):
    r, c = list(map(int, input().split()))
    visited = [[0 for _ in range(c)] for _ in range(r)]
    ary = []
    for i in range(r): ary.append(list(map(str, input())))
    tmp = bfs(1, 1)
    if tmp == -1: print('No Exit')
    else: print('Shortest Path:', tmp)
