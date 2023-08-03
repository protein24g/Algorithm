from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    count = 0
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + (num2 * 2))
        count += 1
    if scoville[0] >= K: return count
    return -1