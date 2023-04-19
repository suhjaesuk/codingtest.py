row, col = map(int, input().split())
golds = list(map(int, input().split()))

dp_table = []
index = 0
for i in range(row):
    dp_table.append(golds[index:index + col])
    index += col

for j in range(1, col):
    for i in range(row):
        if i == 0:
            left_up = 0
        else:
            left_up = dp_table[i-1][j-1]
        if i == row - 1:
            left_down = 0
        else:
            left_down = dp_table[i + 1][j - 1]
        left = dp_table[i][j - 1]
        dp_table[i][j] = dp_table[i][j] + max(left_up, left_down, left)
result = 0
for i in range(row):
    result = max(result, dp_table[i][col - 1])

print(result)