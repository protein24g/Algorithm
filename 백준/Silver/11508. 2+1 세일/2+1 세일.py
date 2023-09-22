n = int(input())
ary = [int(input()) for _ in range(n)]
ary.sort(reverse=True)
s = 0
for i, j in enumerate(ary):
    if (i+1) % 3 != 0:
        s += j
print(s)
