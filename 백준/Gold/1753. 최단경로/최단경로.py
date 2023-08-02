import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        ew, ev = heapq.heappop(q)
        if dist[ev] < ew: continue
        for nw, nv in edge[ev]:
            if dist[nv] > ew + nw:
                dist[nv] = ew + nw
                heapq.heappush(q, (dist[nv], nv))

V, E = list(map(int, input().split()))
K = int(input())
edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    edge[u].append((w, v))

dijkstra(K)
 
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
