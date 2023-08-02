import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, k):
    q = deque([(n, 0)])
    visited = set([n])

    while q:
        x, cnt = q.popleft()
        if x == k:
            return cnt

        if x - 1 >= 0 and x - 1 not in visited:
            q.append((x - 1, cnt + 1))
            visited.add(x - 1)

        if x + 1 <= 100000 and x + 1 not in visited:
            q.append((x + 1, cnt + 1))
            visited.add(x + 1)

        if 2 * x <= 100000 and 2 * x not in visited:
            q.append((2 * x, cnt + 1))
            visited.add(2 * x)

n, k = list(map(int, input().split()))
print(bfs(n, k))
