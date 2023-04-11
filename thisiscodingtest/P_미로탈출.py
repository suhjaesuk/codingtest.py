from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    answer = 0

    while queue:
        start_x, start_y = queue.popleft()
        for i in range(4):
            cur_x = start_x + dx[i]
            cur_y = start_y + dy[i]
            if cur_x < 0 or cur_y < 0 or cur_x >= n or cur_y >= m:
                continue
            if miro[cur_x][cur_y] == 0:
                continue
            if miro[cur_x][cur_y] == 1 and not visited[cur_x][cur_y]:
                visited[cur_x][cur_y] = True
                answer += 1
                queue.append((cur_x, cur_y))
    # 최단거리 반환
    return miro[n-1][m-1]

print(bfs(0, 0))