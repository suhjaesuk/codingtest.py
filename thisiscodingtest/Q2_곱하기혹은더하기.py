n = input()
def solution(n):
    answer = int(n[0])
    for i in range(1, len(n)):
        if int(n[i]) <= 1 or answer <= 1:
            answer += int(n[i])
        else:
            answer *= int(n[i])
    return answer

print(solution(n))