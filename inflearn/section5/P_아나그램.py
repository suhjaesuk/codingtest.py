a= input()
b= input()

def solution(a,b):
    tableA = {}
    tableB = {}

    for i in a:
        if i in tableA:
            tableA[i]+=1
        else:
            tableA[i]=1

    for i in b:
        if i in tableB:
            tableB[i]+=1
        else:
            tableB[i]=1

    for i in tableA:
        if tableA[i]!= tableB[i]:
            return "NO"

    for i in tableB:
        if tableA[i]!= tableB[i]:
            return "NO"

    return "YES"

print(solution(a,b))