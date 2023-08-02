N, M = list(map(int, input().split()))
r = 100 * N
if r - M >= 0:
    print('Yes')
else:
    print('No')