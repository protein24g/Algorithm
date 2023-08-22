A, B, V = map(int, input().split())

days = (V - B - 1) // (A - B) + 1
print(days)