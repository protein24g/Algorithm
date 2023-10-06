S = list(map(str, input()))
T = list(map(str, input()))

while len(T) >= len(S):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]
    if S == T:
        print(1)
        exit(0)
print(0)
