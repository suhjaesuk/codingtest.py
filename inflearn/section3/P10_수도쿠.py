def solution(arr):
    set1=set()

    #박스에 중복된 숫자가 있으면 return "NO"
    for i in range(3):
        for q in range(3):
            for j in range(3):
                for k in range(3):
                    set1.add(arr[3*i+j][3*q+k])
            if len(set1)!=9:
                return "NO"
            set1.clear()

    #가로 검증
    for i in range(len(arr)):
        for j in range(len(arr)):
            set1.add(arr[i][j])

        if len(set1) != 9:
            return "NO"
        set1.clear()

    #세로 검증
    for i in range(len(arr)):
        for j in range(len(arr)):
            set1.add(arr[j][i])

        if len(set1) != 9:
            return "NO"
        set1.clear()

    return "YES"


arr=[[1,4,3,6,2,8,5,7,9],
     [5,7,2,1,3,9,4,6,8],
     [9,8,6,7,5,4,2,3,1],
     [3,9,1,5,4,2,7,8,6],
     [4,6,8,9,1,7,3,5,2],
     [7,2,5,8,6,3,9,1,4],
     [2,3,7,4,8,1,6,9,5],
     [6,1,9,2,7,5,8,4,3],
     [8,5,4,3,9,6,1,2,7]]

print(solution(arr))