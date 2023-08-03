def solution(n):
    def hanoi(n, fr, to, Sub):
        if n == 1:
            answer.append([fr, to])
            return
        hanoi(n - 1, fr, Sub, to)
        answer.append([fr, to])
        hanoi(n - 1, Sub, to, fr) 
        
    answer = []
    hanoi(n, 1, 3, 2)
    return answer