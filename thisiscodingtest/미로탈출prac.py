from collections import deque

n,m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]

            if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
                continue

            if miro[cur_x][cur_y] == 0:
                continue

            if miro[cur_x][cur_y] == 1:
                miro[cur_x][cur_y] = miro[x][y] + 1
                queue.append((cur_x,cur_y))

    return miro[n-1][m-1]

print(bfs(0,0))
