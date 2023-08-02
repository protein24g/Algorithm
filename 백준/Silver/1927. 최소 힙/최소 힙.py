import heapq
import sys
input = sys.stdin.readline
q = []
N = int(input())
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q, x)
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
