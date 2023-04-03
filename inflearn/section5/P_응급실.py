from collections import deque
n,m = map(int, input().split())
arr = list(map(int, input().split()))

dq = [(index, value) for index, value in enumerate(arr)]
dq = deque(dq)
cnt=0

while True:
    cur=dq.popleft()
    if any(cur[1]<x[1] for x in dq):
        dq.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break

print(cnt)