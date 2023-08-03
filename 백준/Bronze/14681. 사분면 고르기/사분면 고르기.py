a = int(input())
b = int(input())
res = 0
if a > 0:
    if b > 0: res = 1
    elif b < 0: res = 4
elif a < 0:
    if b > 0: res = 2
    elif b < 0: res = 3
print(res)