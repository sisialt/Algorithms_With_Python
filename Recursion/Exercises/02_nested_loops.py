def recursive_nested_loops(index, nums):
    if index == len(nums):
        print(*nums, sep=' ')
        return

    for num in range(1, len(nums) + 1):
        nums[index] = num
        recursive_nested_loops(index + 1, nums)


n = int(input())
numbers = [0] * n
recursive_nested_loops(0, numbers)
