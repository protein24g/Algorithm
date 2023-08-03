N = int(input())

ary = [[0 for _ in range(101)] for _ in range(101)]

count = 0
for i in range(N):
    x, y = list(map(int, input().split()))
    for j in range(x, x+10):
        for k in range(y, y+10):
            if ary[j][k] == 0:
                ary[j][k] = 1
                count += 1
print(count)