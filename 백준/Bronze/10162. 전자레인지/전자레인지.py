A = 300; B = 60; C = 10

T = int(input())
result = []
cnt = 0

result.append(T // A)
T -= (T // A * A)

result.append(T // B)
T -= (T // B * B)

result.append(T // C)
T -= (T // C * C)

if T != 0:
    print('-1')
else:
    print(*result)