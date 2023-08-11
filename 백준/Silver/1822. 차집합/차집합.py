a, b = map(int, input().split())
a_ary = set(map(int, input().split()))
b_ary = set(map(int, input().split()))

res = a_ary - b_ary
if res:
    print(len(res))
    print(*sorted(res))
else:
    print(0)
    