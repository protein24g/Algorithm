def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = str(bin(arr1[i])[2:]).zfill(n)
        b = str(bin(arr2[i])[2:]).zfill(n)
        res = ''
        for j in range(n):
            if int(a[j]) or int(b[j]): res += '#'
            else: res += ' '
        answer.append(res)
    return answer