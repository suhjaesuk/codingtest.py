def solution(n):
    arr=[0]*(n+1)
    count = 0

    for i in range(2,n+1):
        if arr[i]==0:
            count+=1
            for j in range(i,n+1,i):
                arr[j]=1
    return count
n=20
print(solution(n))