from itertools import combinations
def solution(n,m):
    cnt = [0]* (n+m+3)
    max = 0
    answer = []
    for i in range(1,n+1):
        for j in range(1,m+1):
            cnt[i+j]+=1

    for i in range(n+m+1):
        if cnt[i]>max:
            max=cnt[i]

    for i in range(n+m+1):
        if cnt[i] == max:
            answer.append(i)
    return answer
n = 4
m = 6
print(solution(n,m))