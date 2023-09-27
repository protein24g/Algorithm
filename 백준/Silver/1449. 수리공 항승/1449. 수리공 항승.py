n, l = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()
start = ary[0] - 0.5
end = start + l
cnt = 1

for i in ary:
    if start < i < end:
        continue
    else:
        cnt += 1
        start = i - 0.5
        end = start + l
print(cnt)
