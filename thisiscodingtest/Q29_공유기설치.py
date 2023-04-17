home_count, wifi_count = map(int, input().split())

homes = []
for _ in range(home_count):
    homes.append(int(input()))

homes.sort()

def solve_wifi_max_distance(homes, wifi_count):
    start = 1 # 최소 거리
    end = homes[-1] - homes[0] # 최대 거리
    result = 0

    while (start <= end):
        mid = (start + end) // 2
        value = homes[0]
        count = 1
        for i in range(1, home_count):
            if homes[i] >= value + mid:
                value = homes[i]
                count += 1
        if count >= wifi_count:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

print(solve_wifi_max_distance(homes, wifi_count))