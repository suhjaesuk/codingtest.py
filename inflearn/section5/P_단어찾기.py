n=int(input())
list =[]
for i in range(2*n-1):
    list.append(input())

def solution(list):
    word = {}
    for i in list:
        if i in word:
            word[i]+=1
        else:
            word[i]=1

    for i in word:
        if word[i]==1:
            return i

print(solution(list))
