import sys
from collections import deque
input = sys.stdin.readline

def dfs(k):
    global N
    visited[k] = 1
    print(k, end=' ')
    for i in range(1, N+1):
        if ary[k][i] and visited[i] == 0:
            dfs(i)

def bfs(k):
    global N
    q = deque()
    q.append(k)
    visited[k] = 1
    
    while q:
        tmp = q.popleft()
        print(tmp, end=' ')
        for i in range(1, N+1):
            if ary[tmp][i] and visited[i] == 0:
                visited[i] = 1
                q.append(i)
    
    
N, M, V = list(map(int, input().split()))
ary = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    fr, to = list(map(int, input().split()))
    ary[fr][to] = 1
    ary[to][fr] = 1

visited = [0] * (N+1)
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)
