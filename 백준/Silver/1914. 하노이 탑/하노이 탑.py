def hanoi(c, fr, tmp, to):
    if c == 0:
        return
    
    hanoi(c-1, fr, to, tmp)
    print(fr, to)
    hanoi(c-1, tmp, fr, to)

N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(N, 1, 2, 3)
