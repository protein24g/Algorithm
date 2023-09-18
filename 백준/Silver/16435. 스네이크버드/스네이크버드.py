n, l = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()

for i in ary:
    if l >= i:
        l += 1
    elif l < i:
        break
print(l)
