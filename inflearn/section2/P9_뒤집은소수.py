def solution(n,arr):

    answer =[]
    for x in arr:
        reverseNum = reverse(x)
        if isPrime(reverseNum):
            answer.append(reverseNum)
    return answer




def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True


def reverse(x):
    num=0
    while x!=0:
        tmp = x%10
        x=x//10
        num=num*10 + tmp
    return num



n=5
arr=[32,55,62,3700,250]
print(solution(n,arr))