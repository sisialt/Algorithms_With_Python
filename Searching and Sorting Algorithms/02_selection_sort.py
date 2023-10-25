nums = [int(x) for x in input().split()]

for i in range(len(nums)):
    min_num = nums[i]
    min_index = i

    for j in range(i + 1, len(nums)):
        if nums[j] < min_num:
            min_num = nums[j]
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]

print(*nums, sep=' ')
