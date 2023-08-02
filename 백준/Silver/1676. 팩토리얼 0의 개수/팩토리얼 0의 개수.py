n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i

count = 0
while fact % 10 == 0:
    count += 1
    fact //= 10

print(count)
