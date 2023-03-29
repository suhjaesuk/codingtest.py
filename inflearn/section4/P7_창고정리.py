def solution(n,arr,m):
    arr.sort()
    answer = 0

    for i in range(m):
        arr[0] = arr[0]+1
        arr[n-1] = arr[n-1]-1
        arr.sort()

    answer = arr[n-1] - arr[0]
    return answer




n=6
arr=[1,2,3,4,5,10]
m=3

print(solution(n,arr,m))