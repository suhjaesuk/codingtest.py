def solution(arr):
    answer = 0

    for i in range(7):
        for j in range(3):
            #가로검증
            if arr[j][i]==arr[j+4][i] and arr[j+1][i] == arr[j+3][i]:
                answer +=1

            # 세로 검증
            if arr[i][j]==arr[i][j+4] and arr[i][j+1]==arr[i][j+3]:
                answer+=1

    return answer

arr = [[2,4,1,5,3,2,6],
       [3,5,1,8,7,1,7],
       [8,3,2,7,1,3,8],
       [6,1,2,3,2,1,1],
       [1,3,1,3,5,3,2],
       [1,1,2,5,6,5,2],
       [1,2,2,2,2,1,5]]

print(solution(arr))