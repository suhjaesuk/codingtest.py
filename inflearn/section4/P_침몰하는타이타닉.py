from collections import deque


def solution(n,m,arr):
    answer = 0
    arr.sort()
    arr = deque(arr)
    while arr:
        if len(arr)==1:
            answer+=1
            break
        if arr[0]+arr[-1]>m:
            arr.pop()
            answer+=1
        else:
            arr.popleft()
            arr.pop()
            answer+=1

    return answer

n=5
m=140
arr=[90,50,70,100,60]
print(solution(n,m,arr))