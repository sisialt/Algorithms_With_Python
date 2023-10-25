def binary_search(nums, searched_num):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2  # it was without ()
        mid_el = nums[mid_idx]

        if searched_num == mid_el:
            return mid_idx

        if searched_num > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1  # it was False


nums = [int(x) for x in input().split()]
searched_num = int(input())

print(binary_search(nums, searched_num))


# def recursive_binary_search(left, right, searched_num, nums):
#     mid_idx = (left + right) // 2
#     mid_el = nums[mid_idx]
#
#     if searched_num == mid_el:
#         return mid_idx
#
#     if searched_num > mid_el:
#         left = mid_idx + 1
#     else:
#         right = mid_idx - 1
#
#     if left <= right:
#         return recursive_binary_search(left, right, searched_num, nums)
#
#     return -1
#
#
# nums = [int(x) for x in input().split()]
# searched_num = int(input())
#
# left = 0
# right = len(nums) - 1
#
# print(recursive_binary_search(left, right, searched_num, nums))

# print(searched_index)
