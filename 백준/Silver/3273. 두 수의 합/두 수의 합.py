n = int(input())
ary = list(map(int, input().split()))
x = int(input())
ary.sort()

res = 0
left, right = 0, n-1
while left < right:
    tmp = ary[left] + ary[right]
    if tmp == x:
        res += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1
print(res)
