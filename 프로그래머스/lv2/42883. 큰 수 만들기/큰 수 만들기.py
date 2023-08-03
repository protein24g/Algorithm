def solution(number, k):
    answer = ''
    number = list(number)
    st = []
    for i in range(len(number)):
        while st and st[-1] < number[i] and k > 0:
            st.pop()
            k -= 1
        st.append(number[i])
    answer = ''.join(st[:len(st) - k])
    return answer