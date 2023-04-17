part_count = int(input())
parts = set(map(int,input().split()))
required_part_count = int(input())
required_parts = list(map(int, input().split()))

for i in required_parts:
    if i in parts:
        print("YES")
    else:
        print("NO")