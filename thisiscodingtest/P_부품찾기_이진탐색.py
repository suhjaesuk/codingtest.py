def solution(parts, target): # 이진탐색
    start = 0
    end = len(parts) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == parts[mid]:
            return "YES"
        elif target > parts[mid]:
            start = mid + 1
        elif target < parts[mid]:
            end = mid - 1
    return "NO"

part_count = int(input())
parts = list(map(int,input().split()))
required_part_count = int(input())
required_parts = list(map(int, input().split()))

# 정렬
parts.sort()

for target in required_parts:
    print(solution(parts, target) , end = ' ')

