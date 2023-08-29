n = 1000 - int(input())
d = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in d:
    cnt += n // i
    n %= i
print(cnt)
