n,m = map(int, input().split())
ice_board = []
for i in range(n):
    ice_board.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice_board[x][y] == 0:
        ice_board[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer += 1

print(answer)

