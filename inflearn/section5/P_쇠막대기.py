def solution(arr):
    stack=[]
    answer=0
    prev=''
    for i in arr:
        if prev=='(' and i ==')':
            stack.pop()
            answer+=len(stack)
        elif i==')':
            stack.pop()
            answer+=1
        elif i=='(':
            stack.append(')')
        prev=i
    return answer

arr='(((()(()()))(())()))(()())'
print(solution(arr))