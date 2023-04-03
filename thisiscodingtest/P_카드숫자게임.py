n,m=map(int, input().split())
answer=0

for _ in range(n):
    arr=list(map(int,input().split()))
    smallest_value=min(arr)
    answer=max(answer,smallest_value)

print(answer)