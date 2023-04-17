n,required_n = map(int, input().split())
array = list(map(int, input().split()))

def solve_first_index(required_n, array): # 연속되는 첫번째 인덱스 구하기
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == required_n and not array[mid-1] == required_n:
            return mid
        elif array[mid] < required_n:
            start = mid + 1
        else: # array[mid] > required_n and array[mid-1 == required_n
            end = mid -1
    return None

def solve_last_index(required_n, array): # 연속되는 마지막 인덱스 구하기
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == required_n and not array[mid+1] == required_n:
            return mid
        elif array[mid] > required_n:
            end = mid - 1
        else: # array[mid] < required_n and array[mid+1] == required_n
            start = mid + 1
    return None

first_number = solve_first_index(required_n, array)
last_number = solve_last_index(required_n, array)
if first_number is None or last_number is None:
    print(-1)
else:
    print(last_number-first_number+1)