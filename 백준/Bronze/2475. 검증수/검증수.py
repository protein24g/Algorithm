n = list(map(int, input().split()))
s = 0
for i in n: s += i*i
print(s%10)
