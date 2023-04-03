nd = input()
x= int(nd[1])
y= int(ord(nd[0])) - int(ord('a'))+1
answer=0

dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]

for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    answer+=1

print(answer)