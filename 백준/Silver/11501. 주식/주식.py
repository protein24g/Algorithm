import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    ary = list(map(int, input().split()))
    res, m = 0, 0
    for i in range(len(ary)-1, -1, -1):
        if m < ary[i]: m = ary[i]
        elif m > ary[i]:
            res += m - ary[i]
    print(res)
                
