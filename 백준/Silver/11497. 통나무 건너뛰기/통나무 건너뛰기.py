import sys
input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    ary = list(map(int, input().split()))
    ary.sort()
    chk = True
    odd, even = [], []
    while ary:
        if chk:
            odd.append(ary.pop(0))
            chk = False
        else:
            even.append(ary.pop(0))
            chk = True
    odd = odd + even[::-1]
    res = 0
    for i in range(1, len(odd)):
        res = max(res, abs(odd[i-1] - odd[i]))
    print(res)
