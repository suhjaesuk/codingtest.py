def solution(n, arr):
    min=101
    avg = round((sum(arr)/n))

    for idx, x in enumerate(arr):
        tmp = abs(x-avg)
        if tmp<min:
            min=tmp
            score=x
            res=idx+1
        elif tmp==min: #점수차가 같을때 높은 숫자를 반환
            if x>score:
                score=x
                res=idx+1
    return avg, res





n = 10
arr = [45,73,66,87,92,67,75,79,75,80]
print(solution(n,arr))