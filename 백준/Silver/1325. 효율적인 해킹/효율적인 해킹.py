import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    visited = [False for _ in range(n+1)]
    visited[x] = True
    q = deque([x])
    cnt = 1
    while q:
        x = q.popleft()
        for i in ary[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt        

n, m = map(int, input().split())
ary = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ary[b].append(a)
    
res = []
for i in range(1, n+1): res.append(bfs(i))
m_r = max(res)
for i in range(len(res)):
    if res[i] == m_r:
        print(i+1, end=' ')
