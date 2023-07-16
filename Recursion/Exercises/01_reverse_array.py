def reverse_array(index, nums):
    if index == len(nums) - 1:
        return print(nums[index], end=' ')

    reverse_array(index + 1, nums)
    return print(nums[index], end=' ')


numbers = [int(x) for x in input().split()]
reverse_array(0, numbers)


# 1 2 3 4 5 6

# def reverse_array(index, elements):
#     if index == len(elements) // 2:
#         return
#
#     swap_index = len(elements) - 1 - index
#     elements[index], elements[swap_index] = elements[swap_index], elements[index]
#     reverse_array(index + 1, elements)
#
#
# elements = input().split()
#
# reverse_array(0, elements)
#
# print(''.join(elements))

