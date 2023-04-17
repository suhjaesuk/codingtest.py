n=int(input())
fears = list(map(int, input().split()))

def solution(fears):
    answer = 0
    fears_dict = {}
    for i in fears:
        if i in fears_dict:
            fears_dict[i] += 1
        else:
            fears_dict[i] = 1

    for i in fears_dict:
        if fears_dict[i] >= i:
            answer += 1

    return answer

print(solution(fears))