# 해시테이블 풀이
def longestConsecutive1(nums):
    longest = 0
    num_dict = {}
    for num in nums:
        num_dict[num] = True

    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    print(longest)
    return longest

nums = [6,7,100,5,4,4]
longestConsecutive1(nums)

# 투포인터 풀이
def longestConsecutive2(nums):
    longest = 0
    count = 1
    tail=0
    head=1
    nums.sort()

    while head < len(nums):
        if nums[tail]+1 == nums[head]:
            count = count+1
            longest = max(longest, count)
        else: count=1

        tail= tail+1
        head= head+1

    return longest

nums = [6,7,100,5,4,4]
print(longestConsecutive2(nums))