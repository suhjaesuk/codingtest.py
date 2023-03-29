def solution(participant, completion):
    answer = ''
    participant_table={}
    completion_table={}
    for i in participant:
        if i in participant_table:
            participant_table[i]+=1
        else:
            participant_table[i]=1

    for i in completion:
        if i in completion_table:
            completion_table[i] += 1
        else:
            completion_table[i] = 1
    for i in participant:
        if i not in completion_table:
            answer = i
        if i in completion_table:
            if participant_table[i] - completion_table[i] == 1:
                answer = i

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))