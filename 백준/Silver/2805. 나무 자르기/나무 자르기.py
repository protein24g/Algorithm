N, M = list(map(int, input().split()))

ary = list(map(int, input().split()))

start = 0; end = max(ary)

while start <= end:
    mid = (start + end) // 2
    target = 0
    for i in ary:
        if i > mid:
            target += i - mid
    if target < M:
        end = mid - 1
    elif target >= M:
        start = mid + 1

print(end)