from collections import deque

q = deque()
N, K = list(map(int, input().split()))

ary = [i for i in range(1, N+1)]

cnt = 0
index = 0
res = []
while ary:
    index += K - 1
    if index >= len(ary):
        index %= len(ary)
    res.append(str(ary.pop(index)))
print("<", ", ".join(res), ">", sep="")
