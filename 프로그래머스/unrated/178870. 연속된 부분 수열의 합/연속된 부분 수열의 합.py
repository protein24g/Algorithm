def solution(sequence, k):
    answer = []
    left, right = 0, -1
    s = 0
    while True:
        if s < k:
            right += 1
            if right >= len(sequence): break
            s += sequence[right]
        else:
            s -= sequence[left]
            if left >= len(sequence): break
            left += 1
        if s == k:
            answer.append([left, right])
            
    answer.sort(key = lambda x: (x[1]-x[0], x[0]))
    return answer[0]