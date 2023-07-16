def recursive_array_sum(index, numbers):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + recursive_array_sum(index + 1, numbers)


numbers = [int(x) for x in input().split()]

print(recursive_array_sum(0, numbers))
