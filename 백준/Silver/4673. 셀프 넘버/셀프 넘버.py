numbers = [i for i in range(1, 10001)]
remove_list = []
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if i <= 10000:
        remove_list.append(i)
for i in set(remove_list):
    numbers.remove(i)
for i in numbers:
    print(i)
