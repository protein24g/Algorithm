N = int(input())
t = list(map(int, input().split()))

t.sort()
ary = []

if len(t) % 2 == 1:
    ary.append(t[-1])
    t.remove(t[-1])

while t:
    a = t[0]; b = t[-1]
    t.remove(t[0]); t.remove(t[-1])
    ary.append(a+b)
print(max(ary))