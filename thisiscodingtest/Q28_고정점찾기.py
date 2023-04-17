array_count= int(input())
array = list(map(int, input().split()))

def solve_fixed_point(array):
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(solve_fixed_point(array))