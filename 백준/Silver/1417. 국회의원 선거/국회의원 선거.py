n = int(input())
dasom = [int(input())]
ary = [int(input()) for i in range(n-1)]
ary.sort(reverse = True)
if n == 1:
    print(0)
else:
    cnt = 0
    while True:
        if ary[0] >= dasom[0]:
            ary[0] -= 1
            dasom[0] += 1
            cnt += 1
            ary.sort(reverse=True)
        else: break
    print(cnt)
