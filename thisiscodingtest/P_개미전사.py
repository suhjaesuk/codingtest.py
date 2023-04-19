n = int(input())
storage = list(map(int, input().split()))

dp_table = [0] * 101

dp_table[0] = storage[0]
dp_table[1] = max(storage[0], storage[1])

for i in range(2, n):
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + storage[i])

print(dp_table[n-1])
