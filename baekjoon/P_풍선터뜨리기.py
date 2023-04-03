n=int(input())
paper=list(map(int,input().split()))

def solution(n,paper):
    start=0
    balloons=[x for x in range(1,n+1)]
    answer=[]
    temp = paper.pop(start)
    answer.append(balloons.pop(start))

    while paper:
        if temp<0:
            start = (start+temp)%len(paper)
        else:
            start=(start+temp-1)%len(paper)
        temp = paper.pop(start)
        answer.append(balloons.pop(start))

    return answer

print(solution(n,paper))