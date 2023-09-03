s = int(input())
n, cnt = 1, 0
res = 0
while res < s:
    n += 1
    res += n
    cnt += 1
print(cnt)
