part_count = int(input())
parts = list(map(int,input().split()))
required_part_count = int(input())
required_parts = list(map(int, input().split()))

array = [0]*1000001

for i in parts:
    array[i] = 1

for i in required_parts:
    if array[i] == 1:
        print("YES", end=' ')
    else:
        print("NO", end=' ')

