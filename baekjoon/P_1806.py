import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
l = 0
r = 1
answer=0

while (l<=r and r<=n):

    #구간 합 계산
    total = sum(arr[l:r])

    if(total < m):
        r+=1
    elif(total > m):
        l+=1
    else:
        answer+=1
        r+=1

print(answer)