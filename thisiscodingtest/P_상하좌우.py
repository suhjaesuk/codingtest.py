n=int(input())
directions=list(input().split())

x,y=1,1
nx,ny = 0,0
dx=[0,0,-1,1]
dy=[-1,1,0,0]
direction_type=['L', 'R', 'U', 'D']

for direction in directions:
    for i in range(len(direction_type)):
        if direction == direction_type[i]:
            nx = x+dx[i]
            ny = y+dy[i]

        if nx<1 or nx>n or ny<1 or ny>n:
            continue
        x,y = nx, ny

print(x,y)

