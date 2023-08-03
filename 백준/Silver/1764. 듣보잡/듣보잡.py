import sys
input = sys.stdin.readline
n, m = map(int, input().split())

names = set()
result = []

for i in range(n):
    names.add(input().rstrip())

for j in range(m):
    name = input().rstrip()
    if name in names:
        result.append(name)

result.sort()
print(len(result))
for name in result:
    print(name)
