def solution(common):
    answer = 0
    a=common[0]
    b=common[1]
    c=common[2]

    if(c-b==b-a):
        answer = common[-1]+(b-a)
    elif(c/b==b/a and a!=0):
        answer = common[-1]*(b/a)
    return answer