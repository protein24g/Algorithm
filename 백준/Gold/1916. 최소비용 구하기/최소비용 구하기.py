import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    dist[start] = 0

    while q:
        c, v = heapq.heappop(q)
        if dist[v] < c:
            continue
        for nc, nv in ary[v]:
            if dist[nv] > nc + c:
                dist[nv] = nc + c
                heapq.heappush(q, [dist[nv], nv])

N = int(input())
M = int(input())
INF = 1e9
ary = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
for i in range(M):
    a, b, c = list(map(int, input().split()))
    ary[a].append([c, b])

fr, to = list(map(int, input().split()))
dijkstra(fr)
print(dist[to])
