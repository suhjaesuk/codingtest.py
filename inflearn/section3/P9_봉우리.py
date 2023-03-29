def solution(n,arr):
    answer = 0
    newArr=[[0]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            newArr[i+1][j+1] = arr[i][j]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(1,n+1):
        for j in range(1,n+1):

            if all(newArr[i][j] > newArr[i+dx[k]][j+dy[k]] for k in range(4)):
                answer +=1

    return answer

n = 5
arr=[[5,3,7,2,3],
     [3,7,1,6,1],
     [7,2,5,3,4],
     [4,3,6,4,1],
     [8,7,3,5,3]]

print(solution(n,arr))