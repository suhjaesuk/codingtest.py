num,m=map(int, input().split())
# 숫자를 하나씩 쪼개기
num = list(map(int,str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:m]

print(stack)