def solution(weights):

    answer = 0

    table = {}

    for i in weights:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1

    for i in table:
        # 같은 무게만큼 더하기
        if table[i] > 1:
            answer += (table[i] * (table[i] - 1)) / 2
        if i * 2 in table:
            answer += table[i] * table[2 * i]
        if i * 2 / 3 in table:
            answer += table[i] * table[i * 2 / 3]
        if i * 3 / 4 in table:
            answer += table[i] * table[i * 3 / 4]

    return answer

print(solution([100,180,360,100,270]))