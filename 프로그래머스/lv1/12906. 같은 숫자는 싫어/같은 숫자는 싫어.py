def solution(arr):
    answer = str(arr[0])
    for i in arr:
        if answer[-1] != str(i):
            answer += str(i)
    
    return list(map(int, answer))