from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    idx = 1
    visited = [0] * (N+1)
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        visited[x] = 1
        if not tree[x]:
            continue

        nex = []
        for i in tree[x]:
            if not visited[i]:
                nex.append(i)
                visited[i] = 1

        l = len(nex)
        for k in range(idx, idx+l):
            if res[k] in nex:
                q.append(res[k])
            else:
                return 0
        idx += l
 
    return 1
    
N = int(input())
tree = [[] for n in range(N+1)]
for n in range(N-1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

res = list(map(int, input().split()))
if res[0] == 1:
    print(bfs(1))
else:
    print(0)
