def f(n):
    res = ''
    for i in range(1, n + 1):
        res += str(i)
    return (res.find(str(n)) + 1)

n=int(input())
print(f(n))