def generate_vectors(index, vector):
    if index == n:
        print(*vector, sep='')
        return

    for num in range(2):
        vector[index] = num
        generate_vectors(index + 1, vector)


n = int(input())
vector = [0] * n
generate_vectors(0, vector)
