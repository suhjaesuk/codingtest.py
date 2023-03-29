n, m = map(int, input().split())

ice_board = []
for i in range(n):
    ice_board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def dfs(start_x, start_y):

    # 시작 노드 방문 처리
    ice_board[start_x][start_y] = 1

    # 시작 노드와 인접한 모든 노드 탐색
    for i in range(4):
        cur_x = start_x + dx[i]
        cur_y = start_y + dy[i]

        if (cur_x >= 0 and cur_x < n and cur_y >= 0 and cur_y < m):

            # 인접 노드에 음료수를 채울 수 있는 경우
            if (ice_board[cur_x][cur_y] == 0):

                # 인접 노드 방문
                dfs(cur_x, cur_y)

# 모든 위치에 음료수 채우기
for i in range(n):
    for j in range(m):
        if (ice_board[i][j] == 0):
            dfs(i,j)
            count += 1

print(count)