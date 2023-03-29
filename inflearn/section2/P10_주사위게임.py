def solution(arr):
    table = {1:0, 2:0, 3:0, 4:0,5:0, 6:0}
    arr.sort()

    for x in arr:
        table[x]= table[x]+1

    max = 0
    for x in range(1,7):

        if max<table[x]:
            max=table[x]
            memory = x

        if max==3:
            return 10000+memory*1000
        elif max==2:
            return 1000+memory*100
        elif max ==1:
            return 100*arr[2]



arr = [6,2,5]
print(solution(arr))