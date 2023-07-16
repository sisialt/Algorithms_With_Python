def calculate_recursive_factorial(n):
    if n == 0:
        return 1
    return n * calculate_recursive_factorial(n - 1)


n = int(input())
print(calculate_recursive_factorial(n))
