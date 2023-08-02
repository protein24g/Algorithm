from collections import deque 
import sys 
input = sys.stdin.readline

def bfs():
    global sword
    q = deque()
    visited[0][0] = 1
    q.append([0, 0]) 
    while q: 
        x, y = q.popleft() 
        if ary[x][y] == 2: 
            sword = n-1-x + m-1-y + visited[x][y]-1 
        if x == n-1 and y == m-1:
            return min(visited[x][y]-1, sword) 
        for i in range(4): 
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] != 1:
                if visited[nx][ny] == 0: 
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1 
    return sword

d = [(-1,0), (1, 0), (0, -1), (0, 1)] 
n, m, t = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)] 
visited = [[0 for _ in range(m)] for _ in range(n)] 
sword = 1000000 
res = bfs()
if res > t: print('Fail')
else: print(res)