cake_count,required_cake_height = map(int, input().split())
cakes = list(map(int, input().split()))

def solve_cutter_height(cakes, required_cake_height):
    start = 0
    result = 0
    end = max(cakes)
    while start <= end:
        temp = 0
        mid = (start+end)//2
        for i in cakes:
            if i > mid:
                temp += i - mid
        if temp < required_cake_height:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(solve_cutter_height(cakes, required_cake_height))