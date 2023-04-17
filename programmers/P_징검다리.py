def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    rocks.sort()

    while start <= end:
        mid = (start + end) // 2
        remove_stone = 0
        start_stone = 0
        for rock in rocks:
            if rock - start_stone < mid:
                remove_stone += 1
            else:
                start_stone = rock

        if remove_stone > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer