def solution(n, arr):
    answer = 1
    applicant = []
    for i in range(n):
        applicant.append((arr[i][0], arr[i][1]))
    applicant.sort(reverse=True)

    max_weight = applicant[0][1]

    for i in range(1,n):
        if max_weight<applicant[i][1]:
            answer+=1
            max_weight=applicant[i][1]

    return answer

n=5
arr=[[172,67],[183,65],[180,70],[170,72],[181,60]]
print(solution(n,arr))