K, N = list(map(int, input().split()))
ary = []
for i in range(K):
    ary.append(int(input()))

start = 1
end = max(ary)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += ary[i] // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
