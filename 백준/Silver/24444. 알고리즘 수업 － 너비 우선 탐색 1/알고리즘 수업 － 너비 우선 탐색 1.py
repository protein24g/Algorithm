from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    global count

    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        ary[v].sort()
        for g in ary[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)
                
n, m, r = map(int, input().split())
ary = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    ary[a].append(b)
    ary[b].append(a)


bfs(r)

for v in visited[1:]:
    print(v)