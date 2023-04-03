n,m=map(int, input().split())
x,y,d = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

# 방문 표시
visited=[[0]*m for _ in range(n)]
visited[x][y]=1

# 북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global d
    d-=1
    if d==-1:
        d=3

answer=1
turn_time=0

while True:
    turn_left()
    nx=x+dx[d]
    ny=y+dy[d]

    if visited[nx][ny]==0 and arr[nx][ny]==0:
        visited[nx][ny]=1
        x,y = nx, ny
        answer+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-dx[d]
        ny=y-dy[d]
        if arr[nx][ny]==0:
            x=nx
            y=nx
        else:
            break
        turn_time=0

print(answer)

