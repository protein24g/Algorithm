n = int(input())
ary = [int(input()) for _ in range(n)]

chk = ary[len(ary)-1]
cnt = 0
for i in range(len(ary)-2, -1, -1):
    tmp = ary[i] - chk
    if tmp >= 0:
        cnt += tmp + 1
        chk -= 1
    else:
        chk = ary[i]
print(cnt)
