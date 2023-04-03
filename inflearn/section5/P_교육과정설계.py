from collections import deque
n=input()
m=int(input())
edu=input()

def solution(n,m,edu):
    n = list(n)
    dq = deque(n)
    edu= deque(edu)

    while edu:
        if edu[0] not in dq:
            edu.popleft()
        else:
            cur = dq.popleft()
            if cur != edu[0]:
                return "NO"

    if len(dq)!=0:
        return "NO"

    return "YES"
print(solution(n,m,edu))