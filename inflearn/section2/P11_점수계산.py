def solution(arr):
    answer=0
    count=0
    for x in arr:
        if x==1:
            count += 1
            answer= answer + count


        elif x==0:
            count=0
    return answer
arr=[1,0,1,1,1,0,0,1,1,0]
print(solution(arr))