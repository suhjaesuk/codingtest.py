n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
sum=arr[0] # 반복문이 0 부터 시작할 경우 첫번째 값이 i%k==0 조건문에 걸리게 되므로
           # sum에 첫번째 값을 넣은 후 반복문을 1부터 시작한다.

for i in range(1,m):
    if i%k!=0:
        sum+=arr[0]
    elif i%k==0:
        sum+=arr[1]

print(sum)