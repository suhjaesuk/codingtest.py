def solution(n, arr):
    answer=0
    maxSum=0
    for x in arr:
        tmp=0
        s=x
        while s!=0:
            tmp=tmp+s%10
            s=s//10

        if maxSum<tmp:
            answer = x
            maxSum=tmp
    return answer

n = 3
arr = [125,15232,97]
print(solution(n,arr))