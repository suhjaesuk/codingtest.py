n = int(input())
soldiers = list(map(int, input().split()))
answer = 0
for i in range(len(soldiers) - 1):
    if soldiers[i] < soldiers[i+1]:
        answer += 1
print(answer)