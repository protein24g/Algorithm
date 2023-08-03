from collections import deque
def solution(n, edge):
    def bfs(x):
        q = deque()
        q.append(x)
        visited[x] = 0
        
        while q:
            x = q.popleft()
            for i in ary[x]:
                if i != 1 and visited[i] == 0:
                    visited[i] = visited[x] + 1
                    q.append(i)
                
        
    visited = [0 for _ in range(n+1)]
    answer = 0
    ary = [[] for _ in range(n+1)]
    edge.sort()
    for i in range(len(edge)):
        a, b = edge[i]
        ary[a].append(b)
        ary[b].append(a)
    bfs(1)
    return visited[1:].count(max(visited[1:]))